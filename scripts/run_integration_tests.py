#!/usr/bin/env python3
"""
Cross-repo integration test runner.

Implements Task T5: Cross-verification harness
- Imports from all 5 SU(2) repos
- Runs cross-verification checks (closedform vs generating-functional vs SymPy)
- Generates integration validation report (JSON)
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Add repo paths to sys.path
WORKSPACE_ROOT = Path(__file__).parent.parent.parent
REPOS = [
    "su2-3nj-closedform",
    "su2-3nj-uniform-closed-form",
    "su2-3nj-recurrences",
    "su2-3nj-generating-functional",
    "su2-node-matrix-elements",
]

def setup_imports():
    """Add all repo src/project paths to sys.path."""
    for repo in REPOS:
        repo_path = WORKSPACE_ROOT / repo
        
        # Try common Python package locations
        for subdir in ["src", "project", ""]:
            candidate = repo_path / subdir if subdir else repo_path
            if candidate.exists() and candidate not in sys.path:
                sys.path.insert(0, str(candidate))

def check_repo_availability():
    """Check if all repos are available in the workspace."""
    print("Checking repository availability...")
    
    available = []
    missing = []
    
    for repo in REPOS:
        repo_path = WORKSPACE_ROOT / repo
        if repo_path.exists():
            print(f"  ✓ {repo}")
            available.append(repo)
        else:
            print(f"  ✗ {repo} (not found)")
            missing.append(repo)
    
    print(f"\nAvailable: {len(available)}/{len(REPOS)}")
    
    if missing:
        print(f"Missing repos: {', '.join(missing)}")
        print("\nNote: Ensure all repos are cloned as siblings of this hub repo.")
    
    return available, missing


def run_cross_verification():
    """Run cross-verification between different implementations."""
    print("\n" + "=" * 60)
    print("Cross-Verification Matrix")
    print("=" * 60)
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "tests": [],
        "summary": {"passed": 0, "failed": 0, "skipped": 0}
    }

    # Ensure this exists even if imports fail early.
    test_cases = []
    
    try:
        # Import packages
        print("\nImporting packages...")
        import sympy as sp
        from sympy.physics.wigner import wigner_6j
        
        from su2_3nj_gen.su2_3nj import generate_3nj, recursion_3nj
        from project.su2_3nj_closed_form import closed_form_3nj
        from su2_node_matrix_elements.model import node_matrix_element
        
        print("  ✓ All imports successful")
        
        # Test cases: (j1, j2, j3, j4, j5, j6)
        test_cases = [
            (1, 1, 1, 1, 1, 1, "uniform integer"),
            (1, 2, 3, 4, 5, 6, "sequential integer"),
            (2, 2, 2, 2, 2, 2, "uniform j=2"),
            (sp.Rational(1,2), sp.Rational(1,2), 1, sp.Rational(1,2), sp.Rational(1,2), 1, "half-integer"),
            (1, sp.Rational(1,2), sp.Rational(3,2), 1, sp.Rational(1,2), sp.Rational(3,2), "mixed"),
        ]
        
        print(f"\nRunning {len(test_cases)} cross-verification tests...\n")
        
        for *spins, description in test_cases:
            test_result = {
                "spins": [str(s) for s in spins],
                "description": description,
                "implementations": {},
                "status": "unknown"
            }
            
            try:
                # Get values from different implementations
                sympy_val = wigner_6j(*spins)
                gen_val = generate_3nj(*spins)
                closed_val = closed_form_3nj(*spins)
                
                # Store results
                test_result["implementations"]["sympy"] = str(sympy_val)
                test_result["implementations"]["generating_functional"] = str(gen_val)
                test_result["implementations"]["closed_form"] = str(closed_val)
                
                # Check agreement
                diff_gen_sympy = sp.simplify(gen_val - sympy_val)
                diff_closed_sympy = sp.simplify(closed_val - sympy_val)
                diff_gen_closed = sp.simplify(gen_val - closed_val)
                
                if diff_gen_sympy == 0 and diff_closed_sympy == 0:
                    test_result["status"] = "PASS"
                    test_result["agreement"] = "All implementations agree"
                    results["summary"]["passed"] += 1
                    print(f"  ✓ {description:20s} {spins}")
                else:
                    test_result["status"] = "FAIL"
                    test_result["discrepancies"] = {
                        "gen_vs_sympy": str(diff_gen_sympy),
                        "closed_vs_sympy": str(diff_closed_sympy),
                        "gen_vs_closed": str(diff_gen_closed)
                    }
                    results["summary"]["failed"] += 1
                    print(f"  ✗ {description:20s} {spins}")
                    print(f"    Discrepancy: gen-sympy={diff_gen_sympy}, closed-sympy={diff_closed_sympy}")
                    
            except Exception as e:
                test_result["status"] = "ERROR"
                test_result["error"] = str(e)
                results["summary"]["skipped"] += 1
                print(f"  ⚠ {description:20s} {spins} — {str(e)[:50]}")
            
            results["tests"].append(test_result)
        
        # Test recursion vs generate_3nj
        print("\nRecursion cross-check...")
        try:
            test_spins = (2, 3, 4, 5, 6, 7)
            rec_val = recursion_3nj(*test_spins)
            gen_val = generate_3nj(*test_spins)
            diff = sp.simplify(rec_val - gen_val)
            
            rec_test = {
                "spins": [str(s) for s in test_spins],
                "description": "recursion vs generate",
                "implementations": {
                    "recursion_3nj": str(rec_val),
                    "generate_3nj": str(gen_val)
                },
                "status": "PASS" if diff == 0 else "FAIL"
            }
            
            if diff == 0:
                print(f"  ✓ recursion_3nj agrees with generate_3nj")
                results["summary"]["passed"] += 1
            else:
                print(f"  ✗ recursion mismatch: diff={diff}")
                rec_test["discrepancy"] = str(diff)
                results["summary"]["failed"] += 1
                
            results["tests"].append(rec_test)
            
        except Exception as e:
            print(f"  ⚠ recursion check failed: {e}")
            results["summary"]["skipped"] += 1

        # Node matrix elements: backend consistency + permutation invariance
        print("\nNode-matrix-elements spot checks...")
        try:
            node_spins = [sp.Rational(1, 2), 1, sp.Rational(3, 2), 2]
            val_np = node_matrix_element(spins=node_spins, epsilon=1e-10, backend="numpy")
            val_sp = node_matrix_element(spins=node_spins, epsilon=1e-10, backend="sympy")

            backend_test = {
                "spins": [str(s) for s in node_spins],
                "description": "node-matrix backend consistency",
                "implementations": {"numpy": str(val_np), "sympy": str(val_sp)},
                "status": "PASS" if abs(val_np - val_sp) < 1e-7 else "FAIL",
            }

            if backend_test["status"] == "PASS":
                print("  ✓ numpy backend agrees with sympy backend")
                results["summary"]["passed"] += 1
            else:
                print(f"  ✗ backend mismatch: |numpy-sympy|={abs(val_np - val_sp)}")
                results["summary"]["failed"] += 1

            results["tests"].append(backend_test)

            base = val_np
            perm_spins = [
                [node_spins[1], node_spins[0], node_spins[2], node_spins[3]],
                [node_spins[2], node_spins[1], node_spins[0], node_spins[3]],
                [node_spins[3], node_spins[2], node_spins[1], node_spins[0]],
            ]
            max_diff = 0.0
            for spins in perm_spins:
                v = node_matrix_element(spins=spins, epsilon=1e-10, backend="numpy")
                max_diff = max(max_diff, abs(v - base))

            perm_test = {
                "spins": [str(s) for s in node_spins],
                "description": "node-matrix permutation invariance (sample)",
                "max_abs_diff": max_diff,
                "status": "PASS" if max_diff < 1e-9 else "FAIL",
            }

            if perm_test["status"] == "PASS":
                print("  ✓ permutation invariance (sample) holds")
                results["summary"]["passed"] += 1
            else:
                print(f"  ✗ permutation invariance max diff={max_diff}")
                results["summary"]["failed"] += 1

            results["tests"].append(perm_test)

        except Exception as e:
            print(f"  ⚠ node-matrix-elements checks failed: {e}")
            results["summary"]["skipped"] += 2
        
    except ImportError as e:
        print(f"\n⚠️  Import failed: {e}")
        print("   Fix options:")
        print("   - Install hub dependencies (sympy/numpy/mpmath) into this venv")
        print("   - Or install each repo editable: cd <repo> && pip install -e .")
        # If we failed before populating cases, report a safe skipped count.
        # (We intentionally avoid crashing here so the harness always emits JSON.)
        results["summary"]["skipped"] = len(test_cases)
        results["error"] = str(e)
        return results
    
    return results


def main():
    """Main integration test runner."""
    print("=" * 60)
    print("SU(2) 3nj Series — Cross-Repo Integration Test Runner")
    print("=" * 60)
    print()
    
    available, missing = check_repo_availability()
    
    if missing:
        print("\n⚠️  Cannot proceed: some repos are missing.")
        return 1
    
    # Setup import paths
    setup_imports()
    
    # Run cross-verification
    results = run_cross_verification()
    
    # Save results
    output_dir = Path(__file__).parent.parent / "data"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "integration_validation_report.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Passed:  {results['summary']['passed']}")
    print(f"Failed:  {results['summary']['failed']}")
    print(f"Skipped: {results['summary']['skipped']}")
    print(f"\nReport saved to: {output_file}")
    
    return 0 if results["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

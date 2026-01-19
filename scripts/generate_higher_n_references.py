#!/usr/bin/env python3
"""scripts/generate_higher_n_references.py

Generate higher-n reference datasets using high-precision evaluation.

Current scope: 9j reference dataset.

Notes:
- SymPy (as of 1.14) provides `wigner_9j` but not `wigner_12j`/`wigner_15j`.
- We therefore treat 12j/15j as a separate follow-up task pending an explicit
    choice of topology/kind and an agreed computational route.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

try:
    import mpmath as mp
    import sympy as sp
    from sympy.physics.wigner import wigner_9j
except ImportError as e:
    print(f"Error: Required packages not found: {e}")
    print("Install with: pip install sympy mpmath")
    sys.exit(1)

# Set high precision (50 decimal places)
mp.dps = 50


def compute_9j_reference(j_matrix):
    """
    Compute 9j symbol with high precision.
    
    j_matrix: 3x3 matrix of angular momentum values
    Returns: (value_exact, value_numeric, precision_info)
    """
    j1, j2, j3, j4, j5, j6, j7, j8, j9 = [
        item for row in j_matrix for item in row
    ]
    
    try:
        # Exact symbolic computation
        exact = wigner_9j(j1, j2, j3, j4, j5, j6, j7, j8, j9)

        # Deterministic high-precision numeric evaluation
        # (avoid Python float coercion; keep all digits controlled by mp.dps)
        exact_hp = sp.N(exact, mp.dps + 10)
        numeric = mp.nstr(mp.mpf(str(exact_hp)), 30)
        
        # Simplified form
        simplified = sp.simplify(exact)
        
        return {
            "spins": [[str(j) for j in row] for row in j_matrix],
            "exact": str(simplified),
            "numeric_50dps": numeric,
            "status": "success"
        }
    except Exception as e:
        return {
            "spins": [[str(j) for j in row] for row in j_matrix],
            "status": "error",
            "error": str(e)
        }


def generate_9j_dataset():
    """Generate a comprehensive 9j reference dataset."""
    print("Generating 9j reference dataset with high precision...")
    
    cases = []
    
    # Small integer cases
    cases.append(([[1, 1, 1], [1, 1, 1], [1, 1, 1]], "uniform j=1"))
    cases.append(([[2, 2, 2], [2, 2, 2], [2, 2, 2]], "uniform j=2"))
    cases.append(([[1, 2, 3], [2, 3, 4], [3, 4, 5]], "sequential ladder"))
    
    # Half-integer cases
    cases.append((
        [[sp.Rational(1,2), sp.Rational(1,2), 1],
         [sp.Rational(1,2), sp.Rational(1,2), 1],
         [1, 1, 0]],
        "half-integer basic"
    ))
    
    # Mixed integer/half-integer
    cases.append((
        [[1, sp.Rational(1,2), sp.Rational(3,2)],
         [sp.Rational(1,2), 1, sp.Rational(3,2)],
         [sp.Rational(3,2), sp.Rational(3,2), 0]],
        "mixed spin configuration"
    ))
    
    # Edge cases
    cases.append(([[0, 0, 0], [0, 0, 0], [0, 0, 0]], "all zeros"))
    cases.append(([[1, 1, 0], [1, 1, 0], [0, 0, 0]], "partial zeros"))
    
    results = []
    for j_matrix, description in cases:
        print(f"  Computing: {description}")
        result = compute_9j_reference(j_matrix)
        result["description"] = description
        results.append(result)
    
    return results


def analyze_stability(results):
    """Analyze numerical stability and identify failure modes."""
    print("\nAnalyzing stability regimes...")
    
    stability_report = {
        "total_cases": len(results),
        "successful": sum(1 for r in results if r["status"] == "success"),
        "failed": sum(1 for r in results if r["status"] == "error"),
        "notes": []
    }
    
    # Check for zero results
    zero_cases = [r for r in results if r.get("exact") == "0"]
    if zero_cases:
        stability_report["notes"].append(
            f"Found {len(zero_cases)} cases that evaluate to exactly zero (likely triangle violations)"
        )
    
    # Check for failures
    failed_cases = [r for r in results if r["status"] == "error"]
    if failed_cases:
        stability_report["notes"].append(
            f"Failed cases: {[r.get('description', 'unknown') for r in failed_cases]}"
        )
        stability_report["failure_modes"] = [
            {"description": r.get("description"), "error": r.get("error")}
            for r in failed_cases
        ]
    
    return stability_report


def main():
    """Main reference dataset generator."""
    print("=" * 70)
    print("Higher-n Reference Dataset Generator (Task T2)")
    print("=" * 70)
    print(f"Precision: {mp.dps} decimal places\n")
    
    # Generate 9j dataset (stepping stone to 12j/15j)
    results_9j = generate_9j_dataset()
    
    # Analyze stability
    stability = analyze_stability(results_9j)
    
    # Prepare output
    output = {
        "timestamp": datetime.now().isoformat(),
        "precision_dps": mp.dps,
        "symbol_type": "9j",
        "results": results_9j,
        "stability_analysis": stability
    }
    
    # Save to file
    output_dir = Path(__file__).parent.parent / "data"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "higher_n_reference_9j.json"
    
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total cases:    {stability['total_cases']}")
    print(f"Successful:     {stability['successful']}")
    print(f"Failed:         {stability['failed']}")
    
    if stability['notes']:
        print("\nNotes:")
        for note in stability['notes']:
            print(f"  - {note}")
    
    print(f"\nReference dataset saved to: {output_file}")
    print("\nNext steps:")
    print("  - Extend to 12j symbols (requires custom implementation)")
    print("  - Add 15j symbols (highly specialized)")
    print("  - Compare against existing repo implementations")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""
Generate deterministic JSON reference tables for paper inclusion.

This script produces versioned datasets of 3nj symbol values that can be
used in the LaTeX paper and for regression testing.
"""

import json
import os
from pathlib import Path
from su2_3nj_closedform import calculate_3nj, build_rhos


def generate_reference_table(output_path, edge_count=7, precision=50):
    """
    Generate a deterministic reference table of 3nj values.
    
    Parameters:
        output_path: Path to save JSON file
        edge_count: Number of edges (default 7 for 15j-like symbols)
        precision: Decimal precision for calculations
    """
    rhos = build_rhos(edge_count)
    
    # Define test cases with meaningful configurations
    test_cases = [
        # All zeros
        {"j": [0] * edge_count, "label": "all_zeros"},
        # Uniform spins
        {"j": [1] * edge_count, "label": "uniform_1"},
        {"j": [2] * edge_count, "label": "uniform_2"},
        # Sequential
        {"j": list(range(edge_count)), "label": "sequential_0_to_n"},
        # Palindromic
        {"j": [1, 2, 3, 4, 3, 2, 1], "label": "palindromic_1234321"},
        # Mixed
        {"j": [2, 3, 1, 4, 2, 1, 3], "label": "mixed_2314213"},
        # Half-integers
        {"j": [0.5, 1.5, 2.5, 2.5, 1.5, 0.5, 0.5], "label": "half_integers"},
    ]
    
    results = {
        "metadata": {
            "edge_count": edge_count,
            "precision": precision,
            "rhos": [float(r) for r in rhos],
            "version": "1.0",
            "generator": "su2_3nj_closedform.generate_reference_table"
        },
        "values": []
    }
    
    for case in test_cases:
        j = case["j"]
        label = case["label"]
        
        # Calculate value
        value = calculate_3nj(j, rhos, precision)
        
        results["values"].append({
            "label": label,
            "j": j,
            "value": str(value),  # Store as string for exact precision
            "value_float": float(value),  # Convenience float version
        })
    
    # Save to JSON
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Generated reference table: {output_path}")
    print(f"  {len(results['values'])} entries")
    print(f"  Edge count: {edge_count}")
    print(f"  Precision: {precision} decimal places")
    
    return results


def generate_symmetry_table(output_path, edge_count=7, precision=50):
    """
    Generate table demonstrating reflection symmetry.
    
    Parameters:
        output_path: Path to save JSON file
        edge_count: Number of edges
        precision: Decimal precision
    """
    from su2_3nj_closedform import check_reflection_symmetry
    
    test_cases = [
        [0, 1, 2, 3, 4, 5, 6],
        [1, 1, 1, 1, 1, 1, 1],
        [2, 3, 1, 4, 2, 1, 3],
        [1, 2, 3, 4, 3, 2, 1],  # Palindromic
        [0.5, 1.5, 2.5, 1.5, 0.5, 0, 0],
    ]
    
    results = {
        "metadata": {
            "edge_count": edge_count,
            "precision": precision,
            "tolerance": 1e-8,
            "version": "1.0"
        },
        "symmetry_checks": []
    }
    
    for j in test_cases:
        is_symmetric, diff = check_reflection_symmetry(j, precision=precision)
        
        results["symmetry_checks"].append({
            "j": j,
            "is_symmetric": is_symmetric,
            "difference": str(diff),
            "difference_float": float(diff),
            "is_palindromic": j == j[::-1]
        })
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Generated symmetry table: {output_path}")
    print(f"  {len(results['symmetry_checks'])} symmetry checks")
    
    return results


def main():
    """Generate all reference tables for paper inclusion."""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data" / "reference"
    
    print("Generating deterministic reference tables...")
    print("=" * 60)
    
    # Generate main reference table
    ref_path = data_dir / "3nj_reference_values.json"
    generate_reference_table(ref_path, edge_count=7, precision=50)
    
    print()
    
    # Generate symmetry demonstration table
    sym_path = data_dir / "reflection_symmetry_table.json"
    generate_symmetry_table(sym_path, edge_count=7, precision=50)
    
    print()
    print("=" * 60)
    print("All tables generated successfully!")
    print(f"Output directory: {data_dir}")


if __name__ == "__main__":
    main()

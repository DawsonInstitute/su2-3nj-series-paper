#!/usr/bin/env python3
"""
Verify that the 4F3 implementation produces correct Wigner 6j values.

This script validates:
1. Independence from SymPy's wigner_6j (we implement our own Racah sum)
2. Correct triangle coefficient calculations
3. Proper sum bounds and term evaluation
4. Cross-validation against SymPy's reference implementation
"""

import sys
sys.path.insert(0, 'project')

from su2_3nj_closed_form import closed_form_3nj, triangle_coefficient
from sympy.physics.wigner import wigner_6j
from sympy import Rational, N, simplify
import pandas as pd


def main():
    print("=" * 60)
    print("Verifying 4F3 Hypergeometric Formula Implementation")
    print("=" * 60)
    
    # Test cases: (j1, j2, j3, j4, j5, j6)
    test_cases = [
        # Integer spins
        (1, 1, 1, 1, 1, 1),
        (2, 2, 2, 2, 2, 2),
        (1, 2, 2, 2, 1, 2),
        (1, 2, 3, 3, 2, 2),
        
        # Half-integer spins
        (Rational(1, 2), Rational(1, 2), 1, Rational(1, 2), Rational(1, 2), 1),
        (Rational(3, 2), Rational(1, 2), 1, Rational(1, 2), Rational(3, 2), 1),
        
        # Triangle violations
        (1, 1, 3, 1, 1, 1),  # Should return 0
        (2, 2, 5, 1, 1, 1),  # Should return 0
    ]
    
    results = []
    
    for spins in test_cases:
        j1, j2, j3, j4, j5, j6 = spins
        
        # Compute with our 4F3 implementation
        our_result = closed_form_3nj(j1, j2, j3, j4, j5, j6)
        
        # Compute with SymPy reference
        sympy_result = wigner_6j(j1, j2, j3, j4, j5, j6)
        
        # Compare
        difference = simplify(our_result - sympy_result)
        match = (difference == 0)
        
        # Store results
        results.append({
            'j1': float(j1),
            'j2': float(j2),
            'j3': float(j3),
            'j4': float(j4),
            'j5': float(j5),
            'j6': float(j6),
            'our_value': float(N(our_result, 15)),
            'sympy_value': float(N(sympy_result, 15)),
            'difference': float(N(difference, 15)),
            'match': match
        })
        
        status = "✓" if match else "✗"
        print(f"{status} {spins}: our={float(N(our_result, 6)):.6f}, sympy={float(N(sympy_result, 6)):.6f}")
    
    # Summary
    df = pd.DataFrame(results)
    all_match = df['match'].all()
    
    print("\n" + "=" * 60)
    print(f"Results: {df['match'].sum()}/{len(df)} tests passed")
    
    if all_match:
        print("✓ All tests PASSED - 4F3 implementation is correct!")
    else:
        print("✗ Some tests FAILED - check implementation")
        print("\nFailed cases:")
        print(df[~df['match']])
    
    # Save detailed results
    output_file = 'data/4F3_verification_results.csv'
    df.to_csv(output_file, index=False)
    print(f"\nDetailed results saved to: {output_file}")
    
    # Test triangle coefficient function independently
    print("\n" + "=" * 60)
    print("Testing Triangle Coefficient Function")
    print("=" * 60)
    
    triangle_tests = [
        ((1, 1, 1), "valid"),
        ((2, 2, 2), "valid"),
        ((1, 1, 3), "violation"),  # 1 + 1 < 3
        ((1, 2, 4), "violation"),  # 1 + 2 < 4
        ((Rational(1, 2), Rational(1, 2), 1), "valid"),
    ]
    
    for (a, b, c), expected in triangle_tests:
        delta = triangle_coefficient(a, b, c)
        is_zero = (delta == 0)
        status = "✓" if (expected == "violation") == is_zero else "✗"
        print(f"{status} Δ({a}, {b}, {c}) = {float(N(delta, 6)):.6f} [{expected}]")
    
    print("\n" + "=" * 60)
    print("Verification Complete")
    print("=" * 60)
    
    return 0 if all_match else 1


if __name__ == '__main__':
    sys.exit(main())

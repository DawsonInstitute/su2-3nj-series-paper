#!/usr/bin/env python3
"""
Stability report for recurrence-based 6-j computation (R2).

Compares forward vs backward recursion and provides stability metrics.
"""

import sys
import json
import pandas as pd
from sympy import Rational
from sympy.physics.wigner import wigner_6j
from su2_3nj_recur.wigner_6j_recurrence import racah_recurrence_6j
from su2_3nj_recur.recurrence_engine import analyze_stability, compute_forward


def main():
    print("=" * 70)
    print("Recurrence Stability Analysis for Wigner 6-j Symbols")
    print("=" * 70)
    
    # Test cases: (j1, j2, j3, j4, j5, j6_max)
    test_cases = [
        ("uniform_1", 1, 1, 1, 1, 1, 5),
        ("uniform_2", 2, 2, 2, 2, 2, 5),
        ("mixed_1", 1, 2, 2, 2, 1, 5),
        ("mixed_2", 1, 2, 3, 3, 2, 5),
        ("half_int", 0.5, 0.5, 1, 0.5, 0.5, 3),
    ]
    
    results = []
    
    for label, j1, j2, j3, j4, j5, j6_max in test_cases:
        print(f"\nCase: {label} — j1={j1}, j2={j2}, j3={j3}, j4={j4}, j5={j5}")
        print("-" * 70)
        
        # Compute reference values using SymPy
        reference_values = []
        for j6 in range(j6_max + 1):
            if isinstance(j1, float):
                j1_r = Rational(int(2 * j1), 2)
                j2_r = Rational(int(2 * j2), 2)
                j3_r = Rational(int(2 * j3), 2)
                j4_r = Rational(int(2 * j4), 2)
                j5_r = Rational(int(2 * j5), 2)
            else:
                j1_r = Rational(j1)
                j2_r = Rational(j2)
                j3_r = Rational(j3)
                j4_r = Rational(j4)
                j5_r = Rational(j5)
            
            val = float(wigner_6j(j1_r, j2_r, j3_r, j4_r, j5_r, Rational(j6)))
            reference_values.append(val)
        
        # Get recurrence relation
        recurrence = racah_recurrence_6j(j1, j2, j3, j4, j5)
        
        # Analyze stability
        try:
            stability = analyze_stability(
                recurrence,
                reference_values,
                y0=reference_values[0],
                y1=reference_values[1]
            )
            
            max_fwd_err = stability.max_forward_error()
            max_bwd_err = stability.max_backward_error()
            mean_cn = stability.mean_condition_number()
            recommendation = stability.recommend_direction()
            
            print(f"  Max forward error:  {max_fwd_err:.2e}")
            print(f"  Max backward error: {max_bwd_err:.2e}")
            print(f"  Mean condition #:   {mean_cn:.2f}")
            print(f"  Recommendation:     {recommendation}")
            
            results.append({
                'label': label,
                'j1': j1, 'j2': j2, 'j3': j3, 'j4': j4, 'j5': j5,
                'j6_max': j6_max,
                'max_forward_error': max_fwd_err,
                'max_backward_error': max_bwd_err,
                'mean_condition_number': mean_cn,
                'recommended_direction': recommendation,
            })
            
        except Exception as e:
            print(f"  ERROR: {e}")
            results.append({
                'label': label,
                'j1': j1, 'j2': j2, 'j3': j3, 'j4': j4, 'j5': j5,
                'j6_max': j6_max,
                'max_forward_error': None,
                'max_backward_error': None,
                'mean_condition_number': None,
                'recommended_direction': 'error',
            })
    
    # Save CSV
    df = pd.DataFrame(results)
    csv_file = 'data/recurrence_stability_report.csv'
    df.to_csv(csv_file, index=False)
    print(f"\n{'=' * 70}")
    print(f"Stability report saved to: {csv_file}")
    
    # Save JSON
    json_file = 'data/recurrence_stability_report.json'
    with open(json_file, 'w') as f:
        json.dump({
            'metadata': {
                'description': 'Stability analysis for 6-j recurrence relations',
                'note': 'Current implementation uses placeholder recurrence coefficients',
            },
            'results': results
        }, f, indent=2)
    
    print(f"Stability report (JSON) saved to: {json_file}")
    
    # Summary
    print(f"\n{'=' * 70}")
    print("Summary")
    print(f"{'=' * 70}")
    
    if all(r['max_forward_error'] is not None for r in results):
        avg_fwd = sum(r['max_forward_error'] for r in results) / len(results)
        avg_bwd = sum(r['max_backward_error'] for r in results) / len(results)
        
        print(f"Average max forward error:  {avg_fwd:.2e}")
        print(f"Average max backward error: {avg_bwd:.2e}")
        
        recommendations = [r['recommended_direction'] for r in results]
        print(f"Direction recommendations: {dict((x, recommendations.count(x)) for x in set(recommendations))}")
    
    print(f"\n{'=' * 70}")
    print("Note: Current recurrence coefficients are placeholders.")
    print("Full Racah coefficient implementation needed for production use.")
    print(f"{'=' * 70}")
    
    return 0


if __name__ == '__main__':
    # Create data directory if needed
    import os
    os.makedirs('data', exist_ok=True)
    
    sys.exit(main())

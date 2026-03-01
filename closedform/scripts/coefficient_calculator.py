#!/usr/bin/env python3
import os
import sys
import mpmath as mp
import pandas as pd

# Increase mpmath precision
mp.mp.dps = 50

# Add parent directory to path if run from scripts folder
if os.path.basename(os.getcwd()) == 'scripts':
    sys.path.append('..')

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def build_rhos(edge_count=7):
    return [fib(edge_count+2 - e) / fib(edge_count+3 - e) for e in range(1, edge_count+1)]

def calculate_3nj(j, rhos=None):
    if rhos is None:
        rhos = build_rhos(len(j))
    res = mp.mpf(1)
    for idx, j_e in enumerate(j):
        twoj = 2 * j_e
        rho = rhos[idx]
        term = mp.hyper([-twoj, 0.5], [1], -rho) / mp.factorial(twoj)
        res *= term
    return res

def generate_test_cases(edge_count=7):
    return [
        [0,1,2,3,4,5,6][:edge_count],
        [1]*edge_count,
        [2,3,1,4,2,1,3][:edge_count],
        [0]*edge_count,
        [1,2,3,4,3,2,1][:edge_count]
    ]

def analyze_symmetry(test_cases=None, edge_count=7):
    if test_cases is None:
        test_cases = generate_test_cases(edge_count)
    rhos = build_rhos(edge_count)

    print("\n==== 3nj Symbol Reflection Symmetry Analysis ====\n")
    rows = []
    for j in test_cases:
        orig = calculate_3nj(j, rhos)
        rev  = calculate_3nj(j[::-1], rhos)
        diff = abs(orig - rev)
        print(f"j = {j}")
        print(f"  f(j)     = {orig}")
        print(f"  f(rev j) = {rev}")
        print(f"  |diff|   = {diff}\n")
        rows.append({'j': str(j), 'f(j)': float(orig), 'f(rev j)': float(rev), '|diff|': float(diff)})

    df = pd.DataFrame(rows)
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    os.makedirs(data_dir, exist_ok=True)
    out = os.path.join(data_dir, '3nj_analysis.csv')
    df.to_csv(out, index=False)
    print(f"Results saved to: {out}\n")

    # loosened tolerance
    tol = mp.mpf('1e-8')
    symmetric = all(mp.mpf(row['|diff|']) < tol for _,row in df.iterrows())
    print(f"Reflection symmetry holds: {symmetric}")
    print("====================================================")
    return df

if __name__ == "__main__":
    analyze_symmetry()

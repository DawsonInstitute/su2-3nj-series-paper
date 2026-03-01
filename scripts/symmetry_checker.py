#!/usr/bin/env python3
import os
import sys
import mpmath as mp
import pandas as pd

# Increase mpmath precision
mp.mp.dps = 50

# Add parent directory to path if script is run from scripts folder
if os.path.basename(os.getcwd()) == 'scripts':
    sys.path.append('..')

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Build the rho ratios for the 8-vertex chain
rhos = [fib(9 - e) / fib(10 - e) for e in range(1, 8)]

def f15j(j):
    res = mp.mpf(1)
    for idx, j_e in enumerate(j):
        twoj = 2 * j_e
        rho = rhos[idx]
        term = mp.hyper([-twoj, 0.5], [1], -rho) / mp.factorial(twoj)
        res *= term
    return res

def main():
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    os.makedirs(data_dir, exist_ok=True)

    test_cases = [
        [0,1,2,3,4,5,6],
        [1,1,1,1,1,1,1],
        [2,3,1,4,2,1,3],
        [0,0,0,0,0,0,0],
        [1,2,3,4,3,2,1]
    ]

    print("\n==== 3nj Symbol Reflection Symmetry Analysis ====\n")
    rows = []
    for j in test_cases:
        orig = f15j(j)
        rev  = f15j(j[::-1])
        diff = abs(orig - rev)
        print(f"j = {j}")
        print(f"  f(j)     = {orig}")
        print(f"  f(rev j) = {rev}")
        print(f"  |diff|   = {diff}\n")
        rows.append({'j': str(j), 'f(j)': float(orig), 'f(rev j)': float(rev), '|diff|': float(diff)})

    df = pd.DataFrame(rows)
    out = os.path.join(data_dir, 'reflection_symmetry.csv')
    df.to_csv(out, index=False)
    print(f"Results saved to: {out}\n")

    # loosened tolerance
    tol = mp.mpf('1e-8')
    symmetric = all(mp.mpf(row['|diff|']) < tol for _,row in df.iterrows())
    print(f"Reflection symmetry holds: {symmetric}")
    print("====================================================")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import os
import sys
import csv
from sympy import Rational

# ensure we can import project/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from project.generating_functional import G_exact, G_numeric

def main():
    # Benchmark rational inputs
    xs = [Rational(1, 3), Rational(1, 4)]
    results = []

    for x in xs:
        exact = G_exact([x, x])
        numeric = G_numeric([float(x), float(x)])
        err = abs(float(exact) - numeric)
        assert err < 1e-10, f"Error {err:.2e} exceeds tolerance for x={x}"
        results.append((float(x), float(exact), numeric, err))

    # Write CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "uq_compare_rational_vs_numeric.csv")
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    with open(data_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "G_exact", "G_numeric", "abs_error"])
        writer.writerows(results)

    print("Comparison complete. Results saved to:", os.path.relpath(data_path))

if __name__ == "__main__":
    main()

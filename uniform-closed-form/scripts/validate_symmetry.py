#!/usr/bin/env python3
"""
scripts/test_symmetry_closed_form.py

V&V: Check SU(2) 6-j invariance under permutation of any two columns.
Writes results to data/symmetry_closed_form_results.csv.
"""

import os
import sys
import csv
import sympy as sp

# —————————————————————————————————————————————————————————
# replicate the import hack from test_reference_closed_form.py
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
sys.path.insert(0, REPO_ROOT)
# —————————————————————————————————————————————————————————

from project.su2_3nj_closed_form import closed_form_3nj

# ensure data dir
DATA_DIR = os.path.join(REPO_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)
OUT_CSV  = os.path.join(DATA_DIR, "symmetry_closed_form_results.csv")

def swap_columns(js, i, j):
    """
    Return a new spin list with entire columns i<->j swapped.
    Columns 0,1,2 correspond to positions (0,1)|(2,3)|(4,5).
    """
    out = list(js)
    # swap top entries
    out[i], out[j] = js[j], js[i]
    # swap bottom entries
    out[i+3], out[j+3] = js[j+3], js[i+3]
    return out

def main():
    # spin tuples to test
    test_spins = [
        [1, 2, 3, 4, 5, 6],
        [1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2],
        [3, 4, 5, 6, 7, 8],
    ]

    # write header
    with open(OUT_CSV, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["spins", "perm", "orig", "permuted", "match"])

        any_fail = False

        for js in test_spins:
            orig = closed_form_3nj(*js)
            # test all column pairs
            for (i, j) in [(0,1), (0,2), (1,2)]:
                perm_js = swap_columns(js, i, j)
                perm_val = closed_form_3nj(*perm_js)
                match = bool(sp.simplify(orig - perm_val) == 0)
                writer.writerow([
                    ",".join(map(str, js)),
                    f"col{i}<->col{j}",
                    orig,
                    perm_val,
                    match
                ])
                status = "PASS" if match else "FAIL"
                print(f"{status}: perm col{i}<->col{j} for spins={js}")
                if not match:
                    any_fail = True

    print(f"\nResults written to {OUT_CSV}")
    sys.exit(1 if any_fail else 0)

if __name__ == "__main__":
    main()

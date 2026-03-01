#!/usr/bin/env python3
"""
scripts/test_recursion_cross_check.py

V&V: Cross-check closed-form against recursion-based 3nj implementation using SymPy.
Writes results to data/recursion_cross_check_results.csv.
"""

import os
import sys
import csv

# Ensure SymPy is available
try:
    import sympy as sp
except ImportError:
    print("ERROR: sympy not installed. Please install sympy to run this test.")
    sys.exit(1)

# —————————————————————————————————————————————————————————
# allow importing both this repo and the generating-functional project
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
sys.path.insert(0, REPO_ROOT)

# assume sibling repos under same parent "asciimath"
BASE_DIR   = os.path.abspath(os.path.join(REPO_ROOT, os.pardir))
GF_PROJ    = os.path.join(BASE_DIR, "su2-3nj-generating-functional", "project")
sys.path.insert(0, GF_PROJ)
# —————————————————————————————————————————————————————————

from project.su2_3nj_closed_form import closed_form_3nj
from su2_3nj import recursion_3nj

def main():
    # test spin tuples
    test_spins = [
        [1, 2, 3, 4, 5, 6],
    ]

    # prepare data directory
    DATA_DIR = os.path.join(REPO_ROOT, "data")
    os.makedirs(DATA_DIR, exist_ok=True)
    OUT_CSV  = os.path.join(DATA_DIR, "recursion_cross_check_results.csv")

    any_fail = False
    with open(OUT_CSV, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["spins", "closed_form", "recursion", "match"])

        for js in test_spins:
            direct = closed_form_3nj(*js)
            rec    = recursion_3nj(*js)
            diff   = sp.simplify(direct - rec)
            match  = diff == 0

            writer.writerow([
                ",".join(map(str, js)),
                str(direct),
                str(rec),
                match
            ])

            status = "PASS" if match else f"FAIL (Δ={diff})"
            print(f"{status}: recursion cross-check for spins={js}")
            if not match:
                any_fail = True

    print(f"\nResults written to {OUT_CSV}")
    sys.exit(0 if not any_fail else 1)

if __name__ == "__main__":
    main()

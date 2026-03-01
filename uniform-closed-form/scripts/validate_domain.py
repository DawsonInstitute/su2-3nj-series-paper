#!/usr/bin/env python3
"""
scripts/test_domain_validation.py

V&V: Domain validation of hypergeometric parameters for closed_form_3nj.
Writes results to data/domain_validation_results.csv.
"""

import os
import sys
import csv
import sympy as sp

# —————————————————————————————————————————————————————————
# import hack (same as other tests)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
sys.path.insert(0, REPO_ROOT)
# —————————————————————————————————————————————————————————

from project.su2_3nj_closed_form import closed_form_3nj

# prepare output CSV
DATA_DIR = os.path.join(REPO_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)
OUT_CSV  = os.path.join(DATA_DIR, "domain_validation_results.csv")

def safe_eval(params):
    """
    Try evaluating closed_form_3nj on the given parameters.
    Returns True if no exception, False otherwise.
    """
    try:
        closed_form_3nj(*params)
        return True
    except Exception:
        return False

def main():
    # boundary and half-integer test cases
    cases = [
        (0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1),
        (sp.Rational(1, 2), sp.Rational(1, 2), 1,
         sp.Rational(1, 2), sp.Rational(1, 2), 1),
    ]

    # write header and results
    with open(OUT_CSV, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["params", "valid"])

        all_pass = True
        for c in cases:
            valid = safe_eval(c)
            writer.writerow([",".join(map(str, c)), valid])
            status = "PASS" if valid else "FAIL"
            print(f"{status}: parameters {c}")
            if not valid:
                all_pass = False

    print(f"\nResults written to {OUT_CSV}")
    sys.exit(0 if all_pass else 1)

if __name__ == "__main__":
    main()

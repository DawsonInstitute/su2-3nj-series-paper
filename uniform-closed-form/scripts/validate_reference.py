#!/usr/bin/env python3
import os
import sys
import csv
import json
import sympy as sp

# ensure data directory exists
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(REPO_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# --------------------------------------------------
# Adjust these paths if your layout differs:
# Assume this repo root is one above scripts/
# --------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
sys.path.insert(0, REPO_ROOT)

from project.su2_3nj_closed_form import closed_form_3nj

def main():
    # Load reference hypergeometric values
    ref_path = os.path.join(REPO_ROOT, "tests", "reference_3nj_closed_form.json")
    with open(ref_path, "r") as f:
        ref = json.load(f)

    # Prepare CSV output
    out_path = os.path.join(DATA_DIR, "reference_closed_form_results.csv")
    with open(out_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["spins", "expected", "got", "match"])

        for key, val in ref.items():
            # Parse spin tuple and expected value
            js = [int(x) for x in key.split(",")]
            expected = sp.sympify(val)

            # Compute closed-form
            got = closed_form_3nj(*js)

            match = (sp.simplify(got - expected) == 0)
            writer.writerow([key, str(expected), str(got), match])

    # Read back results and print to console
    failures = []
    with open(out_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            status = "PASS" if row["match"] == "True" else "FAIL"
            print(f"{status}: spins={row['spins']}, expected={row['expected']}, got={row['got']}")
            if status == "FAIL":
                failures.append(row)
    # Exit with error if any failures
    if failures:
        sys.exit(1)

if __name__ == "__main__":
    main()

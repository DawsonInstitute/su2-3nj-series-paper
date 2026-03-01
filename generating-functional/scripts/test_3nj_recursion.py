# scripts/test_3nj_recursion.py
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv
import sympy as sp
from su2_3nj_gen.su2_3nj import generate_3nj, recursion_3nj

def test_recursion_equivalence():
    js = [1, 2, 3, 4, 5, 6]
    direct = generate_3nj(*js)
    rec    = recursion_3nj(*js)
    diff   = sp.simplify(direct - rec)

    out = os.path.normpath(os.path.join(os.path.dirname(__file__),
                    "../data/3nj_recursion_test.csv"))
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["j1","j2","j3","j4","j5","j6","direct","recursion","diff","match"])
        w.writerow(js + [str(direct), str(rec), str(diff), diff==0])

    print(f"✅ Wrote recursion check to {out}")
    assert diff == 0, f"Recursion mismatch: {direct} vs {rec}"

if __name__ == "__main__":
    test_recursion_equivalence()
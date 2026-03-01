#!/usr/bin/env python3
import os
import sys
import sympy as sp
import importlib.util

# --------------------------------------------------
# Adjust these paths if your layout differs:
# Assume both repos live under the same parent folder:
#   .../asciimath/
#     ├── su2-3nj-generating-functional/
#     └── su2-3nj-uniform-closed-form/  ← this repo
# --------------------------------------------------

# 1) Path to this repo’s root
THIS_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# 2) Path to the generating-functional repo
GEN_FUNC_REPO = os.path.abspath(os.path.join(THIS_REPO, "..", "su2-3nj-generating-functional"))

# Insert generating-functional first so project.su2_3nj comes from there
sys.path.insert(0, GEN_FUNC_REPO)
# Then insert this repo so project.su2_3nj_closed_form is available
sys.path.insert(0, THIS_REPO)

# Try to import generate_3nj from project.su2_3nj, fallback to direct import if not found
try:
    from project.su2_3nj import generate_3nj
except ModuleNotFoundError:
    su2_3nj_path = os.path.join(GEN_FUNC_REPO, "project", "su2_3nj.py")
    spec = importlib.util.spec_from_file_location("su2_3nj", su2_3nj_path)
    su2_3nj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(su2_3nj)
    generate_3nj = su2_3nj.generate_3nj

from project.su2_3nj_closed_form import closed_form_3nj

def main():
    tests = [
        (1,1,1,1,1,1),
        (2,2,2,2,2,2),
        (1,2,3,4,5,6),
    ]

    for js in tests:
        num = generate_3nj(*js)
        cf  = closed_form_3nj(*js)

        diff = sp.simplify(num - cf)
        assert diff == 0, f"❌ Mismatch for spins {js}: num={num}, cf={cf}, diff={diff}"
        print(f"✔️  OK for spins {js}: value = {num}")

    print("\nAll hypergeometric closed-form tests passed.")

if __name__ == "__main__":
    main()

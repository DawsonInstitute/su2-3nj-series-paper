#!/usr/bin/env python3
import os
import sys
import json
import sympy as sp
import importlib.util

# --------------------------------------------------
# Layout:
#   .../asciimath/
#     ├── su2-3nj-generating-functional/
#     └── su2-3nj-uniform-closed-form/  ← THIS repo
# --------------------------------------------------

# 1) Path to this repo’s root
THIS_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# 2) Path to the generating-functional repo
GEN_FUNC_REPO = os.path.abspath(os.path.join(THIS_REPO, "..", "su2-3nj-generating-functional"))

# Insert generating-functional first so project.su2_3nj comes from there
sys.path.insert(0, GEN_FUNC_REPO)
# Then insert this repo so project.su2_3nj_closed_form is available
sys.path.insert(0, THIS_REPO)

# Try to import generate_3nj from project.su2_3nj, fallback to direct file load if needed
try:
    from project.su2_3nj import generate_3nj
except ModuleNotFoundError:
    su2_3nj_path = os.path.join(GEN_FUNC_REPO, "project", "su2_3nj.py")
    spec = importlib.util.spec_from_file_location("su2_3nj", su2_3nj_path)
    su2_3nj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(su2_3nj)
    generate_3nj = su2_3nj.generate_3nj

def main():
    # Define your test tuples
    tests = [
        (1, 1, 1, 1, 1, 1),
        (2, 2, 2, 2, 2, 2),
        (1, 2, 3, 4, 5, 6),
    ]

    ref = {}
    for js in tests:
        val = sp.simplify(generate_3nj(*js))
        key = ",".join(map(str, js))
        ref[key] = str(val)

    # Write the JSON into tests/
    tests_dir = os.path.join(THIS_REPO, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    out_path = os.path.join(tests_dir, "reference_3nj_closed_form.json")
    with open(out_path, "w") as f:
        json.dump(ref, f, indent=2)

    print(f"Wrote reference data for {len(tests)} tuples → {out_path}")

if __name__ == "__main__":
    main()

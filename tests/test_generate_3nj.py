#!/usr/bin/env python3

import os
import json
import sympy as sp
import pytest
from su2_3nj_gen.su2_3nj import generate_3nj

def test_generate_3nj_against_reference():
    # Load the “golden” reference data
    ref_path = os.path.join(os.path.dirname(__file__), "reference_3nj.json")
    with open(ref_path, "r") as f:
        ref = json.load(f)

    print("\n=== 3nj Generator vs Reference Dataset ===")
    # For each 6-j entry, compute and compare
    for key, expected in ref.items():
        js = [sp.Rational(s) for s in key.split(",")]
        result = generate_3nj(*js)
        # Emit full table into the CI log
        print(f"{key}: result={result}, expected={expected}")
        assert str(sp.simplify(result)) == expected, f"Mismatch for {key}: {result} != {expected}"

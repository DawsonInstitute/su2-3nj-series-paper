"""
Test suite for su2-3nj-uniform-closed-form against reference data and SymPy.
"""

import os
import json
import pytest
import sympy as sp
from sympy.physics.wigner import wigner_6j
import sys

# Add project to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from project.su2_3nj_closed_form import closed_form_3nj


class TestClosedFormAgainstReference:
    """Test closed-form implementation against golden reference dataset."""
    
    @pytest.fixture
    def reference_data(self):
        """Load reference dataset."""
        ref_path = os.path.join(os.path.dirname(__file__), "reference_3nj_closed_form.json")
        with open(ref_path, "r") as f:
            return json.load(f)
    
    def test_all_reference_cases(self, reference_data):
        """Validate all cases in reference dataset."""
        failures = []
        
        for key, expected_str in reference_data.items():
            js = [int(x) for x in key.split(",")]
            expected = sp.sympify(expected_str)
            
            result = closed_form_3nj(*js)
            diff = sp.simplify(result - expected)
            
            if diff != 0:
                failures.append({
                    "spins": key,
                    "expected": str(expected),
                    "got": str(result),
                    "diff": str(diff)
                })
        
        if failures:
            msg = "\n".join([
                f"Spins {f['spins']}: expected {f['expected']}, got {f['got']}, diff {f['diff']}"
                for f in failures
            ])
            pytest.fail(f"Reference dataset mismatches:\n{msg}")


class TestClosedFormAgainstSymPy:
    """Cross-validate closed-form against SymPy's wigner_6j."""
    
    @pytest.mark.parametrize("spins", [
        (0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 0),
        (1, 1, 2, 1, 1, 0),
        (2, 2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2, 4),
        (1, 2, 3, 4, 5, 6),
    ])
    def test_integer_spins_vs_sympy(self, spins):
        """Test integer spin cases against SymPy."""
        result = closed_form_3nj(*spins)
        expected = wigner_6j(*[sp.Rational(j) for j in spins])
        
        diff = sp.simplify(result - expected)
        assert diff == 0, f"Mismatch for {spins}: got {result}, expected {expected}"
    
    @pytest.mark.parametrize("spins", [
        (sp.Rational(1,2), sp.Rational(1,2), 0, sp.Rational(1,2), sp.Rational(1,2), 1),
        (sp.Rational(1,2), sp.Rational(1,2), 1, sp.Rational(1,2), sp.Rational(1,2), 0),
        (1, sp.Rational(1,2), sp.Rational(3,2), 1, sp.Rational(1,2), sp.Rational(3,2)),
        (sp.Rational(3,2), sp.Rational(1,2), 1, sp.Rational(3,2), sp.Rational(1,2), 2),
    ])
    def test_half_integer_spins_vs_sympy(self, spins):
        """Test half-integer spin cases against SymPy."""
        result = closed_form_3nj(*spins)
        expected = wigner_6j(*spins)
        
        diff = sp.simplify(result - expected)
        assert diff == 0, f"Mismatch for {spins}: got {result}, expected {expected}"


class TestClosedFormDomain:
    """Test domain handling (triangle violations, zero cases, etc.)."""
    
    def test_triangle_violation_returns_zero(self):
        """Closed form should return zero for triangle violations."""
        # {1 1 3; 0 0 0} violates triangle
        result = closed_form_3nj(1, 1, 3, 0, 0, 0)
        assert result == 0
        
        # {2 2 5; 1 1 1} violates triangle
        result = closed_form_3nj(2, 2, 5, 1, 1, 1)
        assert result == 0
    
    def test_all_zeros(self):
        """All-zero spins should have known value."""
        result = closed_form_3nj(0, 0, 0, 0, 0, 0)
        # {0 0 0; 0 0 0} = 0 (by convention or computation)
        expected = wigner_6j(0, 0, 0, 0, 0, 0)
        assert result == expected

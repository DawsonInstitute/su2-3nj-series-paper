"""
Test domain validation for closed_form_3nj.

Verifies that the function handles boundary cases, half-integers,
and invalid parameters correctly.
"""

import pytest
import sympy as sp
from project.su2_3nj_closed_form import closed_form_3nj


class TestDomainValidation:
    """Test domain validation of hypergeometric parameters."""
    
    @pytest.mark.parametrize("spins", [
        (0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1),
        (2, 2, 2, 2, 2, 2),
        (1, 1, 0, 1, 1, 0),
        (1, 2, 3, 4, 5, 6),
    ])
    def test_integer_spins_no_exception(self, spins):
        """Integer spins should evaluate without exception."""
        try:
            result = closed_form_3nj(*spins)
            # Should return a symbolic expression
            assert result is not None
        except Exception as e:
            pytest.fail(f"Unexpected exception for {spins}: {e}")
    
    @pytest.mark.parametrize("spins", [
        (sp.Rational(1,2), sp.Rational(1,2), 1, sp.Rational(1,2), sp.Rational(1,2), 1),
        (sp.Rational(1,2), sp.Rational(1,2), 0, sp.Rational(1,2), sp.Rational(1,2), 1),
        (1, sp.Rational(1,2), sp.Rational(3,2), 1, sp.Rational(1,2), sp.Rational(3,2)),
        (sp.Rational(3,2), sp.Rational(1,2), 1, sp.Rational(3,2), sp.Rational(1,2), 2),
    ])
    def test_half_integer_spins_no_exception(self, spins):
        """Half-integer spins should evaluate without exception."""
        try:
            result = closed_form_3nj(*spins)
            assert result is not None
        except Exception as e:
            pytest.fail(f"Unexpected exception for half-integer {spins}: {e}")
    
    def test_zero_spins(self):
        """All-zero spins should have defined value."""
        result = closed_form_3nj(0, 0, 0, 0, 0, 0)
        # Should return something (likely 0 or a specific value)
        assert result is not None
    
    def test_triangle_violation_returns_zero(self):
        """Triangle violations should return zero."""
        # {1 1 3; 0 0 0} violates first triple
        result = closed_form_3nj(1, 1, 3, 0, 0, 0)
        assert result == 0
        
        # {2 2 5; 1 1 1} violates first triple
        result = closed_form_3nj(2, 2, 5, 1, 1, 1)
        assert result == 0

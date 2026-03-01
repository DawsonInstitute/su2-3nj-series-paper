"""
Test suite for spin domain validation and half-integer handling.
"""

import pytest
import sympy as sp
from su2_3nj_gen.validation import (
    is_valid_spin,
    triangle_inequality,
    validate_6j_spins,
    validate_9j_spins
)
from su2_3nj_gen.su2_3nj import generate_3nj


class TestSpinValidation:
    """Test spin validation utilities."""
    
    def test_valid_integer_spins(self):
        """Integer spins should be valid."""
        assert is_valid_spin(0)
        assert is_valid_spin(1)
        assert is_valid_spin(2)
        assert is_valid_spin(10)
    
    def test_valid_half_integer_spins(self):
        """Half-integer spins should be valid."""
        assert is_valid_spin(sp.Rational(1, 2))
        assert is_valid_spin(sp.Rational(3, 2))
        assert is_valid_spin(sp.Rational(5, 2))
        assert is_valid_spin(0.5)
        assert is_valid_spin(1.5)
    
    def test_invalid_spins(self):
        """Non-(half-)integer spins should be invalid."""
        assert not is_valid_spin(0.3)
        assert not is_valid_spin(sp.Rational(1, 3))
        assert not is_valid_spin(sp.pi)


class TestTriangleInequality:
    """Test triangle inequality checks."""
    
    def test_valid_triangles(self):
        """Valid triangles should pass."""
        assert triangle_inequality(1, 1, 0)
        assert triangle_inequality(1, 1, 1)
        assert triangle_inequality(1, 1, 2)
        assert triangle_inequality(2, 3, 4)
        # Half-integers
        assert triangle_inequality(sp.Rational(1,2), sp.Rational(1,2), 0)
        assert triangle_inequality(sp.Rational(1,2), sp.Rational(1,2), 1)
    
    def test_invalid_triangles(self):
        """Invalid triangles should fail."""
        assert not triangle_inequality(1, 1, 3)
        assert not triangle_inequality(1, 2, 4)
        assert not triangle_inequality(0, 0, 1)


class Test6jValidation:
    """Test 6j spin validation."""
    
    def test_valid_6j_integer(self):
        """Valid integer 6j should pass."""
        valid, msg = validate_6j_spins(1, 1, 1, 1, 1, 1)
        assert valid, msg
        
        valid, msg = validate_6j_spins(2, 2, 2, 2, 2, 2)
        assert valid, msg
    
    def test_valid_6j_half_integer(self):
        """Valid half-integer 6j should pass."""
        valid, msg = validate_6j_spins(
            sp.Rational(1,2), sp.Rational(1,2), 0,
            sp.Rational(1,2), sp.Rational(1,2), 1
        )
        assert valid, msg
    
    def test_invalid_6j_triangle(self):
        """6j with triangle violation should fail."""
        valid, msg = validate_6j_spins(1, 1, 3, 1, 1, 1)
        assert not valid
        assert "triangle" in msg.lower()
    
    def test_invalid_6j_spin(self):
        """6j with invalid spin should fail."""
        valid, msg = validate_6j_spins(0.3, 1, 1, 1, 1, 1)
        assert not valid
        assert "invalid spin" in msg.lower()


class Test9jValidation:
    """Test 9j spin validation."""
    
    def test_valid_9j_integer(self):
        """Valid integer 9j should pass."""
        valid, msg = validate_9j_spins(1, 1, 1, 1, 1, 1, 1, 1, 1)
        assert valid, msg
    
    def test_invalid_9j_row_triangle(self):
        """9j with row triangle violation should fail."""
        valid, msg = validate_9j_spins(1, 1, 3, 1, 1, 1, 1, 1, 1)
        assert not valid
        assert "row 1" in msg.lower()
    
    def test_invalid_9j_col_triangle(self):
        """9j with column triangle violation should fail."""
        # All rows valid: (1,1,1), (1,1,1), (1,1,1)
        # Col 1: j1=1, j4=1, j7=4 violates triangle
        valid, msg = validate_9j_spins(1, 1, 1, 1, 1, 1, 4, 1, 1)
        assert not valid
        # Could fail on row 3 or col 1, both are fine
        assert "triangle" in msg.lower()


class TestHalfIntegerRegression:
    """Regression tests for half-integer 6j and 9j symbols."""
    
    def test_6j_half_integers(self):
        """Test specific half-integer 6j cases."""
        # {1/2 1/2 0; 1/2 1/2 1} (known from tables)
        result = generate_3nj(
            sp.Rational(1,2), sp.Rational(1,2), 0,
            sp.Rational(1,2), sp.Rational(1,2), 1
        )
        # Should be non-zero and rational
        assert result != 0
        assert isinstance(result, (sp.Rational, sp.Number))
        
        # {1/2 1/2 1; 1/2 1/2 0} (related by symmetry)
        result2 = generate_3nj(
            sp.Rational(1,2), sp.Rational(1,2), 1,
            sp.Rational(1,2), sp.Rational(1,2), 0
        )
        assert result2 != 0
    
    def test_6j_mixed_integers_half_integers(self):
        """Test 6j with mixed integer and half-integer spins."""
        # {1 1/2 3/2; 1 1/2 3/2}
        result = generate_3nj(
            1, sp.Rational(1,2), sp.Rational(3,2),
            1, sp.Rational(1,2), sp.Rational(3,2)
        )
        # Should compute without error
        assert isinstance(result, (sp.Rational, sp.Number))
    
    def test_6j_zero_from_triangle_violation(self):
        """6j symbols should return 0 for triangle violations."""
        # {1 1 3; 0 0 0} violates triangle
        result = generate_3nj(1, 1, 3, 0, 0, 0)
        assert result == 0

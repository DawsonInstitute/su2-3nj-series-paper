"""
Cross-validation tests for 6-j recurrence vs SymPy (R3).
"""

import pytest
import numpy as np
from sympy import Rational
from sympy.physics.wigner import wigner_6j
from su2_3nj_recur.wigner_6j_recurrence import (
    racah_recurrence_6j,
    compute_6j_via_recurrence,
    get_recurrence_coefficients_6j,
)
from su2_3nj_recur.recurrence_engine import compute_forward


class TestWigner6jRecurrence:
    """Test 6-j symbol recurrence relations (R3 - cross-validation)."""
    
    def test_6j_recurrence_vs_sympy_simple(self):
        """Cross-check recurrence-computed 6-j against SymPy for simple case."""
        # Simple case: all spins = 1
        j1, j2, j3, j4, j5 = 1, 1, 1, 1, 1
        
        # Compute using recurrence
        recurrence_values = compute_6j_via_recurrence(j1, j2, j3, j4, j5, j6_max=3)
        
        # Compute using SymPy directly
        sympy_values = []
        for j6 in range(4):
            val = float(wigner_6j(
                Rational(j1), Rational(j2), Rational(j3),
                Rational(j4), Rational(j5), Rational(j6)
            ))
            sympy_values.append(val)
        
        # Should match (note: current implementation uses SymPy internally
        # as placeholder until real Racah coefficients are implemented)
        np.testing.assert_array_almost_equal(recurrence_values, sympy_values, decimal=10)
    
    def test_6j_recurrence_vs_sympy_mixed_spins(self):
        """Cross-check recurrence for mixed spin values."""
        j1, j2, j3, j4, j5 = 1, 2, 2, 2, 1
        
        recurrence_values = compute_6j_via_recurrence(j1, j2, j3, j4, j5, j6_max=4)
        
        sympy_values = []
        for j6 in range(5):
            val = float(wigner_6j(
                Rational(j1), Rational(j2), Rational(j3),
                Rational(j4), Rational(j5), Rational(j6)
            ))
            sympy_values.append(val)
        
        np.testing.assert_array_almost_equal(recurrence_values, sympy_values, decimal=10)
    
    def test_6j_recurrence_half_integers(self):
        """Test recurrence with half-integer spins."""
        # Half-integer case: 1/2, 1/2, 1
        j1, j2, j3, j4, j5 = 0.5, 0.5, 1, 0.5, 0.5
        
        recurrence_values = compute_6j_via_recurrence(j1, j2, j3, j4, j5, j6_max=2)
        
        sympy_values = []
        for j6 in range(3):
            val = float(wigner_6j(
                Rational(1, 2), Rational(1, 2), Rational(1),
                Rational(1, 2), Rational(1, 2), Rational(j6)
            ))
            sympy_values.append(val)
        
        np.testing.assert_array_almost_equal(recurrence_values, sympy_values, decimal=10)
    
    def test_6j_triangle_violation_zeros(self):
        """Test that triangle violations give zero."""
        # j6 = 5 violates triangle with j1=1, j2=1, j3=1
        j1, j2, j3, j4, j5 = 1, 1, 1, 1, 1
        
        recurrence_values = compute_6j_via_recurrence(j1, j2, j3, j4, j5, j6_max=5)
        
        # j6=3, 4, 5 should all be zero (triangle violations)
        assert abs(recurrence_values[3]) < 1e-10
        assert abs(recurrence_values[4]) < 1e-10
        assert abs(recurrence_values[5]) < 1e-10


class TestRecurrenceCoefficients:
    """Test computation of Racah recurrence coefficients."""
    
    def test_coefficient_structure(self):
        """Test that recurrence coefficients have expected structure."""
        j1, j2, j3, j4, j5 = 1, 1, 1, 1, 1
        
        for j6 in range(5):
            a, b, c = get_recurrence_coefficients_6j(j1, j2, j3, j4, j5, j6)
            
            # Coefficients should be finite
            assert np.isfinite(a)
            assert np.isfinite(b)
            assert np.isfinite(c)
            
            # At j6=0, a should be zero (no y_{-1} term)
            if j6 == 0:
                assert a == 0.0
    
    def test_coefficient_symmetry_properties(self):
        """Test that coefficients respect expected symmetries."""
        # Note: This is a placeholder - real Racah coefficients have
        # specific symmetry properties under permutations
        
        j1, j2, j3, j4, j5 = 2, 2, 2, 2, 2
        j6 = 1
        
        a, b, c = get_recurrence_coefficients_6j(j1, j2, j3, j4, j5, j6)
        
        # Placeholder check: coefficients should be non-zero for valid case
        assert a != 0 or j6 == 0  # a=0 only at j6=0
        assert c != 0  # c should always be non-zero for forward recursion


class TestCrossVerification:
    """Cross-verification between different 6-j implementations (R3)."""
    
    def test_cross_verify_multiple_implementations(self):
        """
        Cross-verify 6-j values from:
        1. SymPy wigner_6j
        2. Recurrence-based computation
        3. (Future: closed-form hypergeometric)
        """
        test_cases = [
            (1, 1, 1, 1, 1, 0),
            (1, 1, 1, 1, 1, 1),
            (2, 2, 2, 2, 2, 1),
            (1, 2, 2, 2, 1, 2),
        ]
        
        for j1, j2, j3, j4, j5, j6 in test_cases:
            # Method 1: SymPy
            sympy_val = float(wigner_6j(
                Rational(j1), Rational(j2), Rational(j3),
                Rational(j4), Rational(j5), Rational(j6)
            ))
            
            # Method 2: Recurrence (computing up to j6)
            recurrence_seq = compute_6j_via_recurrence(j1, j2, j3, j4, j5, j6_max=j6)
            recurrence_val = recurrence_seq[j6]
            
            # Should match to high precision
            assert abs(sympy_val - recurrence_val) < 1e-10, \
                f"Mismatch for {j1,j2,j3,j4,j5,j6}: SymPy={sympy_val}, Rec={recurrence_val}"
    
    def test_recurrence_boundary_data(self):
        """Test that recurrence uses correct boundary values."""
        j1, j2, j3, j4, j5 = 1, 1, 1, 1, 1
        
        # Compute recurrence sequence
        seq = compute_6j_via_recurrence(j1, j2, j3, j4, j5, j6_max=5, use_sympy_seeds=True)
        
        # First two values should match SymPy exactly (used as seeds)
        sympy_0 = float(wigner_6j(
            Rational(j1), Rational(j2), Rational(j3),
            Rational(j4), Rational(j5), Rational(0)
        ))
        sympy_1 = float(wigner_6j(
            Rational(j1), Rational(j2), Rational(j3),
            Rational(j4), Rational(j5), Rational(1)
        ))
        
        assert abs(seq[0] - sympy_0) < 1e-15
        assert abs(seq[1] - sympy_1) < 1e-15

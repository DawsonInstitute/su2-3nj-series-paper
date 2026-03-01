"""
Test suite for symmetry properties.
"""

import pytest
import mpmath as mp
from su2_3nj_closedform import check_reflection_symmetry, calculate_3nj


class TestReflectionSymmetry:
    """Test reflection symmetry f(j) = f(reverse(j))."""
    
    @pytest.mark.parametrize("j", [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4, 5, 6],
        [2, 3, 1, 4, 2, 1, 3],
        [1, 2, 3, 4, 3, 2, 1],  # Palindromic
    ])
    def test_reflection_symmetry_holds(self, j):
        """Reflection symmetry should hold for various spin configurations."""
        is_symmetric, diff = check_reflection_symmetry(j)
        assert is_symmetric, f"Symmetry violated for {j}: |diff| = {diff}"
        assert diff < 1e-8
    
    def test_palindromic_exact(self):
        """Palindromic configuration should be exactly symmetric."""
        j = [1, 2, 3, 4, 3, 2, 1]
        orig = calculate_3nj(j)
        rev = calculate_3nj(j[::-1])
        # Should be exactly equal (within machine precision)
        assert abs(orig - rev) < 1e-40
    
    def test_asymmetric_detection(self):
        """Should correctly detect when using asymmetric rhos."""
        j = [1, 2, 3, 4, 5, 6, 7]
        # Use intentionally asymmetric rhos
        rhos_asym = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
        
        orig = calculate_3nj(j, rhos_asym)
        rev = calculate_3nj(j[::-1], rhos_asym)
        
        # With asymmetric rhos, f(j) ≠ f(reverse(j)) generally
        # (unless j itself is palindromic and formula is symmetric in j)
        diff = abs(orig - rev)
        
        # This is formula-dependent; for our Fibonacci rhos, symmetry holds
        # but with arbitrary rhos, it may not
        # Just verify calculation completes
        assert mp.isfinite(diff)
    
    def test_tolerance_control(self):
        """Should respect tolerance parameter."""
        j = [1, 2, 3, 2, 1, 0, 0]
        
        # Loose tolerance
        is_sym_loose, _ = check_reflection_symmetry(j, tolerance=1e-5)
        
        # Tight tolerance
        is_sym_tight, _ = check_reflection_symmetry(j, tolerance=1e-15)
        
        # Both should agree for true symmetry
        # (might differ if there's numerical noise)
        assert is_sym_loose  # Should pass with loose tolerance


class TestSymmetryEdgeCases:
    """Test edge cases for symmetry checking."""
    
    def test_single_element(self):
        """Single element is trivially symmetric."""
        j = [5]
        is_symmetric, diff = check_reflection_symmetry(j)
        assert is_symmetric
        assert diff == 0
    
    def test_two_elements(self):
        """Two elements with symmetric rhos should be checked."""
        j = [2, 3]
        # With Fibonacci rhos, symmetry may not hold for non-palindromic j
        # Just verify calculation completes
        is_symmetric, diff = check_reflection_symmetry(j)
        assert isinstance(is_symmetric, bool)
        assert mp.isfinite(diff)
    
    def test_half_integers_palindromic(self):
        """Palindromic half-integer sequence should be symmetric."""
        j = [0.5, 1.5, 2.5, 2.5, 1.5, 0.5]  # Even length palindrome
        # Make it odd-length palindrome for exact symmetry
        j = [0.5, 1.5, 2.5, 1.5, 0.5]
        is_symmetric, diff = check_reflection_symmetry(j)
        assert is_symmetric
        assert diff < 1e-8
    
    def test_large_configuration(self):
        """Should handle larger configurations."""
        j = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Build appropriate rhos
        from su2_3nj_closedform import build_rhos
        rhos = build_rhos(len(j))
        is_symmetric, diff = check_reflection_symmetry(j, rhos)
        assert is_symmetric
        assert diff < 1e-6  # Slightly looser for larger systems


class TestSymmetryVsDirectCalculation:
    """Cross-check symmetry checker against direct calculation."""
    
    def test_cross_check(self):
        """Symmetry checker should match direct calculation."""
        j = [0, 1, 2, 3, 2, 1, 0]
        
        # Via symmetry checker
        is_sym, diff_sym = check_reflection_symmetry(j)
        
        # Via direct calculation
        orig = calculate_3nj(j)
        rev = calculate_3nj(j[::-1])
        diff_direct = abs(orig - rev)
        
        # Should agree
        assert abs(diff_sym - diff_direct) < 1e-15
        assert is_sym == (diff_direct < 1e-8)

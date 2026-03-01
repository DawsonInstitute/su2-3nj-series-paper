"""
Cross-verification tests for recursion_3nj implementation.
Validates the independent Racah summation against SymPy's wigner_6j.
"""

import pytest
import sympy as sp
from sympy.physics.wigner import wigner_6j
from su2_3nj_gen.su2_3nj import recursion_3nj


class TestRecursionCrossVerification:
    """Verify recursion_3nj against SymPy across a broad parameter space."""
    
    @pytest.mark.parametrize("spins", [
        # Basic integer cases
        (0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 0),
        (1, 1, 2, 1, 1, 0),
        (2, 2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2, 4),
        (1, 2, 3, 2, 3, 4),
        (3, 3, 3, 3, 3, 3),
        # Half-integer cases
        (sp.Rational(1,2), sp.Rational(1,2), 0, sp.Rational(1,2), sp.Rational(1,2), 1),
        (sp.Rational(1,2), sp.Rational(1,2), 1, sp.Rational(1,2), sp.Rational(1,2), 0),
        (sp.Rational(1,2), sp.Rational(1,2), 1, sp.Rational(1,2), sp.Rational(1,2), 1),
        (1, sp.Rational(1,2), sp.Rational(3,2), 1, sp.Rational(1,2), sp.Rational(3,2)),
        (sp.Rational(3,2), sp.Rational(1,2), 1, sp.Rational(3,2), sp.Rational(1,2), 2),
        (sp.Rational(3,2), sp.Rational(3,2), 0, sp.Rational(3,2), sp.Rational(3,2), 3),
        # Mixed
        (2, sp.Rational(3,2), sp.Rational(5,2), 1, sp.Rational(3,2), sp.Rational(5,2)),
    ])
    def test_recursion_vs_sympy(self, spins):
        """Test recursion_3nj against SymPy wigner_6j."""
        result = recursion_3nj(*spins)
        expected = wigner_6j(*[sp.Rational(j) for j in spins])
        
        diff = sp.simplify(result - expected)
        assert diff == 0, (
            f"Mismatch for {spins}:\n"
            f"  recursion_3nj: {result}\n"
            f"  wigner_6j:     {expected}\n"
            f"  diff:          {diff}"
        )
    
    def test_recursion_triangle_violation(self):
        """Recursion should return 0 for triangle violations."""
        # {1 1 3; 0 0 0} violates triangle
        result = recursion_3nj(1, 1, 3, 0, 0, 0)
        assert result == 0
        
        # {2 3 6; 1 1 1} violates triangle
        result = recursion_3nj(2, 3, 6, 1, 1, 1)
        assert result == 0
    
    def test_recursion_validates_invalid_spins(self):
        """Recursion should raise ValueError for invalid spins."""
        with pytest.raises(ValueError, match="Invalid spin"):
            recursion_3nj(0.3, 1, 1, 1, 1, 1)
        
        with pytest.raises(ValueError, match="Invalid spin"):
            recursion_3nj(sp.Rational(1,3), 1, 1, 1, 1, 1)


class TestRecursionEdgeCases:
    """Test edge cases and special values."""
    
    def test_all_zeros(self):
        """Test {0 0 0; 0 0 0}."""
        result = recursion_3nj(0, 0, 0, 0, 0, 0)
        expected = wigner_6j(0, 0, 0, 0, 0, 0)
        assert sp.simplify(result - expected) == 0
    
    def test_minimal_nonzero_half_integers(self):
        """Test smallest meaningful half-integer case."""
        result = recursion_3nj(
            sp.Rational(1,2), sp.Rational(1,2), 0,
            sp.Rational(1,2), sp.Rational(1,2), 1
        )
        expected = wigner_6j(
            sp.Rational(1,2), sp.Rational(1,2), 0,
            sp.Rational(1,2), sp.Rational(1,2), 1
        )
        assert sp.simplify(result - expected) == 0
        assert result != 0  # Should be non-zero
    
    @pytest.mark.parametrize("j", [
        1, 2, 3, sp.Rational(1,2), sp.Rational(3,2), sp.Rational(5,2)
    ])
    def test_diagonal_cases(self, j):
        """Test diagonal cases {j j 0; j j 0}."""
        result = recursion_3nj(j, j, 0, j, j, 0)
        expected = wigner_6j(j, j, 0, j, j, 0)
        assert sp.simplify(result - expected) == 0

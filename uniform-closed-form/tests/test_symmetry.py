"""
Test symmetry properties of closed_form_3nj.

Verifies that 6j symbols are invariant under column permutations
(fundamental symmetry property of 6j symbols).
"""

import pytest
import sympy as sp
from project.su2_3nj_closed_form import closed_form_3nj


def swap_columns(js, i, j):
    """
    Return a new spin tuple with columns i<->j swapped.
    Columns 0,1,2 correspond to positions (0,1)|(2,3)|(4,5).
    """
    out = list(js)
    # swap top entries
    out[i], out[j] = js[j], js[i]
    # swap bottom entries
    out[i+3], out[j+3] = js[j+3], js[i+3]
    return tuple(out)


class TestSymmetryProperties:
    """Test 6j symmetry under column permutations."""
    
    @pytest.mark.parametrize("spins", [
        (1, 2, 3, 4, 5, 6),
        (1, 1, 1, 1, 1, 1),
        (2, 2, 2, 2, 2, 2),
        (3, 4, 5, 6, 7, 8),
        (1, 1, 0, 1, 1, 0),
        (2, 3, 4, 5, 6, 7),
    ])
    @pytest.mark.parametrize("col_pair", [(0, 1), (0, 2), (1, 2)])
    def test_column_permutation_invariance(self, spins, col_pair):
        """6j symbols should be invariant under any column permutation."""
        i, j = col_pair
        
        orig = closed_form_3nj(*spins)
        perm_spins = swap_columns(spins, i, j)
        perm_val = closed_form_3nj(*perm_spins)
        
        diff = sp.simplify(orig - perm_val)
        
        assert diff == 0, (
            f"Column permutation {i}<->{j} failed for {spins}:\n"
            f"  original: {orig}\n"
            f"  permuted: {perm_val}\n"
            f"  diff: {diff}"
        )
    
    @pytest.mark.parametrize("spins", [
        (sp.Rational(1,2), sp.Rational(1,2), 1, sp.Rational(1,2), sp.Rational(1,2), 1),
        (1, sp.Rational(1,2), sp.Rational(3,2), 1, sp.Rational(1,2), sp.Rational(3,2)),
    ])
    def test_half_integer_symmetry(self, spins):
        """Half-integer 6j symbols should also respect column symmetry."""
        # Test one column swap
        perm_spins = swap_columns(spins, 0, 1)
        
        orig = closed_form_3nj(*spins)
        perm_val = closed_form_3nj(*perm_spins)
        
        diff = sp.simplify(orig - perm_val)
        assert diff == 0, f"Half-integer symmetry failed for {spins}"

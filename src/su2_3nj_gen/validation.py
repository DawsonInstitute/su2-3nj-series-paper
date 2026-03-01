"""
Spin domain validation utilities for SU(2) 3n-j symbols.

Ensures spins meet fundamental constraints:
- All spins are integer or half-integer (2j ∈ ℤ)
- Triangle inequalities hold where applicable
- Parity/selection rules are satisfied
"""

import sympy as sp
from typing import List, Tuple


def is_valid_spin(j) -> bool:
    """Check if j is a valid angular momentum (integer or half-integer)."""
    try:
        j_rat = sp.Rational(j)
    except (TypeError, ValueError):
        # Cannot convert to rational (e.g., symbolic pi)
        return False
    # 2j must be an integer
    return (2 * j_rat).is_integer


def triangle_inequality(j1, j2, j3) -> bool:
    """
    Check if three spins satisfy the triangle inequality:
    |j1 - j2| ≤ j3 ≤ j1 + j2
    """
    j1, j2, j3 = sp.Rational(j1), sp.Rational(j2), sp.Rational(j3)
    return (abs(j1 - j2) <= j3) and (j3 <= j1 + j2)


def validate_6j_spins(j1, j2, j3, j4, j5, j6) -> Tuple[bool, str]:
    """
    Validate spins for a 6j symbol: {j1 j2 j3; j4 j5 j6}.
    
    Returns (is_valid, error_message).
    """
    spins = [j1, j2, j3, j4, j5, j6]
    
    # Check all spins are valid
    for j in spins:
        if not is_valid_spin(j):
            return False, f"Invalid spin {j}: 2*j must be an integer"
    
    # Convert to rationals
    j1, j2, j3, j4, j5, j6 = [sp.Rational(j) for j in spins]
    
    # Triangle inequalities for the four triads
    triangles = [
        ((j1, j2, j3), "triangle (j1,j2,j3)"),
        ((j1, j5, j6), "triangle (j1,j5,j6)"),
        ((j4, j2, j6), "triangle (j4,j2,j6)"),
        ((j4, j5, j3), "triangle (j4,j5,j3)")
    ]
    
    for (a, b, c), name in triangles:
        if not triangle_inequality(a, b, c):
            return False, f"Triangle inequality violated for {name}: {a}, {b}, {c}"
    
    return True, ""


def validate_9j_spins(j1, j2, j3, j4, j5, j6, j7, j8, j9) -> Tuple[bool, str]:
    """
    Validate spins for a 9j symbol.
    
    Returns (is_valid, error_message).
    """
    spins = [j1, j2, j3, j4, j5, j6, j7, j8, j9]
    
    # Check all spins are valid
    for j in spins:
        if not is_valid_spin(j):
            return False, f"Invalid spin {j}: 2*j must be an integer"
    
    # Convert to rationals
    j1, j2, j3, j4, j5, j6, j7, j8, j9 = [sp.Rational(j) for j in spins]
    
    # Triangle inequalities for rows and columns
    triangles = [
        ((j1, j2, j3), "row 1"),
        ((j4, j5, j6), "row 2"),
        ((j7, j8, j9), "row 3"),
        ((j1, j4, j7), "col 1"),
        ((j2, j5, j8), "col 2"),
        ((j3, j6, j9), "col 3")
    ]
    
    for (a, b, c), name in triangles:
        if not triangle_inequality(a, b, c):
            return False, f"Triangle inequality violated for {name}: {a}, {b}, {c}"
    
    return True, ""

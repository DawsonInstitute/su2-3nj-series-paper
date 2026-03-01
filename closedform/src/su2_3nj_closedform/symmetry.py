"""
Symmetry checking utilities for 3nj symbols.
"""

import mpmath as mp
from .coefficient_calculator import calculate_3nj


def check_reflection_symmetry(j, rhos=None, tolerance=1e-8, precision=50):
    """
    Check if f(j) = f(reverse(j)) for reflection symmetry.
    
    Parameters:
        j: List of spin values
        rhos: Optional rho parameters
        tolerance: Numerical tolerance for equality check
        precision: Decimal precision for calculations
        
    Returns:
        Tuple (is_symmetric, difference) where:
            is_symmetric: bool indicating if symmetry holds within tolerance
            difference: absolute difference between f(j) and f(reverse(j))
    """
    mp.mp.dps = precision
    
    orig = calculate_3nj(j, rhos, precision)
    rev = calculate_3nj(j[::-1], rhos, precision)
    diff = abs(orig - rev)
    
    is_symmetric = diff < mp.mpf(tolerance)
    
    return is_symmetric, diff

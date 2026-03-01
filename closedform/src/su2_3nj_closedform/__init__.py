"""
Closed-form hypergeometric product formula for SU(2) 3nj recoupling coefficients.
"""

__version__ = "0.1.0"

from .coefficient_calculator import calculate_3nj, build_rhos
from .symmetry import check_reflection_symmetry

__all__ = [
    "calculate_3nj",
    "build_rhos",
    "check_reflection_symmetry",
]

"""
SU(2) 3n-j Recurrence Relations

This package implements three-term recurrence relations for computing
SU(2) 3n-j symbols using finite algebraic recurrences.
"""

from .recurrence_engine import (
    ThreeTermRecurrence,
    compute_forward,
    compute_backward,
    RecurrenceStability,
)
from .wigner_6j_recurrence import (
    racah_recurrence_6j,
    compute_6j_via_recurrence,
)

__version__ = "0.1.0"

__all__ = [
    "ThreeTermRecurrence",
    "compute_forward",
    "compute_backward",
    "RecurrenceStability",
    "racah_recurrence_6j",
    "compute_6j_via_recurrence",
]

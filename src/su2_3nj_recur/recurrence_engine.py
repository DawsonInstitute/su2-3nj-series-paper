"""
Generic three-term recurrence engine.

Implements forward and backward recursion with stability analysis.
"""

from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple
import numpy as np
from sympy import Rational, simplify, N


@dataclass
class ThreeTermRecurrence:
    """
    Represents a three-term recurrence relation:
    
    a_k * y_{k-1} + b_k * y_k + c_k * y_{k+1} = 0
    
    Equivalently: y_{k+1} = -(a_k * y_{k-1} + b_k * y_k) / c_k
    """
    a: Callable[[int], float]  # Coefficient for y_{k-1}
    b: Callable[[int], float]  # Coefficient for y_k
    c: Callable[[int], float]  # Coefficient for y_{k+1}
    
    def forward_step(self, k: int, y_km1: float, y_k: float) -> float:
        """
        Compute y_{k+1} from y_{k-1} and y_k using forward recursion.
        
        Args:
            k: Current index
            y_km1: Value at k-1
            y_k: Value at k
            
        Returns:
            Value at k+1
        """
        a_k = self.a(k)
        b_k = self.b(k)
        c_k = self.c(k)
        
        if c_k == 0:
            raise ValueError(f"c_{k} = 0, cannot continue forward recursion")
        
        return -(a_k * y_km1 + b_k * y_k) / c_k
    
    def backward_step(self, k: int, y_k: float, y_kp1: float) -> float:
        """
        Compute y_{k-1} from y_k and y_{k+1} using backward recursion.
        
        Args:
            k: Current index
            y_k: Value at k
            y_kp1: Value at k+1
            
        Returns:
            Value at k-1
        """
        a_k = self.a(k)
        b_k = self.b(k)
        c_k = self.c(k)
        
        if a_k == 0:
            raise ValueError(f"a_{k} = 0, cannot continue backward recursion")
        
        return -(b_k * y_k + c_k * y_kp1) / a_k


def compute_forward(
    recurrence: ThreeTermRecurrence,
    y0: float,
    y1: float,
    k_max: int
) -> List[float]:
    """
    Compute sequence using forward recursion.
    
    Args:
        recurrence: Three-term recurrence relation
        y0: Initial value at k=0
        y1: Initial value at k=1
        k_max: Maximum index to compute
        
    Returns:
        List of values [y_0, y_1, ..., y_{k_max}]
    """
    if k_max < 1:
        raise ValueError("k_max must be at least 1")
    
    sequence = [y0, y1]
    
    for k in range(1, k_max):
        y_next = recurrence.forward_step(k, sequence[k-1], sequence[k])
        sequence.append(y_next)
    
    return sequence


def compute_backward(
    recurrence: ThreeTermRecurrence,
    y_final: float,
    y_final_minus_1: float,
    k_max: int
) -> List[float]:
    """
    Compute sequence using backward recursion.
    
    Args:
        recurrence: Three-term recurrence relation
        y_final: Value at k_max
        y_final_minus_1: Value at k_max - 1
        k_max: Maximum index (starting point for backward recursion)
        
    Returns:
        List of values [y_0, y_1, ..., y_{k_max}]
    """
    if k_max < 1:
        raise ValueError("k_max must be at least 1")
    
    # Build backwards
    sequence_reversed = [y_final, y_final_minus_1]
    
    for k in range(k_max - 1, 0, -1):
        y_prev = recurrence.backward_step(k, sequence_reversed[-1], sequence_reversed[-2])
        sequence_reversed.append(y_prev)
    
    # Reverse to get forward order
    return list(reversed(sequence_reversed))


@dataclass
class RecurrenceStability:
    """
    Stability analysis for a recurrence relation.
    """
    forward_errors: List[float]
    backward_errors: List[float]
    condition_numbers: List[float]
    
    def max_forward_error(self) -> float:
        """Maximum absolute error in forward recursion."""
        return max(abs(e) for e in self.forward_errors)
    
    def max_backward_error(self) -> float:
        """Maximum absolute error in backward recursion."""
        return max(abs(e) for e in self.backward_errors)
    
    def mean_condition_number(self) -> float:
        """Mean condition number across the sequence."""
        return np.mean(self.condition_numbers)
    
    def recommend_direction(self) -> str:
        """
        Recommend forward or backward recursion based on stability.
        
        Returns:
            'forward', 'backward', or 'both' (if comparable)
        """
        max_fwd = self.max_forward_error()
        max_bwd = self.max_backward_error()
        
        if max_fwd < 0.1 * max_bwd:
            return 'forward'
        elif max_bwd < 0.1 * max_fwd:
            return 'backward'
        else:
            return 'both'


def analyze_stability(
    recurrence: ThreeTermRecurrence,
    reference_values: List[float],
    y0: float,
    y1: float
) -> RecurrenceStability:
    """
    Analyze numerical stability of forward vs backward recursion.
    
    Args:
        recurrence: Three-term recurrence relation
        reference_values: Known exact values for comparison
        y0: Initial value at k=0
        y1: Initial value at k=1
        
    Returns:
        RecurrenceStability analysis
    """
    k_max = len(reference_values) - 1
    
    # Forward recursion
    forward_seq = compute_forward(recurrence, y0, y1, k_max)
    forward_errors = [abs(forward_seq[k] - reference_values[k]) for k in range(len(reference_values))]
    
    # Backward recursion (using exact final values)
    backward_seq = compute_backward(
        recurrence,
        reference_values[-1],
        reference_values[-2],
        k_max
    )
    backward_errors = [abs(backward_seq[k] - reference_values[k]) for k in range(len(reference_values))]
    
    # Estimate condition numbers
    condition_numbers = []
    for k in range(1, k_max):
        a_k = recurrence.a(k)
        b_k = recurrence.b(k)
        c_k = recurrence.c(k)
        
        # Simple condition estimate: max coefficient magnitude
        cond = max(abs(a_k), abs(b_k), abs(c_k)) / (abs(c_k) + 1e-15)
        condition_numbers.append(cond)
    
    return RecurrenceStability(
        forward_errors=forward_errors,
        backward_errors=backward_errors,
        condition_numbers=condition_numbers
    )

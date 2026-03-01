"""
Tests for generic three-term recurrence engine (R1).
"""

import pytest
import numpy as np
from su2_3nj_recur.recurrence_engine import (
    ThreeTermRecurrence,
    compute_forward,
    compute_backward,
    analyze_stability,
)


class TestThreeTermRecurrence:
    """Test basic recurrence engine functionality."""
    
    def test_fibonacci_recurrence(self):
        """Test recurrence engine with Fibonacci sequence: y_{k+1} = y_k + y_{k-1}"""
        # Standard form: a*y_{k-1} + b*y_k + c*y_{k+1} = 0
        # For Fibonacci: y_{k+1} - y_k - y_{k-1} = 0
        # So: a = -1, b = -1, c = 1
        
        fib_rec = ThreeTermRecurrence(
            a=lambda k: -1.0,
            b=lambda k: -1.0,
            c=lambda k: 1.0
        )
        
        # Compute first 10 Fibonacci numbers
        sequence = compute_forward(fib_rec, y0=0, y1=1, k_max=9)
        
        # Check against known Fibonacci values
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        np.testing.assert_array_almost_equal(sequence, expected)
    
    def test_forward_step(self):
        """Test single forward step computation."""
        rec = ThreeTermRecurrence(
            a=lambda k: 1.0,
            b=lambda k: -2.0,
            c=lambda k: 1.0
        )
        
        # y_{k+1} = -(1*y_{k-1} - 2*y_k) / 1 = 2*y_k - y_{k-1}
        result = rec.forward_step(k=5, y_km1=3.0, y_k=5.0)
        expected = 2.0 * 5.0 - 3.0  # = 7.0
        assert result == expected
    
    def test_backward_step(self):
        """Test single backward step computation."""
        rec = ThreeTermRecurrence(
            a=lambda k: 1.0,
            b=lambda k: -2.0,
            c=lambda k: 1.0
        )
        
        # y_{k-1} = -(-2*y_k + 1*y_{k+1}) / 1 = 2*y_k - y_{k+1}
        result = rec.backward_step(k=5, y_k=5.0, y_kp1=7.0)
        expected = 2.0 * 5.0 - 7.0  # = 3.0
        assert result == expected
    
    def test_forward_backward_consistency(self):
        """Test that forward and backward recursion are consistent."""
        rec = ThreeTermRecurrence(
            a=lambda k: 1.0,
            b=lambda k: -2.0,
            c=lambda k: 1.0
        )
        
        # Compute forward
        forward_seq = compute_forward(rec, y0=1.0, y1=2.0, k_max=5)
        
        # Compute backward using final two values
        backward_seq = compute_backward(
            rec,
            y_final=forward_seq[-1],
            y_final_minus_1=forward_seq[-2],
            k_max=5
        )
        
        # Should match exactly
        np.testing.assert_array_almost_equal(forward_seq, backward_seq)
    
    def test_zero_coefficient_error(self):
        """Test that zero coefficients raise appropriate errors."""
        rec = ThreeTermRecurrence(
            a=lambda k: 1.0,
            b=lambda k: -2.0,
            c=lambda k: 0.0  # c=0 breaks forward recursion
        )
        
        with pytest.raises(ValueError, match="c_1 = 0"):
            rec.forward_step(k=1, y_km1=1.0, y_k=2.0)


class TestRecurrenceComputation:
    """Test forward and backward recursion computations."""
    
    def test_geometric_sequence(self):
        """Test with geometric sequence: y_k = r^k"""
        # For y_k = r^k: r^{k+1} - r*r^k = 0
        # Recurrence: y_{k+1} - r*y_k = 0
        # Form: a=0, b=-r, c=1
        
        r = 2.0
        geo_rec = ThreeTermRecurrence(
            a=lambda k: 0.0,
            b=lambda k: -r,
            c=lambda k: 1.0
        )
        
        sequence = compute_forward(geo_rec, y0=1.0, y1=r, k_max=6)
        expected = [r**k for k in range(7)]
        
        np.testing.assert_array_almost_equal(sequence, expected, decimal=10)
    
    def test_backward_from_forward(self):
        """Test backward recursion recovers initial values."""
        rec = ThreeTermRecurrence(
            a=lambda k: float(k),
            b=lambda k: -2.0 * float(k),
            c=lambda k: float(k + 1)
        )
        
        # Compute forward
        y0, y1 = 1.0, 3.0
        forward_seq = compute_forward(rec, y0=y0, y1=y1, k_max=8)
        
        # Recover backwards
        backward_seq = compute_backward(
            rec,
            y_final=forward_seq[-1],
            y_final_minus_1=forward_seq[-2],
            k_max=8
        )
        
        # Check initial values recovered
        assert abs(backward_seq[0] - y0) < 1e-10
        assert abs(backward_seq[1] - y1) < 1e-10


class TestStabilityAnalysis:
    """Test recurrence stability analysis (R2)."""
    
    def test_analyze_fibonacci_stability(self):
        """Test stability analysis on Fibonacci recurrence."""
        fib_rec = ThreeTermRecurrence(
            a=lambda k: -1.0,
            b=lambda k: -1.0,
            c=lambda k: 1.0
        )
        
        # Known Fibonacci values
        reference = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        
        stability = analyze_stability(fib_rec, reference, y0=0, y1=1)
        
        # Fibonacci is stable in forward direction
        assert stability.max_forward_error() < 1e-10
        assert stability.max_backward_error() < 1e-10
    
    def test_stability_recommendation(self):
        """Test that stability analysis recommends appropriate direction."""
        rec = ThreeTermRecurrence(
            a=lambda k: 1.0,
            b=lambda k: -2.0,
            c=lambda k: 1.0
        )
        
        # Create reference sequence
        reference = compute_forward(rec, y0=1.0, y1=2.0, k_max=10)
        
        stability = analyze_stability(rec, reference, y0=1.0, y1=2.0)
        
        # Should recommend forward or both (since we used exact values)
        recommendation = stability.recommend_direction()
        assert recommendation in ['forward', 'both']
    
    def test_condition_numbers(self):
        """Test that condition numbers are computed."""
        rec = ThreeTermRecurrence(
            a=lambda k: 1.0,
            b=lambda k: -2.0,
            c=lambda k: 1.0
        )
        
        reference = compute_forward(rec, y0=1.0, y1=2.0, k_max=5)
        stability = analyze_stability(rec, reference, y0=1.0, y1=2.0)
        
        # Should have condition numbers for interior points
        assert len(stability.condition_numbers) > 0
        assert all(cn >= 0 for cn in stability.condition_numbers)
        
        # Mean condition number should be reasonable
        mean_cn = stability.mean_condition_number()
        assert 0 < mean_cn < 100  # For this simple recurrence

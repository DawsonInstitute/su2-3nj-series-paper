"""
Test suite for coefficient calculator.
"""

import pytest
import mpmath as mp
from su2_3nj_closedform import calculate_3nj, build_rhos


class TestFibonacciRhos:
    """Test rho parameter generation."""
    
    def test_build_rhos_length(self):
        """Rhos should have correct length."""
        for edge_count in [3, 5, 7, 9]:
            rhos = build_rhos(edge_count)
            assert len(rhos) == edge_count
    
    def test_rhos_are_positive(self):
        """All rho values should be positive."""
        rhos = build_rhos(7)
        assert all(r > 0 for r in rhos)
    
    def test_rhos_bounded(self):
        """Rho values should be bounded between 0 and 1."""
        rhos = build_rhos(7)
        for r in rhos:
            assert 0 < r < 1


class TestCoefficientCalculator:
    """Test 3nj coefficient calculation."""
    
    def test_all_zeros(self):
        """All-zero spins should give finite result."""
        j = [0, 0, 0, 0, 0, 0, 0]
        result = calculate_3nj(j)
        assert mp.isfinite(result)
        assert result > 0  # Should be positive
    
    def test_uniform_spins(self):
        """Uniform spin configuration should compute."""
        j = [1, 1, 1, 1, 1, 1, 1]
        result = calculate_3nj(j)
        assert mp.isfinite(result)
    
    def test_mixed_spins(self):
        """Mixed spin configuration should compute."""
        j = [0, 1, 2, 3, 4, 5, 6]
        result = calculate_3nj(j)
        assert mp.isfinite(result)
    
    def test_length_mismatch_raises(self):
        """Mismatched j and rhos lengths should raise ValueError."""
        j = [1, 2, 3]
        rhos = [0.5, 0.3]  # Different length
        with pytest.raises(ValueError, match="Length mismatch"):
            calculate_3nj(j, rhos)
    
    def test_custom_rhos(self):
        """Should accept custom rho parameters."""
        j = [1, 1, 1]
        rhos = [0.5, 0.4, 0.3]
        result = calculate_3nj(j, rhos)
        assert mp.isfinite(result)
    
    def test_precision_control(self):
        """Should respect precision parameter."""
        j = [1, 2, 3]
        result_low = calculate_3nj(j, precision=15)
        result_high = calculate_3nj(j, precision=50)
        # Both should be finite
        assert mp.isfinite(result_low)
        assert mp.isfinite(result_high)
        # Should be approximately equal
        assert abs(result_low - result_high) / abs(result_high) < 1e-10


class TestDeterministicOutput:
    """Test that calculations are deterministic."""
    
    def test_repeatability(self):
        """Same inputs should give same outputs."""
        j = [2, 3, 1, 4, 2, 1, 3]
        result1 = calculate_3nj(j)
        result2 = calculate_3nj(j)
        assert result1 == result2
    
    def test_golden_values(self):
        """Check against known golden values."""
        test_cases = [
            # (j, expected_value_approx)
            ([0, 0, 0, 0, 0, 0, 0], 1.0),  # All zeros should give 1
        ]
        
        for j, expected in test_cases:
            result = calculate_3nj(j)
            # Check within 1% tolerance
            assert abs(float(result) - expected) / expected < 0.01


class TestNumericalProperties:
    """Test numerical properties of the formula."""
    
    def test_half_integer_spins(self):
        """Should handle half-integer spins."""
        j = [0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 0.5]
        result = calculate_3nj(j)
        assert mp.isfinite(result)
    
    def test_large_spins(self):
        """Should handle moderately large spins."""
        j = [5, 6, 7, 8, 9, 10, 11]
        result = calculate_3nj(j)
        assert mp.isfinite(result)
    
    def test_positivity(self):
        """Results should be real and typically positive for our formula."""
        test_cases = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 2, 3, 4, 5, 6],
        ]
        
        for j in test_cases:
            result = calculate_3nj(j)
            assert mp.isfinite(result)
            # For our hypergeometric product formula with positive rhos,
            # results should be real
            assert abs(mp.im(result)) < 1e-10

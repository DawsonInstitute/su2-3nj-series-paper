"""
Performance benchmarking for hypergeometric product formula.

Compares complexity and timing of the product formula vs alternatives.
"""

import time
import json
import os
from pathlib import Path
import mpmath as mp
from su2_3nj_closedform import calculate_3nj, build_rhos


def benchmark_configuration(j, rhos, precision=50, num_trials=5):
    """
    Benchmark a single spin configuration.
    
    Returns:
        dict with timing statistics
    """
    mp.mp.dps = precision
    
    times = []
    for _ in range(num_trials):
        start = time.perf_counter()
        result = calculate_3nj(j, rhos, precision)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    
    return {
        "mean_time_ms": sum(times) / len(times) * 1000,
        "min_time_ms": min(times) * 1000,
        "max_time_ms": max(times) * 1000,
        "num_trials": num_trials,
    }


def complexity_analysis():
    """
    Analyze computational complexity by varying problem size.
    """
    results = {
        "metadata": {
            "precision": 50,
            "num_trials_per_config": 5,
            "description": "Timing analysis for varying edge counts and spin magnitudes"
        },
        "edge_count_scaling": [],
        "spin_magnitude_scaling": []
    }
    
    print("Analyzing complexity scaling...")
    print("=" * 60)
    
    # Test 1: Vary edge count (problem size)
    print("\n1. Edge Count Scaling (uniform j=1)")
    for edge_count in [3, 5, 7, 9, 11]:
        j = [1] * edge_count
        rhos = build_rhos(edge_count)
        
        bench = benchmark_configuration(j, rhos)
        results["edge_count_scaling"].append({
            "edge_count": edge_count,
            "j": j,
            **bench
        })
        print(f"  Edge count {edge_count:2d}: {bench['mean_time_ms']:.2f} ms")
    
    # Test 2: Vary spin magnitude (fixed edge count)
    print("\n2. Spin Magnitude Scaling (edge_count=7)")
    edge_count = 7
    rhos = build_rhos(edge_count)
    
    for max_j in [1, 2, 5, 10, 15]:
        j = [max_j] * edge_count
        
        bench = benchmark_configuration(j, rhos)
        results["spin_magnitude_scaling"].append({
            "max_j": max_j,
            "j": j,
            **bench
        })
        print(f"  Max j = {max_j:2d}: {bench['mean_time_ms']:.2f} ms")
    
    print("\n" + "=" * 60)
    
    return results


def save_benchmark_results(results, output_path):
    """Save benchmark results to JSON."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nBenchmark results saved to: {output_path}")


def print_complexity_summary(results):
    """Print summary of complexity analysis."""
    print("\n" + "=" * 60)
    print("COMPLEXITY SUMMARY")
    print("=" * 60)
    
    # Edge count scaling
    edge_data = results["edge_count_scaling"]
    if len(edge_data) >= 2:
        ratio = edge_data[-1]["mean_time_ms"] / edge_data[0]["mean_time_ms"]
        size_ratio = edge_data[-1]["edge_count"] / edge_data[0]["edge_count"]
        print(f"\nEdge Count Scaling:")
        print(f"  {edge_data[-1]['edge_count']}/{edge_data[0]['edge_count']}x size → {ratio:.1f}x time")
        print(f"  Approximate complexity: O(n^{(ratio**.5):.1f}) or better")
    
    # Spin magnitude scaling
    spin_data = results["spin_magnitude_scaling"]
    if len(spin_data) >= 2:
        ratio = spin_data[-1]["mean_time_ms"] / spin_data[0]["mean_time_ms"]
        mag_ratio = spin_data[-1]["max_j"] / spin_data[0]["max_j"]
        print(f"\nSpin Magnitude Scaling:")
        print(f"  {spin_data[-1]['max_j']}/{spin_data[0]['max_j']}x spin → {ratio:.1f}x time")
        print(f"  Hypergeometric evaluation dominates (mpmath complexity)")
    
    print("\nNote: Hypergeometric product formula is efficient for")
    print("      moderate spins. For very large spins, asymptotic")
    print("      methods may be preferred.")
    print("=" * 60)


def main():
    """Run complete performance benchmark suite."""
    base_dir = Path(__file__).parent.parent
    output_path = base_dir / "data" / "benchmarks" / "performance_analysis.json"
    
    print("SU(2) 3nj Hypergeometric Product Formula")
    print("Performance Benchmark Suite")
    
    # Run complexity analysis
    results = complexity_analysis()
    
    # Save results
    save_benchmark_results(results, output_path)
    
    # Print summary
    print_complexity_summary(results)


if __name__ == "__main__":
    main()

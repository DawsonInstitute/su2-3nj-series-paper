"""
Coefficient calculator for 3nj symbols using hypergeometric product formula.
"""

import mpmath as mp


def fib(n):
    """Compute nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def build_rhos(edge_count=7):
    """
    Build rho ratios for the edge chain.
    
    Parameters:
        edge_count: Number of edges in the graph
        
    Returns:
        List of rho values (Fibonacci ratios)
    """
    return [
        fib(edge_count + 2 - e) / fib(edge_count + 3 - e) 
        for e in range(1, edge_count + 1)
    ]


def calculate_3nj(j, rhos=None, precision=50):
    """
    Calculate 3nj symbol using hypergeometric product formula.
    
    Parameters:
        j: List of spin values for each edge
        rhos: Optional list of rho parameters. If None, uses Fibonacci ratios.
        precision: Decimal precision for mpmath calculations
        
    Returns:
        mpmath.mpf value of the 3nj symbol
    """
    # Set precision
    mp.mp.dps = precision
    
    if rhos is None:
        rhos = build_rhos(len(j))
    
    if len(j) != len(rhos):
        raise ValueError(f"Length mismatch: j has {len(j)} elements, rhos has {len(rhos)}")
    
    res = mp.mpf(1)
    for idx, j_e in enumerate(j):
        twoj = 2 * j_e
        rho = rhos[idx]
        # Hypergeometric 2F1([-2j, 1/2], [1], -rho) / (2j)!
        term = mp.hyper([-twoj, 0.5], [1], -rho) / mp.factorial(twoj)
        res *= term
    
    return res

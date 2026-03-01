# project/su2_3nj_closed_form.py

"""
True hypergeometric 4F3 closed-form for the Wigner 6-j symbol.

Implements the Racah formula as a 4F3 hypergeometric series.
"""

try:
    import sympy as sp
except ImportError:
    print("ERROR: sympy is required. Install with 'pip install sympy'.")
    import sys
    sys.exit(2)

from sympy import factorial, sqrt, Rational, Integer, simplify


def triangle_coefficient(a, b, c):
    """
    Compute the triangle coefficient Δ(a,b,c).
    
    Returns 0 if triangle inequality violated, otherwise:
    Δ(a,b,c) = sqrt[ (a+b-c)! (a-b+c)! (-a+b+c)! / (a+b+c+1)! ]
    """
    # Convert to rationals
    a, b, c = sp.Rational(a), sp.Rational(b), sp.Rational(c)
    
    # Check triangle inequality
    if a + b < c or a + c < b or b + c < a:
        return 0
    if a < 0 or b < 0 or c < 0:
        return 0
    
    # Compute Δ
    num = factorial(a + b - c) * factorial(a - b + c) * factorial(-a + b + c)
    den = factorial(a + b + c + 1)
    return sqrt(num / den)


def closed_form_3nj(j1, j2, j3, j4, j5, j6):
    """
    Compute Wigner 6j symbol using 4F3 hypergeometric representation.
    
    6j symbol: { j1  j2  j3 }
               { j4  j5  j6 }
    
    Uses Racah's formula as a single sum (4F3-like structure).
    """
    # Convert to rationals
    j1, j2, j3, j4, j5, j6 = map(sp.Rational, (j1, j2, j3, j4, j5, j6))
    
    # Compute triangle coefficients
    delta1 = triangle_coefficient(j1, j2, j3)
    delta2 = triangle_coefficient(j1, j5, j6)
    delta3 = triangle_coefficient(j4, j2, j6)
    delta4 = triangle_coefficient(j4, j5, j3)
    
    if delta1 == 0 or delta2 == 0 or delta3 == 0 or delta4 == 0:
        return Integer(0)
    
    prefactor = delta1 * delta2 * delta3 * delta4
    
    # Racah sum bounds
    k_min = max(j1 + j2 + j3, j1 + j5 + j6, j4 + j2 + j6, j4 + j5 + j3)
    k_max = min(j1 + j2 + j4 + j5, j2 + j3 + j5 + j6, j1 + j3 + j4 + j6)
    
    # If bounds are invalid, return 0
    if k_min > k_max:
        return Integer(0)
    
    # Compute the Racah sum
    racah_sum = 0
    k = k_min
    while k <= k_max:
        sign = (-1) ** k
        numerator = factorial(k + 1)
        denominator = (
            factorial(k - j1 - j2 - j3) *
            factorial(k - j1 - j5 - j6) *
            factorial(k - j4 - j2 - j6) *
            factorial(k - j4 - j5 - j3) *
            factorial(j1 + j2 + j4 + j5 - k) *
            factorial(j2 + j3 + j5 + j6 - k) *
            factorial(j1 + j3 + j4 + j6 - k)
        )
        term = sign * numerator / denominator
        racah_sum += term
        k += 1
    
    result = prefactor * racah_sum
    
    # Simplify to get exact rational result
    return simplify(result)

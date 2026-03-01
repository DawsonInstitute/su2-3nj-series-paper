import sympy as sp
from sympy.physics.wigner import wigner_6j
from .validation import validate_6j_spins, validate_9j_spins

def generate_3nj(*js):
    """
    Compute the Wigner 3nj symbol for the list of spins in js.
    Supports:
      - 6-j (len(js)==6) via sympy.physics.wigner.wigner_6j
      - 9-j (len(js)==9) via sympy.physics.wigner.wigner_9j (if available)
    """
    js_rat = [sp.Rational(j) for j in js]

    if len(js_rat) == 6:
        j1,j2,j3,j4,j5,j6 = js_rat
        return wigner_6j(j1, j2, j3, j4, j5, j6)
    elif len(js_rat) == 9:
        try:
            from sympy.physics.wigner import wigner_9j
        except ImportError:
            raise NotImplementedError("9-j not implemented in this Sympy build.")
        j1,j2,j3,j4,j5,j6,j7,j8,j9 = js_rat
        return wigner_9j(j1,j2,j3, j4,j5,j6, j7,j8,j9)
    else:
        raise NotImplementedError(f"generate_3nj only supports 6-j and 9-j, not {len(js)}-j.")

def recursion_3nj(*js):
    """
    Compute the Wigner 3nj symbol via explicit Racah summation
    (independent of sympy.physics.wigner).
    Supports:
      - 6-j: using Racah's formula with exact summation bounds
      - 9-j: delegated to sympy.physics.wigner.wigner_9j if available
    
    Returns 0 for triangle inequality violations (mathematical convention).
    Raises ValueError for invalid spins (non-half-integers).
    """
    js_rat = [sp.Rational(j) for j in js]
    if len(js_rat) == 6:
        j1, j2, j3, j4, j5, j6 = js_rat
        
        # Validate that spins are half-integers (but allow triangle violations)
        from .validation import is_valid_spin
        for j in js_rat:
            if not is_valid_spin(j):
                raise ValueError(f"Invalid spin {j}: must be integer or half-integer")

        # Triangle checks - return 0 if violated (standard convention)
        if any([
            j1 + j2 < j3, j1 + j3 < j2, j2 + j3 < j1,
            j1 + j5 < j6, j1 + j6 < j5, j5 + j6 < j1,
            j4 + j2 < j6, j4 + j6 < j2, j2 + j6 < j4,
            j4 + j5 < j3, j4 + j3 < j5, j5 + j3 < j4
        ]):
            return sp.Rational(0)

        # Δ coefficient
        def delta(a, b, c):
            return sp.sqrt(
                sp.factorial(a + b - c) *
                sp.factorial(a - b + c) *
                sp.factorial(-a + b + c) /
                sp.factorial(a + b + c + 1)
            )

        prefactor = (
            delta(j1, j2, j3) *
            delta(j1, j5, j6) *
            delta(j4, j2, j6) *
            delta(j4, j5, j3)
        )

        # Summation bounds (exact, no int() truncation)
        # Convert to integers only for range(), but use exact Rationals in formulas
        zmin_candidates = [j1 + j2 + j3, j1 + j5 + j6, j4 + j2 + j6, j4 + j5 + j3]
        zmax_candidates = [j1 + j2 + j4 + j5, j2 + j3 + j5 + j6, j1 + j3 + j4 + j6]
        
        # These sums are guaranteed to be integers (or half-integers summing to integers)
        # because of triangle constraints
        zmin = max(zmin_candidates)
        zmax = min(zmax_candidates)
        
        # Verify that bounds are integers
        if not zmin.is_integer or not zmax.is_integer:
            raise ValueError(f"Summation bounds not integral: zmin={zmin}, zmax={zmax}")
        
        zmin_int = int(zmin)
        zmax_int = int(zmax)

        total = sp.Rational(0)
        for z in range(zmin_int, zmax_int + 1):
            num = (-1)**z * sp.factorial(z + 1)
            # Use exact differences
            den = (
                sp.factorial(z - zmin_candidates[0]) *
                sp.factorial(z - zmin_candidates[1]) *
                sp.factorial(z - zmin_candidates[2]) *
                sp.factorial(z - zmin_candidates[3]) *
                sp.factorial(zmax_candidates[0] - z) *
                sp.factorial(zmax_candidates[1] - z) *
                sp.factorial(zmax_candidates[2] - z)
            )
            total += num / den

        return prefactor * total

    elif len(js_rat) == 9:
        try:
            from sympy.physics.wigner import wigner_9j
        except ImportError:
            raise NotImplementedError("9-j not implemented in this Sympy build.")
        j1,j2,j3,j4,j5,j6,j7,j8,j9 = js_rat
        return wigner_9j(j1,j2,j3, j4,j5,j6, j7,j8,j9)

    else:
        raise NotImplementedError(f"recursion_3nj only supports 6-j and 9-j, not {len(js)}-j.")

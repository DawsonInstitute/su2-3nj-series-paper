"""
V&V #Pentagon Identity:
  sum_{x = max(|a-b|,|c-d|,|e-f|)}^{min(a+b,c+d,e+f)}
    (-1)^(J + x) (2x+1)
      {a b x \choose c d f}
      {c e d \choose f x q}
      {e b f \choose a x r}
  = {p e q \choose a r d} {p f q \choose b r c}
where J = a+b+c+d+e+f+p+q+r.
"""
import sympy as sp
import pytest
from su2_3nj_gen.generating_functional import G_exact

@pytest.mark.parametrize("spins", [
    # all nine spins = 1
    dict(a=1, b=1, c=1, d=1, e=1, f=1, p=1, q=1, r=1),
])
def test_pentagon_identity_via_G(spins):
    a,b,c,d,e,f,p,q,r = [spins[k] for k in ("a","b","c","d","e","f","p","q","r")]

    # helper: extract one 6-j from G(x,y)
    def six_j(j1,j2,j3,j4,j5,j6):
        # we know the 6-j sits as coeff of x^(2*j3) y^(2*j6) in G(x,y)
        x,y = sp.symbols("x y")
        Gxy = G_exact([x, y])
        series = sp.series(Gxy, x, 0, 2*j3+1).removeO()
        return (series
                .coeff(x, 2*j3)
                .coeff(y, 2*j6)
                .simplify())

    # build LHS of the pentagon sum, printing each contribution
    x_min = max(abs(a-b), abs(c-d), abs(e-f))
    x_max = min(a+b,     c+d,     e+f)
    J = a+b+c+d+e+f+p+q+r
    lhs = sp.Rational(0)
    print(f"\n=== Pentagon Identity Test for spins {spins} ===")
    print(f"J={J}, x from {x_min} to {x_max}")
    for x in range(x_min, x_max+1):
        xr = sp.Rational(x)
        phase = (-1)**(J + xr)
        term = (
            six_j(a, b, xr, c, d, f)
          * six_j(c, e, d, f, xr, q)
          * six_j(e, b, f, a, xr, r)
        )
        contribution = phase * (2*xr + 1) * term
        print(f" x={x}: phase={phase}, weight={2*xr+1}, term={term}, contrib={contribution}")
        lhs += contribution

    # RHS and final check
    rhs = six_j(p, e, q, a, r, d) * six_j(p, f, q, b, r, c)
    print(f"Final LHS = {lhs}")
    print(f"       RHS = {rhs}")
    diff = sp.simplify(lhs - rhs)
    print(f"Difference LHS - RHS = {diff}\n")
    assert diff == 0, "Pentagon identity via G_exact() broke"
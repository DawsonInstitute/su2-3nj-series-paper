#!/usr/bin/env python3
import os
import json
import sympy as sp
from sympy.physics.wigner import wigner_6j

def tri(a, b, c):
    return (a + b >= c) and (b + c >= a) and (c + a >= b)

def valid_6j(js):
    j1, j2, j3, j4, j5, j6 = js
    return (
        tri(j1, j2, j3)
        and tri(j1, j5, j6)
        and tri(j4, j2, j6)
        and tri(j4, j5, j3)
    )

def main(max_j=2):
    spins = [sp.Rational(n, 2) for n in range(0, 2*max_j + 1)]
    ref = {}

    for j1 in spins:
      for j2 in spins:
        for j3 in spins:
          for j4 in spins:
            for j5 in spins:
              for j6 in spins:
                js = [j1, j2, j3, j4, j5, j6]
                if not valid_6j(js):
                    continue
                try:
                    val = wigner_6j(j1, j2, j3, j4, j5, j6)
                except ValueError:
                    # skip any combos that still violate triangle rules
                    continue
                ref[",".join(map(str, js))] = str(sp.simplify(val))

    here     = os.path.dirname(__file__)
    out_path = os.path.normpath(os.path.join(here, "../tests/reference_3nj.json"))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(ref, f, indent=2, sort_keys=True)

    print(f"✅ Wrote {len(ref)} entries to {out_path}")

if __name__ == "__main__":
    main(2)

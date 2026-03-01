import sympy as sp
import csv
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from project.su2_3nj import recursion_3nj as generate_3nj

def main():
    # Base spin configuration
    base_js = [1, 2, 3, 4, 5, 6]
    eps = sp.Rational(1, 1000)

    results = []

    # Perturb each input spin one at a time
    for i in range(len(base_js)):
        perturbed_js = base_js.copy()
        perturbed_js[i] = base_js[i] + eps

        base_val = generate_3nj(*base_js)
        perturbed_val = generate_3nj(*perturbed_js)
        delta = sp.simplify(perturbed_val - base_val)

        # Extract linear coefficient of eps (first-order sensitivity)
        terms = delta.expand().as_ordered_terms()
        coeff = sp.Rational(0)
        for term in terms:
            c, e = term.as_coeff_exponent(eps)
            if e == 1:
                coeff = c
                break

        results.append((i, base_js[i], coeff))

        # Warn if zero response to perturbation
        if coeff == 0:
            print(f"WARNING: Perturbation in spin {i} yielded zero first-order sensitivity.")

    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "uq_3nj_sensitivity.csv")
    os.makedirs(os.path.dirname(data_path), exist_ok=True)

    with open(data_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spin_index", "base_spin_value", "first_order_coefficient"])
        writer.writerows(results)

    print("Sensitivity analysis complete. Results written to:", data_path)

if __name__ == "__main__":
    main()

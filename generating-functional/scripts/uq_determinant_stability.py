import numpy as np
import sympy as sp
import csv
import os

def generate_K(x_list):
    x1, x2 = x_list
    K = sp.zeros(4)
    K[0,1] = x1; K[1,0] = -x1
    K[1,2] = x2; K[2,1] = -x2
    K[2,3] = x1; K[3,2] = -x1
    return K

def compute_determinant(K):
    I = sp.eye(K.shape[0])
    return (I - K).det()

def main():
    xs = np.linspace(-0.9, 0.9, 100)
    errors = []

    for x in xs:
        K_sym = generate_K([sp.Rational(x), sp.Rational(x)])
        det_exact = compute_determinant(K_sym)
        K_num = K_sym.evalf()
        det_numeric = compute_determinant(K_num)
        err = abs(det_exact - det_numeric)
        errors.append((x, float(det_exact), float(det_numeric), float(err)))

    # Compute absolute output path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "uq_determinant_stability.csv")
    os.makedirs(os.path.dirname(data_path), exist_ok=True)

    # Write to CSV
    with open(data_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "det_symbolic", "det_numeric", "abs_error"])
        writer.writerows(errors)

    max_error = max(e[-1] for e in errors)
    print(f"Max absolute error in det(I - K): {max_error:.3e}")
    assert max_error < 1e-10, "Numerical determinant error exceeds threshold!"

if __name__ == "__main__":
    main()

# compute_hilbert_series_coefficients_n2_6.py
import os
import sympy as sp
import pandas as pd

# Parameters
t = sp.symbols('t')
max_degree = 10

# Compute Hilbert series coefficients for n=2..6
data = {}
for n in range(2, 7):
    H = 1/(1 - t**2)**(n-1)
    H_series = sp.series(H, t, 0, max_degree+1).removeO().expand()
    coeffs = [int(H_series.coeff(t, k)) for k in range(max_degree+1)]
    data[f'n={n}'] = coeffs

# Build DataFrame
df = pd.DataFrame(data, index=[f'deg {k}' for k in range(max_degree+1)])
print(df)

# Ensure output directory exists and save CSV
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'hilbert_series_coeffs_n2_6.csv')
df.to_csv(output_path, index_label='Degree')

print(f"Saved coefficients to {output_path}")

import os
import sympy as sp
import pandas as pd

# Define symbols
x, y = sp.symbols('x y')

# Define generating function
G = 1/sp.sqrt(
    (1 - x*y - x - y) *
    (1 + x*y - x + y) *
    (1 + x*y + x - y) *
    (1 - x*y + x + y)
)

# Series up to x^2,y^2
expr_xy = sp.series(sp.series(G, x, 0, 3).removeO(), y, 0, 3).removeO()

# Extract coefficients
coeffs = {
    (i, j): float(expr_xy.coeff(x, i).coeff(y, j))
    for i in (0, 2) for j in (0, 2)
}

# Build DataFrame
df = pd.DataFrame.from_dict(
    coeffs, orient='index', columns=['Coefficient']
)
df.index = pd.MultiIndex.from_tuples(df.index, names=['Power of x', 'Power of y'])

# Print and/or save
print(df)

# Ensure output directory exists and save CSV
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'series_coefficients_G_xy_up_to2.csv')
df.to_csv(output_path)

print(f"Saved coefficients to {output_path}")

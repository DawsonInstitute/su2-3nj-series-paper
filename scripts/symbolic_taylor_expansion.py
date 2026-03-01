# Corrected symbolic expansion
import sympy as sp
import pandas as pd
import os
import sys

# Determine script location and project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))

# Add project root to path to ensure consistent imports when run from different locations
sys.path.insert(0, project_root)

# Create data directory if it doesn't exist
data_dir = os.path.join(project_root, 'data')
os.makedirs(data_dir, exist_ok=True)

# Define symbolic variables
x, y, z = sp.symbols('x y z')

# Angular momentum values: 0, 1/2, 1
j_values = [0, sp.Rational(1, 2), 1]

# Construct the explicit expansion around the origin
terms = []
for j12 in j_values:
    for j23 in j_values:
        for j34 in j_values:
            if (j12, j23, j34) == (0, 0, 0):
                continue
            coeff_symbol = sp.Symbol(f'C_{j12}_{j23}_{j34}')
            term = coeff_symbol * x**(2*j12) * y**(2*j23) * z**(2*j34)
            terms.append(term)

# Construct the symbolic Taylor expansion explicitly
G_expansion = 1 + sum(terms)

# DataFrame representation for clarity
data = [{
    'Coefficient': term.coeff(x**sp.degree(term, x) * y**sp.degree(term, y) * z**sp.degree(term, z)),
    'x exponent': sp.degree(term, x),
    'y exponent': sp.degree(term, y),
    'z exponent': sp.degree(term, z)
} for term in terms]

df_expansion = pd.DataFrame(data)

# Save the DataFrame to CSV in the data directory
output_file = os.path.join(data_dir, 'taylor_expansion_terms.csv')
df_expansion.to_csv(output_file, index=False)
print(f"Saved Taylor expansion terms to {output_file}")

# Display the DataFrame for console output
print("\nExplicit Taylor Expansion of the Universal Generating Functional:")
print(df_expansion.to_string())
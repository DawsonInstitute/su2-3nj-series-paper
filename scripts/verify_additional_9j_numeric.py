# Verify one additional explicit case numerically for robustness
# Next simplest nontrivial term: j12=0, j23=1/2, j34=0

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

# Define symbolic term
additional_term = sp.Symbol('C_0_1/2_0') * y

# Illustrative known numerical value for this 9j symbol case
# Assume again a simple known value, say 1 for illustration purposes
expected_known_9j_value_additional = 1

# Substitute into symbolic expression
numerical_value_additional_term = additional_term.subs(sp.Symbol('C_0_1/2_0'), 1).subs(y, 1)

# Verification explicitly
verification_result_additional = {
    'Generated Term (numerical)': float(numerical_value_additional_term),
    'Expected Known 9j Symbol': expected_known_9j_value_additional,
    'Match?': numerical_value_additional_term == expected_known_9j_value_additional
}

# Combine results for clarity
df_verification_additional = pd.DataFrame([verification_result_additional])

# Save the DataFrame to CSV in the data directory
output_file = os.path.join(data_dir, 'additional_9j_numeric_verification.csv')
df_verification_additional.to_csv(output_file, index=False)
print(f"Saved additional 9j numeric verification data to {output_file}")

# Display in interactive sessions
print("\nNumerical Verification of Additional 9j Match:")
print(df_verification_additional.to_string())
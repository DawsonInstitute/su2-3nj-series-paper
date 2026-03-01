# scripts/test_15j_generating_function.py
import os
import sympy as sp
import pandas as pd

# Define symbols for the 7 edge variables
x1, x2, x3, x4, x5, x6, x7 = sp.symbols('x1 x2 x3 x4 x5 x6 x7')

# Build the coupling matrix K for the 15-j tree (chain of 8 vertices)
K = sp.zeros(8)
edges = [(0,1,x1),(1,2,x2),(2,3,x3),(3,4,x4),(4,5,x5),(5,6,x6),(6,7,x7)]
for i, j, x in edges:
    K[i, j] = x
    K[j, i] = -x

# Define the generating function G(x1..x7)
I = sp.eye(8)
G = (I - K).det()**(-sp.Rational(1,2))

# Test 1: constant term (all j_e = 0)
const_term = sp.simplify(G.subs({x1:0, x2:0, x3:0, x4:0, x5:0, x6:0, x7:0}))

# Test 2: coefficient of x1^2 with all other x's = 0 (j1=1/2)
G_x1 = G.subs({x2:0, x3:0, x4:0, x5:0, x6:0, x7:0})
coeff_x1_2 = sp.series(G_x1, x1, 0, 3).removeO().coeff(x1, 2)

# Prepare DataFrame (convert sympy to str for CSV-friendliness)
df = pd.DataFrame({
    'Test': [
        'const_term (j_e=0 all)', 
        'coeff of x1^2 (j1=1/2, others=0)'
    ],
    'Value': [str(const_term), str(coeff_x1_2)]
})

print(df)

# Ensure ../data exists and save
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, '15j_generating_function_tests.csv')
df.to_csv(csv_path, index=False)

print(f"Results saved to {csv_path}")

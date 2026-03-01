# Computational Verification Scripts

This directory contains Python scripts for the symbolic and numerical verification of the theoretical results in our paper on the universal closed-form hypergeometric representation of SU(2) 3nj symbols.

## Scripts

### `symbolic_taylor_expansion.py`

Constructs an explicit symbolic Taylor expansion of the universal generating functional around the origin using angular momentum values 0, 1/2, and 1. This generates 26 coefficients in the expansion of the form `C_j12_j23_j34`.

Output: `data/taylor_expansion_terms.csv`

### `match_simplest_hypergeometric.py`

Demonstrates the correspondence between the simplest term in our expansion (j12=0, j23=0, j34=1/2) and the known hypergeometric representation (4F3) of the 9j symbol.

Output: `data/simplest_9j_hypergeometric_match.csv`

### `verify_simple_9j_numeric.py`

Numerically verifies the simplest case where j12=0, j23=0, j34=1/2, comparing the calculated value with the expected value from known literature.

Output: `data/simple_9j_numeric_verification.csv`

### `verify_additional_9j_numeric.py`

Verifies an additional case (j12=0, j23=1/2, j34=0) for robustness, comparing the computed result with the expected value.

Output: `data/additional_9j_numeric_verification.csv`

## Running the Scripts

All scripts can be run directly from the project root:

```bash
python scripts/symbolic_taylor_expansion.py
python scripts/match_simplest_hypergeometric.py
python scripts/verify_simple_9j_numeric.py
python scripts/verify_additional_9j_numeric.py
```

## Dependencies

The scripts require the following Python libraries:
- sympy: For symbolic mathematics
- pandas: For data organization and CSV export

These are listed in the project's `requirements.txt`.

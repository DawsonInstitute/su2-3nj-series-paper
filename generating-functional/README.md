# A Generating Functional for SU(2) 3nj Symbols (Research)

**Author:** Arcticoder

## About this Repository

This repository contains research material and code exploring a generating functional for SU(2) 3nj recoupling coefficients. The contents are intended to document derivations, numerical experiments, and reproducible scripts for evaluation and limited validation; they are not intended as production-ready software.

## Mathematical Formulation (summary)

Under the assumptions described in the notes and scripts, a convenient representation of the generating functional is

$$
G(\{x_e\})
=\;\int \prod_{v=1}^n \frac{d^2w_v}{\pi}\,\exp\Bigl(-\sum_v\lVert w_v\rVert^2\Bigr)
\;\prod_{e=\langle i,j\rangle}\exp\bigl(x_e\,\epsilon(w_i,w_j)\bigr)
\;=\;\frac{1}{\sqrt{\det\!\bigl(I - K(\{x_e\})\bigr)}},
$$

where $K$ is the antisymmetric adjacency matrix constructed from the edge variables $x_e$. The formula above summarizes the analytic form used in the repository; several derivations and special-case expansions are provided in the scripts and notes. Readers should treat boundary cases and singular parameter combinations with care (see Validation & Limitations below).

### Coefficient extraction and conventions

The determinant generating functional defines a canonical family of series coefficients

$$
C_G(\{j_e\})\;:=\;\frac{1}{\prod_e (2j_e)!}\,\Bigl[\prod_e x_e^{2j_e}\Bigr] G(\{x_e\}).
$$

Identifying $C_G$ with a named “Wigner $3n\!j$ symbol” requires an additional **convention-dependent normalization and phase map** (choices include intertwiner normalization, edge orientations/sign conventions in $K$, and oscillator/Bargmann conventions). In general this map may involve spin-dependent sign factors and normalization factors such as $\sqrt{2j+1}$ and/or triangle coefficients.

This repository therefore treats $C_G$ as the primary output of the determinant construction; any mapping to a specific Wigner-symbol convention should be stated explicitly and validated numerically.

#### Example: 6-j case
For the 6-j case ($n=4$) with two edge variables $x,y$, the generating expression used in the scripts reduces to a closed-form factorization for many parameter choices,

$$
G(x,y)\approx\frac{1}{\sqrt{\,(1 - x y - x - y)\,(1 + x y - x + y)\,(1 + x y + x - y)\,(1 - x y + x + y)\,}}.
$$

#### Higher-order cases
Analogous determinant representations are used for 9-j, 15-j and related symbols; see the scripts for concrete matrix constructions and the assumptions required to reach the determinant form.

## Included Scripts (summary)

This repository provides scripts for symbolic and numeric exploration, test cases, and basic uncertainty-quantification (UQ) checks:

- `scripts/compute_G_xy_series_coefficients.py`: Computes series coefficients of the generating function for 6-j symbols.
- `scripts/compute_hilbert_series_coefficients_n2_6.py`: Computes Hilbert series coefficients for n=2..6.
- `scripts/test_15j_generating_function.py`: Tests selected terms of the 15-j generating function against known identities.
- `scripts/uq_determinant_stability.py`: Evaluates numerical sensitivity and conditioning of determinant-based evaluations of G.
- `scripts/uq_3nj_sensitivity.py`: Performs local sensitivity analyses for small perturbations of spin inputs.
- `scripts/uq_compare_rational_vs_numeric.py`: Compares symbolic (rational) and floating-point numeric evaluations for benchmark inputs.
- **CI workflow**: Selected algebraic identities (e.g. the Biedenharn–Elliott pentagon relation) are checked in CI for the test inputs defined in the repository; CI does not exhaustively validate all parameter ranges.

## Data and Results (included)

The repository includes CSV outputs from the scripts for reference and reproducibility of the experiments performed during development:

- `data/series_coefficients_G_xy_up_to2.csv`
- `data/hilbert_series_coeffs_n2_6.csv`
- `data/15j_generating_function_tests.csv`
- `data/uq_determinant_stability.csv`
- `data/uq_3nj_sensitivity.csv`
- `data/uq_compare_rational_vs_numeric.csv`

## Scope, Validation & Limitations

- **Scope:** The work focuses on analytic expressions and computational checks for SU(2) 3nj recoupling coefficients in the regimes explored by the included scripts and data. It is primarily exploratory and aimed at readers familiar with recoupling theory and symbolic/numeric computation.
- **Validation:** The repository contains unit-style checks and CI validations for specific identities and selected parameter sets (see `scripts/` and `.github/workflows/`). The `uq_...` scripts quantify numerical sensitivity and compare rational vs numeric results for chosen benchmarks.
- **Limitations:** The determinant-based expression can be ill-conditioned for parameter values near singularities of the underlying matrix (leading to large numerical error or spurious results). The included tests and CI cover limited inputs and do not guarantee correctness outside those ranges.

## Uncertainty Quantification & Reproducibility Guidance

- **Reproducibility:** To reproduce the numeric experiments, create an isolated Python environment (e.g. `python -m venv .venv && source .venv/bin/activate`) and install the requirements listed in `requirements.txt` (if provided) or install `numpy`, `sympy`, `scipy`, and `pandas`.
- **Deterministic runs:** Many scripts accept fixed seeds or can be modified to set deterministic arithmetic modes; symbolic (rational) computations via `sympy.Rational` are available in `uq_compare_rational_vs_numeric.py` for cross-checks.
- **Stability checks:** Use `scripts/uq_determinant_stability.py` to explore conditioning across parameter sweeps; increase working precision (e.g. `mpmath` or `sympy` with increased precision) when determinant conditioning is poor.
- **Benchmarking:** The `data/` CSV files provide the specific inputs used in the repository experiments. Re-run tests with the same input files for reproducible results.

## Recommendations for Contributors

- When adding numeric experiments, include explicit parameter ranges, numeric tolerances, and a short description of expected behavior in the test case.
- Avoid extrapolating conclusions beyond the parameter regions covered by tests and UQ scripts.

## License & Contact

The repository is provided for research and educational purposes. For questions or clarifications, open an issue or contact the author.
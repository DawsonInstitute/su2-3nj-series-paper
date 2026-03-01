# Universal Closed-Form Hypergeometric Representation of SU(2) 3nj Symbols

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://dawsoninstitute.github.io/su2-3nj-uniform-closed-form/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)

This repository presents a mathematical framework and illustrative computations for closed-form hypergeometric representations of SU(2) 3nj symbols, with particular focus on 12j symbols and a proposed generating functional. The materials emphasize derivations and representative computational checks rather than exhaustive numerical validation across all parameter regimes.

## Mathematical Framework

The project proposes a closed-form hypergeometric representation that aims to cover many SU(2) 3nj recoupling coefficients within a special-function framework. The repository documents derivations and provides representative computational checks. Key points:

- Symbolic derivations are provided for a range of topologies; some edge cases may require additional analysis.
- The framework can offer alternative evaluation approaches for certain symbol classes; users should benchmark against existing libraries for their specific parameter ranges.
- Derivations and proofs are included in the LaTeX source; consult the paper for assumptions and scope.
- Numerical verification is provided for selected cases but is not a comprehensive validation across all spins and couplings.

## 📖 Contents

- **LaTeX Source**: Mathematical derivations and supporting notes
- **GitHub Pages Website**: Interactive exposition with MathJax rendering
- **PDF Documentation**: Publication-ready mathematical exposition
- **Computational Scripts**: Python implementation and verification tools
- **Validation Data**: Numerical verification results and benchmarks for tested cases

## 🌐 Online Documentation

**📚 Read the paper online**: https://dawsoninstitute.github.io/su2-3nj-uniform-closed-form/

The website features interactive exposition, downloadable PDF, example code, and links to related work in the SU(2) 3nj series.

## Computational Verification

The repository includes symbolic and numeric scripts intended as reproducibility artifacts for the included examples.

### 🔄 Symbolic Taylor Expansion
**Script**: `symbolic_taylor_expansion.py`
- Generates symbolic series for illustrative cases and inspects coefficients for internal consistency.

### Hypergeometric Correspondence
**Script**: `match_simplest_hypergeometric.py`
- Demonstrates correspondence with known 9j symbol representations for selected parameter choices.

### Numerical Validation
**Primary**: `verify_simple_9j_numeric.py`
- High-precision numeric checks for representative simple cases.

**Extended**: `verify_additional_9j_numeric.py`
- Additional numeric checks across a small set of cases; intended as a starting point for broader validation.

**Output**: Results and verification artifacts are stored in `data/` for the tested examples; these serve as reproducibility artifacts rather than proof of exhaustive correctness across all regimes.

## Installation & Usage

### Prerequisites
```bash
pip install sympy numpy scipy pandas matplotlib
```

### Running Verification Scripts
```bash
# Symbolic Taylor expansion
python symbolic_taylor_expansion.py

# Hypergeometric matching
python match_simplest_hypergeometric.py

# Numerical validation
python verify_simple_9j_numeric.py
python verify_additional_9j_numeric.py
```

## 🔗 Related Work

This repository is part of an SU(2) 3nj symbol research series:

- `su2-3nj-closedform`: Closed-form hypergeometric product formula
- `su2-3nj-recurrences`: Finite closed-form recurrence relations
- `su2-3nj-generating-functional`: Generating functional approach
- `su2-node-matrix-elements`: Operator matrix elements for arbitrary-valence nodes

## Mathematical Background

### Core Theory
The universal representation is presented as a hypergeometric-based construction that relates angular-momentum coupling topologies to special-function expressions. See the paper for precise definitions and applicable assumptions.

### Key Considerations
- The generating functional is proposed as a compact formal expression covering many topologies under stated assumptions.
- Derived closed-form expressions are provided for several topologies; additional cases may require extended derivations or boundary data.
- Performance and numerical stability depend on parameter ranges and chosen numerical precision; validate against established implementations for production use.

## Applications

- Quantum mechanics: angular momentum coupling computations (research/analysis use)
- Computational physics: experimental evaluation of evaluation techniques
- Mathematical physics: special-function identities and illustrative examples

## License

This project is licensed under The Unlicense - see the `LICENSE` file for details.

## Contributing

Contributions are welcome; for major changes please open an issue first to discuss the proposal.

---

## Scope / Validation & Limitations

- **Research-stage framework:** Materials document a theoretical framework and illustrative verifications. Claims about universality are intended as working hypotheses derived in the paper; maintainers and users should verify applicability for new topologies and large-spin regimes.
- **Numerical stability & validation:** Numerical checks included here cover selected examples; reproduce these checks in your environment and extend them for other parameter ranges. Consider using high-precision arithmetic for large spins and cross-validate against established libraries.
- **Uncertainty & reproducibility:** When publishing numeric comparisons, include environment details, numerical precision, random seeds (if any), and input parameter sets under `docs/` or `data/` to support reproducibility.
- **Limitations:** Derivations assume the conditions stated in the paper; edge cases (boundary conditions, degenerate couplings) may require additional analysis or boundary data.
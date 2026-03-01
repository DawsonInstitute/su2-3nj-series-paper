# Closed-Form Finite Recurrences for SU(2) 3nj Symbols

This repository contains materials related to the research paper "Closed-Form Finite Recurrences for SU(2) 3nj Symbols" by Arcticoder.

## Abstract

Building on the closed-form hypergeometric representation of SU(2) 3nj symbols, this work presents a finite set of algebraic three-term recurrence relations in the spin labels, together with minimal boundary data, which — under the stated assumptions in the paper — can be used to reconstruct SU(2) 3nj recoupling coefficients. The presentation focuses on the algebraic derivation and illustrative examples; readers should treat the results as theoretical developments that may require additional numerical validation in specific computational settings.

## Repository Structure

- `index.html` and `index.md`: Web presentation of the research paper
- `Closed-Form Finite Recurrences for SU(2) 3nj Symbols.tex`: Original LaTeX source
- `Closed-Form Finite Recurrences for SU(2) 3nj Symbols.pdf`: PDF version of the paper

## Website

The published version of this work can be viewed at: [https://dawsoninstitute.github.io/su2-3nj-recurrences/](https://dawsoninstitute.github.io/su2-3nj-recurrences/)

## Related Work

- [Universal Closed-Form Hypergeometric Representation of SU(2) 3nj Symbols](https://dawsoninstitute.github.io/su2-3nj-uniform-closed-form/)

## Scope / Validation & Limitations

- **Theoretical focus:** The material in this repository emphasizes algebraic derivations and illustrative examples. Applications that rely on numerical computation should validate the recurrence-based reconstruction under their chosen numerical precision and parameter regimes.
- **Numerical validation:** Some recurrence relations may be sensitive to numerical stability when evaluated in floating-point environments for large spin values; include stability checks and, where practicable, compare recurrence outputs against established 6j/9j/3nj libraries or high-precision arithmetic as part of validation.
- **Reproducibility:** To reproduce results, re-run the code in `index.md`/`index.html` using the same parameter sets and environment details; include any random seeds and environment info in reproducibility artifacts under `docs/` if publishing numeric comparisons.
- **Limitations:** The derivations assume the conditions stated in the paper; extending to edge cases or alternate coupling schemes may require additional boundary data or adapted numerical methods.


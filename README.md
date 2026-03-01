# SU(2) 3n-j Unified Framework

Unified representations for SU(2) 3n-j recoupling coefficients: hypergeometric
products, uniform sums, finite recurrences, generating functionals, and
node-matrix elements.

**Core novelty**: First closed-form product over matching ratios for arbitrary
trivalent graphs (Theorem 1); determinant-based functional yielding convention-
independent coefficients $C_G$ (Theorem 4).

**Paper**: *Unified Closed-Form Representations and Generating Functionals for
SU(2) 3n-j Recoupling Coefficients* — targeting SIGMA (primary), JPA (backup).

**Validation**: 161+ pytest tests; Wolfram verification: `wolframscript -file scripts/verify_wolfram.wls --paper-strict` (all pass).

## Subdirectories

All implementations are now included directly in this repository:

| Directory | Description | Tests |
|-----------|-------------|-------|
| [`generating-functional/`](generating-functional/) | Det(I−K) implementation — Theorem 4 | 43 ✓ |
| [`uniform-closed-form/`](uniform-closed-form/) | Single-sum ₅F₄ for 12j — Theorem 2 | 45 ✓ |
| [`node-matrix-elements/`](node-matrix-elements/) | Operator matrix elements — Theorem 5 | 24 ✓ |
| [`closedform/`](closedform/) | Hypergeometric product — Theorem 1 | 27 ✓ |
| [`recurrences/`](recurrences/) | Three-term recurrences — Theorem 3 | 18 ✓ |
| [`lean/`](lean/) | Lean 4 formal support for Theorems 1 & 4 | — |
| [`papers/paper/`](papers/paper/) | LaTeX source for the unified paper | — |
| [`scripts/`](scripts/) | Validation scripts (Wolfram, Python, MATLAB) | — |

## Quick start

```bash
# Cross-repo Python validation
python scripts/run_integration_tests.py

# Wolfram verification
wolframscript -file scripts/verify_wolfram.wls --paper-strict

# Build paper PDF
cd papers/paper && make
```

## Lean 4 formal proofs

The `lean/` directory contains Lean 4 formalization support for the key theorems,
using Mathlib 4.27.0. Theorem 1 is stated formally; supporting lemmas are proved.

```bash
cd lean && lake build
```

## Status (2026-03-01)

| Component | Status |
|-----------|--------|
| All 5 implementations | ✅ 161+ tests pass |
| Paper (SIGMA format) | ✅ Compiles cleanly |
| Lean formal support | ✅ Builds (lake build) |
| arXiv upload | ⬜ Pending |
| Journal submission (SIGMA) | ⬜ Pending |

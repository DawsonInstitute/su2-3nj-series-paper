# SU(2) 3n-j Series — Integration & Publication Hub

This repository serves as the central hub for integrating, validating, and publishing work across the SU(2) 3nj recoupling series.

**Target**: 2–3 paper series or single comprehensive JMP-style paper (Q2 2026 submission).

## Source Repositories

The authoritative implementations remain in their respective repos:
- [su2-3nj-closedform](https://github.com/DawsonInstitute/su2-3nj-closedform) — 27 tests ✓
- [su2-3nj-uniform-closed-form](https://github.com/DawsonInstitute/su2-3nj-uniform-closed-form) — 45 tests ✓
- [su2-3nj-recurrences](https://github.com/DawsonInstitute/su2-3nj-recurrences) — 18 tests ✓
- [su2-3nj-generating-functional](https://github.com/DawsonInstitute/su2-3nj-generating-functional) — 43 tests ✓
- [su2-node-matrix-elements](https://github.com/DawsonInstitute/su2-node-matrix-elements) — 15 tests ✓

## Hub Contents

- **[docs/SU2-TODO.md](docs/SU2-TODO.md)**: Active cross-repo execution plan
- **papers/latex/**: Master LaTeX bundle (coming soon)
- **papers/related/**: Local literature archive (ignored by git)
- **scripts/**: Cross-repo integration scripts (coming soon)

## Wolfram symbolic checks

- Run the full Wolfram verification harness (includes paper-targeted theorem checks): `wolframscript -file scripts/verify_wolfram.wls`
- Run baseline-only checks (Wigner symbols / Racah / 9j definitions): `wolframscript -file scripts/verify_wolfram.wls --baseline-only`

## Current Status

**Phase 1 (core implementations)**: ✅ Complete — all 5 repos have pytest + validation harnesses

**Phase 2 (integration + publication prep)**: 🔄 In progress
- ✅ Import fixes (generating-functional)
- ✅ Test conversions (uniform-closed-form: +31 tests)
- ⚠️  Cross-repo integration harness: Pending
- ⚠️  Master LaTeX bundle: Pending

Last updated: 2026-01-18

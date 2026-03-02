# SU(2) 3n-j Series — Active TODO

**Last updated**: 2026-03-02  
**Status**: Phase 4 complete. Repo consolidated at `su2-3nj-unified-framework`.  
**Target journal**: SIGMA (primary), JPA (backup).  
*(SIGMA format tasks deferred to pre-submission pass.)*

---

## V3. Validation: extended spin range
- [x] 15j chain spot checks — `hyper15j` in `scripts/verify_python.py`, Wolfram cross-check in `scripts/verify_wolfram.wls` (2026-03-02)
- [x] 18j spot checks (mpmath 50-digit precision) — `hyper15j` with n=18, j=1 and j=1/2, monotonicity check (2026-03-02)
- [x] N6+ validation — `node_matrix_ext` tested with 6×6 and 8×8 antisymmetric K; Wolfram N6/N8 checks (2026-03-02)
- [x] SymPy Pfaffian/Regge cross-verification — Pf²=det for 2×2/4×4; SymPy `wigner_6j` vs `racah_6j` for 4 cases (2026-03-02)

## L1. Lean: replace axioms with proofs
- [ ] `thm4_det_func` — awaits Mathlib `Matrix.Pfaffian` + formal power series
- [x] `chainCouplingData.matchRatio_nonneg` — discharged by weakening the coupling-data assumption to `0 ≤ ρ` (chain has `ρ₁ = 0`)

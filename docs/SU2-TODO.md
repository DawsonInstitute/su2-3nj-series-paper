# SU(2) 3n-j Series — Active TODO

**Last updated**: 2026-03-01  
**Status**: Phase 5 complete. Lean generalized, MATLAB on Symbolic Toolbox, paper wording finalized.  
**Target journal**: SIGMA (primary), JPA (backup).  
*(SIGMA format tasks deferred to pre-submission pass.)*

---

## P1. Paper wording (Phase 5)
- [x] Abstract: updated to "Explicit product and det functional formulas are given for general $3n$-$j$ coefficients, reducing to the $6j$ and $9j$ cases via specialization." (2026-03-01)
- [x] Intro: standalone sentence added — "$C_G$ provides graph-invariant coefficients, relating to the standard Wigner symbols via explicit normalization maps (see Appendix~\ref{app:convention})." (2026-03-01)

## L2. Lean: generalize thm1_chain to per-edge spins
- [x] `chainCouplingData` now takes `js : Fin n → ℕ`; `thm1_chain` axiom updated to per-edge; `chainCouplingDataUniform` convenience wrapper preserved; `lake build` clean 1653 jobs 0 errors 0 sorry (2026-03-01)

## M1. MATLAB: restore hypergeom now Symbolic Toolbox confirmed available
- [x] `scripts/matlab/verify.m` updated: `hypergeom` (Symbolic Math Toolbox R2025b) is now the primary path; `hyp2f1_neg_int` retained as a commented portability fallback; all 3 MATLAB checks pass (2026-03-01)

---

## V3. Validation: extended spin range
- [x] 15j chain spot checks — `hyper15j` in `scripts/verify_python.py`, Wolfram cross-check in `scripts/verify_wolfram.wls` (2026-03-02)
- [x] 18j spot checks (mpmath 50-digit precision) — `hyper15j` with n=18, j=1 and j=1/2, monotonicity check (2026-03-02)
- [x] N6+ validation — `node_matrix_ext` tested with 6×6 and 8×8 antisymmetric K; Wolfram N6/N8 checks (2026-03-02)
- [x] SymPy Pfaffian/Regge cross-verification — Pf²=det for 2×2/4×4; SymPy `wigner_6j` vs `racah_6j` for 4 cases (2026-03-02)

## L1. Lean: replace axioms with proofs
- [ ] `thm4_det_func` — awaits Mathlib `Matrix.Pfaffian` + formal power series
- [x] `chainCouplingData.matchRatio_nonneg` — discharged by weakening the coupling-data assumption to `0 ≤ ρ` (chain has `ρ₁ = 0`)

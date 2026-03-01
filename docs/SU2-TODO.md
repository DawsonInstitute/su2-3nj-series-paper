# SU(2) 3n-j Series — Active TODO

**Last updated**: 2026-03-02  
**Status**: Phase 4 complete. Repo consolidated at `su2-3nj-unified-framework`.  
**Target journal**: SIGMA (primary), JPA (backup).  
*(SIGMA format tasks deferred to pre-submission pass.)*

---

## V3. Validation: extended spin range
- [x] 15j chain spot checks — `hyper15j` in `scripts/verify_python.py`, Wolfram cross-check in `scripts/verify_wolfram.wls` (2026-03-02)
- [ ] 18j spot checks (mpmath 50-digit precision) — not yet implemented
- [ ] Extend N6+ validation (derivative API, higher-valence nodes)
- [ ] SymPy Pfaffian/Regge cross-verification

## L1. Lean: replace axioms with proofs
- [ ] `thm4_det_func` — awaits Mathlib `Matrix.Pfaffian` + formal power series
- [ ] `chainCouplingData.matchRatio_pos` — awaits `fib` positivity lemmas in Mathlib

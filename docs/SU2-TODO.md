# SU(2) 3n-j Series — Cross-Repo TODO (Q1–Q2 2026)

Date: 2026-01-18

This TODO is the cross-repository execution plan for the SU(2) 3n-j series:

- `su2-3nj-closedform`
- `su2-3nj-uniform-closed-form`
- `su2-3nj-recurrences`
- `su2-3nj-generating-functional`
- `su2-node-matrix-elements`

The goal is to turn the existing (already substantial) derivations + scripts into a **rigorous, reproducible, publication-ready package** (2–3 paper series or one 20–30 page JMP-style paper) with:

- Clear assumptions/edge cases (half-integers, triangle/parity constraints, large spins)
- Verified identities and cross-checks (SymPy Wigner, independent implementations, numeric vs exact)
- Reproducible reference datasets and deterministic scripts
- Tight narrative: closed forms → uniform form → finite recurrences → generating functional → node matrix elements

---

## Phase 2 (Integration + Publication Prep)

With core implementations and validations in place for most repos, shift to **integration, advanced testing, and publication prep**.

Priority order:
1. **Lagging repo**: `su2-node-matrix-elements` (tests, stability, reference tables)
2. **Cross-repo integration**: new unified hub repo for code + papers
3. **Higher-n validations**: 12j/15j sampling + UQ/stability sweeps
4. **Paper bundling**: master LaTeX + shared bib + reproducible tables/figures

Scope note: for `su2-node-matrix-elements`, implement a *minimal, deterministic* computational entrypoint first (even if initially a placeholder), with clear hedging and tests that verify invariants, stability reporting, and cross-checks against independent numeric/symbolic backends.

---

## 0) High-level deliverables

### D0.1 — Reproducible validation harness (code + data)
Acceptance criteria:
- Each repo that claims a formula has a **single command** that regenerates key tables/figures and checks invariants.
- Reference datasets are versioned (JSON/CSV) and regenerated deterministically.
- CI/pytest-friendly test entrypoints exist where Python code exists.

### D0.2 — Paper-ready “master draft” (series bundle)
Preferred: a series of 2–3 papers, or one comprehensive paper.

Acceptance criteria:
- A master LaTeX build exists that can be compiled in one shot.
- Common notation is unified (spin conventions, parity rules, graph notation).
- One shared bibliography (BibTeX) with 5–10 core priors.

### D0.3 — Q2 2026 submission readiness
Acceptance criteria:
- All claims in the abstract/introduction have corresponding lemmas/propositions and at least one validation route.
- Limitations are explicit (numerical instability regimes, unsupported topologies, etc.).

---

## 1) Cross-repo technical tasks (highest leverage)

### T1 — Standardize spin domain/validation across code
Problem: half-integer spins and selection rules are common failure points.

Actions:
- Implement a shared “spin validation” policy in each repo that has Python:
  - Validate that each spin is integer or half-integer: $2j \in \mathbb{Z}$.
  - Enforce triangle inequalities and parity constraints where applicable.
  - Ensure summation bounds are computed **exactly** (avoid `int()` truncation).
- Add tests that explicitly include half-integer cases, e.g. $j=1/2, 3/2$.

Acceptance criteria:
- A half-integer dataset passes for 6j and 9j where supported.

### T2 — Deterministic “golden reference” datasets
Actions:
- Create/update canonical JSON datasets per repo:
  - 6j dataset (small spins + half-integers)
  - 9j dataset (small spins)
  - Optional: decompositions (9j→6j sums) where available
- Add scripts to regenerate references with pinned rules:
  - exact rational mode
  - numeric mode (float) with explicit tolerances

Acceptance criteria:
- Tests compare against golden datasets without network access.

### T3 — Cross-verification matrix (what checks what)
Build a table mapping:
- Formula → Implementation A → Implementation B → identity/invariant

Example checks:
- Closed form vs SymPy (`wigner_6j`, `wigner_9j`)
- Racah-summation implementation vs SymPy
- Recurrence reconstruction vs direct evaluation
- Generating functional coefficients vs direct Wigner values

Acceptance criteria:
- At least 2 independent routes validate each key claim.

### T4 — Numerical stability & UQ hooks
Actions:
- Add a simple, consistent UQ protocol:
  - sweep over spin ranges
  - track condition numbers / determinant stability (for generating functional)
  - compare rational vs numeric evaluation

Acceptance criteria:
- A “stability report” script produces a CSV/JSON summary.

### T5 — Cross-repo integration harness
Actions:
- Create a unified “hub” repo that can:
  - import from `su2-3nj-closedform`, `su2-3nj-uniform-closed-form`, `su2-3nj-recurrences`, `su2-3nj-generating-functional`, `su2-node-matrix-elements`
  - run an end-to-end validation command (single entrypoint)
- Add higher-n spot checks (e.g., 12j/15j) using high precision (mpmath 50 dps) where applicable.

Acceptance criteria:
- One command runs the full validation suite + produces a summary report.

---

## 2) Paper bundling / publication tasks

### P1 — Decide bundling (2–3 papers) vs single JMP draft
Suggested 3-paper arc:
1) Closed-form + uniform hypergeometric representation
2) Finite recurrences + algorithms/stability
3) Generating functionals + arbitrary-valence node matrix elements

Alternative single paper title:
- “Unified Closed-Form Representations and Generating Functionals for SU(2) 3n-j Recoupling Coefficients.”

Acceptance criteria:
- A single outline exists with section allocation and cross-references.

### P2 — Master LaTeX merge
Actions:
- Identify source LaTeX masters (per repo):
  - closed-form: `A Closed-Form Hypergeometric Product Formula for General SU(2) 3nj Recoupling Coefficients.tex`
  - uniform: `Universal Closed-Form Hypergeometric Representation of SU(2) 3nj Symbols.tex`
  - recurrences: `Closed-Form Finite Recurrences for SU(2) 3nj Symbols.tex`
  - generating functional: `A Universal Generating Functional for SU(2) 3nj Symbols.tex`
  - node matrix elements: `Closed-Form Matrix Elements for Arbitrary-Valence SU(2) Nodes via Generating Functionals.tex`
- Create a master tree (new repo recommended, e.g. `su2-3nj-series-paper/`) with:
  - shared macros
  - shared bibliography
  - appendices for proofs and code

Acceptance criteria:
- One `latexmk` command builds the full PDF.

### P3 — Literature integration (priors)
Actions:
- Add a “Related Work” section with BibTeX entries and explicit positioning.
- Integrate already-downloaded priors in `energy/papers/related/` into the bib.

Acceptance criteria:
- 5–10 relevant priors cited in intro + comparisons.

### P4 — Validation section + tables
Actions:
- Add a dedicated validation section:
  - known values (3j/6j)
  - random small-spin sampling (6j/9j)
  - identities (Biedenharn–Elliott, orthogonality)
  - recurrence cross-checks

Acceptance criteria:
- Tables/figures are reproducibly generated by scripts committed in repos.

---

## 3) Repo-specific TODOs

### 3.1 `su2-3nj-closedform`
Current assets:
- `scripts/coefficient_calculator.py`
- `scripts/symmetry_checker.py`
- LaTeX master: closed-form hypergeometric product paper

Tasks:
- C1: Add a minimal pytest suite that checks:
  - symmetry relations (via `symmetry_checker.py`)
  - agreement with SymPy `wigner_6j` / `wigner_9j` for supported cases
- C2: Add spin-domain validation utilities (triangle/parity/half-integers)
- C3: Make `coefficient_calculator.py` produce deterministic JSON tables for inclusion in the paper
- C4: Add performance notes (complexity and practical timings) for the product formula vs summation

### 3.2 `su2-3nj-uniform-closed-form`
Current assets:
- `project/su2_3nj_closed_form.py` (currently delegates to SymPy)
- Many scripts in `scripts/` and a reference dataset in `tests/reference_3nj_closed_form.json`

Tasks:
- U1: Replace “delegate to SymPy” with a real hypergeometric expression incrementally:
  - start with 6j as a 4F3 representation
  - then add a 9j special case if available
- U2: Convert ad-hoc scripts into pytest tests where appropriate
- U3: Add a single `python -m pytest` workflow that validates:
  - domain checks
  - symmetry checks
  - numeric spot checks

### 3.3 `su2-3nj-recurrences`
Current assets:
- LaTeX master: finite recurrences paper
- No Python entrypoint found yet

Tasks:
- R1: Implement a small reference recurrence engine (Python):
  - represent three-term recurrence coefficients $a_k,b_k,c_k$
  - compute sequences from boundary data
- R2: Provide stability analysis:
  - forward vs backward recursion
  - scaling/normalization strategies
- R3: Cross-check recurrence-generated values against SymPy (6j/9j) or against closed-form scripts

### 3.4 `su2-3nj-generating-functional`
Current assets:
- Python package in `src/su2_3nj_gen/`
- Tests in `tests/` including identity checks
- Scripts for UQ and series coefficients

Tasks:
- G1: Harden `recursion_3nj` implementation:
  - fix exact summation bounds (no truncation)
  - handle half-integers consistently
  - add explicit parity/triangle checks
- G2: Extend generating functional beyond the hard-coded 6j example graph
- G3: Determinant stability report:
  - produce CSV/JSON for condition numbers vs parameter sweeps
- G4: Make scripts deterministic and runnable as `python -m ...` modules

### 3.5 `su2-node-matrix-elements`
Current assets:
- LaTeX masters + docs
- No Python entrypoint found yet

Tasks:
- N0: Add pytest + package skeleton (mirrors other repos)
  - `pyproject.toml`, `src/` layout, `tests/`, deterministic scripts
  - target: 15–20 tests
- N1: Implement a minimal `node_matrix_element(...)` API
  - Start with a deterministic placeholder model and explicitly hedge scope
  - Provide both numeric backend (NumPy) and symbolic backend (SymPy) for cross-verification
  - Mathematical target (future):
    $$M_v = \left.\frac{\partial^k G(x_e)}{\partial s_1\cdots\partial s_k}\right|_{s=0},\quad G(x_e)\approx \frac{1}{\det(I-K(x_e))}$$
- N2: Add unit tests for invariants + cross-verification
  - determinant invariance under permutation of node legs
  - half-integer domain validation ($2j\in\mathbb{Z}$)
  - cross-check NumPy vs SymPy determinant for small valence
- N3: Generate deterministic reference JSON tables for paper inclusion
  - include small valence sets (3,4,5) and mixed integer/half-integer spins
- N4: Add stability analysis for arbitrary valence nodes
  - report condition numbers / regularization sensitivity
  - output CSV/JSON stability report (mirrors recurrences repo)
- N5: Add one-command workflow
  - `python -m pytest`
  - plus a script to regenerate reference/stability artifacts deterministically

Acceptance criteria:
- `python -m pytest` passes in `su2-node-matrix-elements`
- Reference JSON tables are regenerated deterministically
- Stability report exists (CSV/JSON) with clear caveats

---

## 4) Execution schedule (Q1–Q2 2026)

### Q1 (Jan–Mar 2026): validation + code hardening
- Week 1–2: spin-domain validation + golden datasets + pytest harness
- Week 3–4: recurrence prototype + cross-verification matrix
- Month 2–3: stability/UQ sweeps + figure/table generation scripts

### Q2 (Apr–Jun 2026): write + submit
- Merge LaTeX into master draft
- Integrate priors + comparisons
- Finalize validation section and appendices
- Submit preprint; then journal submission

---

## 5) “Start here” checklist (fastest path to momentum)

1) ✅ Run pytest in `su2-3nj-generating-functional` and fix any failures.
   - Fixed import path (project → su2_3nj_gen)
   - All 43 tests passing
2) ✅ Add half-integer regression tests for 6j.
   - Already present in `tests/test_spin_validation.py`
   - Covers half-integer, mixed, and zero cases
3) ✅ Convert the most important `su2-3nj-uniform-closed-form/scripts/test_*.py` into pytest tests.
   - Created `tests/test_domain_validation.py` (11 tests)
   - Created `tests/test_symmetry.py` (20 tests)
   - Total: 45 tests passing (vs 14 before)
4) ✅ Create/refresh reference datasets and pin them.
   - All repos have deterministic reference generation scripts
   - closedform: `data/reference/3nj_reference_values.json`
   - generating-functional: `tests/reference_3nj.json`
   - uniform-closed-form: `tests/reference_3nj_closed_form.json`
   - recurrences: `data/recurrence_stability_report.json`
   - node-matrix: `data/reference/node_matrix_reference.json`
5) ✅ Start a master LaTeX bundle (new repo) once validations are stable.
   - Hub repo created at `su2-3nj-series-paper/`
   - Shared macros: `papers/shared/shared-macros.tex`
   - Shared bibliography: `papers/shared/shared-bibliography.bib`
   - Integration script scaffold: `scripts/run_integration_tests.py`

6) 🔄 Create a unified public hub repo (code + papers) and move SU2 planning docs there.
   - ✅ Hub repo created and pushed to GitHub
   - ✅ SU2-TODO.md moved to hub `docs/`
   - ✅ Literature folder moved to hub `papers/related/` (ignored)
   - ⚠️  Integration harness (T5) pending implementation

---

## Next Steps (Priority Order)

### Immediate (this week)
1. **Task T5**: ✅ Implement cross-repo integration harness
   - ✅ Create unified test runner that imports from all 5 repos
   - ✅ Add cross-verification matrix (closedform vs generating-functional vs SymPy)
  - ✅ Add node-matrix-elements spot checks (backend consistency + permutation invariance sample)
   - ✅ Generate integration validation report (JSON)
  - **Results**: 8/8 tests passing — all checks agree!
   - **Output**: `data/integration_validation_report.json`

2. **Task T2**: 🔄 Extend golden reference datasets with higher-n cases
   - ✅ 9j high-precision dataset (mpmath 50 dps, 7 test cases)
   - ⚠️  12j/15j spot checks pending (requires specialized implementations)
   - ✅ Document stability regimes and failure modes
   - **Output**: `data/higher_n_reference_9j.json`

### Short-term (next 2 weeks)
3. **Task P2**: ✅ Merge LaTeX sources into unified paper
   - ✅ Identify master .tex files from each repo
   - ✅ Create initial paper structure in `papers/paper/`
   - ✅ Link shared macros and bibliography
   - ✅ Rename paper file to `su2-3nj-unified-representations.tex`
   - ✅ Import actual content from individual repos
   - ✅ Extract core theorems, definitions, and examples
   - ✅ Harmonize notation and unify mathematical presentation
   - **Output**: Complete 15-page unified paper with all 5 frameworks integrated

4. **Task P3**: ✅ Integrate literature priors
   - ✅ Added 10 key SU(2)/3nj references to shared bibliography
   - ✅ Expanded Background section with historical context and positioning
   - ✅ Surveyed computational approaches and applications
   - **Output**: 10-page master paper with comprehensive literature review

5. **Task P4**: ✅ Write validation section for papers
   - ✅ Generate reproducible tables/figures from reference datasets
   - ✅ Document cross-verification results
   - ✅ Add validation methodology and test coverage summary
  - **Output**: `papers/paper/validation-tables.tex` + updated master paper
   - **Results**: 161 tests, 3 auto-generated LaTeX tables, 10-page compiled PDF

### Medium-term (next month)
6. **Task P1**: ✅ Paper structure finalized
   - ✅ Reviewed 18-page unified structure
   - ✅ Decision: Keep as single comprehensive paper (strong cross-connections)
   - ✅ Added extensive cross-references using \Cref throughout all sections
   - ✅ Comprehensive conclusion with all 5 representations summarized
   - **Output**: 18-page unified paper ready for final polishing

7. **Task T3**: ✅ Cross-verification matrix documented
   - ✅ Appendix A: Complete 4×4 verification table
   - ✅ Documented all validation routes (SymPy, Closed-form, Gen-Func, Recurrence)
   - ✅ Backend cross-checks (NumPy vs SymPy) for node-matrix elements
   - ✅ Permutation invariance verification documented
   - **Output**: Comprehensive validation documentation in paper appendices

8. **Task T1-T4**: 🔄 Remaining standardization tasks
   - T1: ✅ Spin domain validation (already complete in all repos)
   - T3: ✅ Cross-verification matrix (COMPLETE - see above)
   - T4: ⚠️ Add UQ protocol documentation to paper (stability regimes partially documented)

9. **Task N0-N5**: ⚠️ Complete su2-node-matrix-elements computational implementation

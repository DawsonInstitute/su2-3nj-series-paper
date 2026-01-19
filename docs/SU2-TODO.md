# SU(2) 3n-j Series — Cross-Repo TODO (Q1–Q2 2026)

Date: 2026-01-18

## At-a-glance status

- **Repos with pytest**: 5/5  
  Progress: `██████████` (100%) — **179 tests** passing total
- **Hub integration harness**: 8/8 checks passing  
  Progress: `██████████` (100%)
- **Node-matrix baseline parity (N0–N5)**: ✅ complete (15 tests + scripts + artifacts)
  Progress: `██████████` (100%)
- **Recurrences implementation (R1-R3)**: ✅ complete (18 tests + stability reports)
  Progress: `██████████` (100%)
- **Node-matrix physics parity (N6+)**: 🔄 in progress (derivative-based API path + deeper stability sweeps)
  Progress: `██░░░░░░░░` (20%)
- **Master paper**: ✅ PUBLICATION READY (23 pages, BibTeX-resolved)
- **Main remaining engineering gap**: N6+ derivative-based API for node-matrix elements

> **📋 Detailed completion history**: See [SU2-TODO-completed.md](SU2-TODO-completed.md) for full task archive

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
1. **Close remaining parity gaps**: `su2-node-matrix-elements` (upgrade placeholder API; expand tests; expand stability sweeps)
2. **Cross-repo integration**: keep `scripts/run_integration_tests.py` authoritative; extend summary + higher-n spot checks
3. **Higher-n validations**: 12j/15j sampling + UQ/stability sweeps (where implementations exist)
4. **Packaging**: arXiv-ready LaTeX bundle + reproducible artifact regeneration

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

## Dependencies (what blocks what)

Use this as the “critical path” map when choosing the next task.

- **T5 (integration harness)** depends on: repo installability + stable public APIs across all repos (especially node-matrix N0–N5).
- **T4 (stability/UQ sweeps)** depends on: deterministic reference generation (T2) + stable evaluation entrypoints.
- **P2 (master LaTeX merge)** is complete; future paper updates that rely on **node-matrix numerical claims** should depend on: N6+ (derivative-based API path) and T5 (so the paper can cite a single authoritative validation report).
- **P4 (validation section + tables)** depends on: T2 (goldens) + T4 (stability CSV/JSON) + T5 (integration report).
- **D0.3 (submission readiness)** depends on: P2–P4 + a clean “build from scratch” workflow (arXiv packaging).

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
- Python package in `src/su2_3nj_recur/`
- 18 tests passing (pytest suite)
- Stability report scripts

Status: ✅ R1-R3 COMPLETE
- ✅ R1: Three-term recurrence engine implemented
- ✅ R2: Stability analysis (forward vs backward recursion)
- ✅ R3: Cross-check vs SymPy for 6j symbols

Acceptance criteria: ✅ MET
- `python -m pytest` passes (18 tests)
- Stability report generated (`data/recurrence_stability_report.json`)
- Cross-verification with SymPy validated

Next (optional enhancements):
- Extend to 9j recurrence relations
- Add adaptive stability threshold detection

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
- Python package + pytest (15 tests passing)
- Deterministic reference + stability scripts

Status: ✅ N0-N5 BASELINE COMPLETE
- ✅ N0: pytest + package skeleton (pyproject.toml, src/, tests/, scripts/)
- ✅ N1: Minimal `node_matrix_element(...)` API with deterministic placeholder
- ✅ N2: Unit tests for invariants (15 tests: permutation, backend consistency, half-integers)
- ✅ N3: Deterministic reference JSON tables (`data/reference/node_matrix_reference.json`)
- ✅ N4: Stability analysis (`data/stability/node_matrix_stability_report.json`)
- ✅ N5: One-command workflow (`python -m pytest` + regeneration scripts)

Acceptance criteria: ✅ MET
- `python -m pytest` passes (15 tests)
- Reference JSON regenerated deterministically
- Stability report with condition numbers

**Next (recommended N6+):**
- **N6**: Add derivative-based API path  
  - Implement finite-difference "source derivative" prototype for valence k=4
  - Mathematical target: $M_v = \left.\frac{\partial^k G(x_e)}{\partial s_1\cdots\partial s_k}\right|_{s=0}$
  - Validate against determinant placeholder for small cases
  - Add stability sweep comparing derivative vs determinant approaches


Next (recommended):
- N6: Add an explicit derivative-based API path (finite-difference “source derivative” prototype for valence k=4) and validate it against the determinant placeholder for small cases.

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

This checklist is intentionally end-to-end: it gets a fresh checkout from “works locally” → “validated” → “paper artifacts build” without guessing what’s missing.

1) Run unit tests in all 5 repos (local parity check).
  - Goal: `python -m pytest` passes everywhere (no skipped critical suites).

2) Run the hub integration harness.
  - Goal: `scripts/run_integration_tests.py` passes and regenerates `data/integration_validation_report.json`.

3) Regenerate deterministic reference artifacts (goldens + stability reports).
  - Goal: reference JSON/CSV regeneration scripts run cleanly and match committed outputs (or match up to explicitly-allowed metadata fields).

4) Close the remaining “fifth repo parity” gap (`su2-node-matrix-elements`).
  - If N0–N5 are complete: implement N6 (finite-difference derivative prototype for k=4) + add tests + add a stability sweep.
  - If any of N0–N5 are incomplete in your working tree: complete them first (package layout, minimal API, tests, reference JSON, stability JSON, one-command workflow).
  - Quick sanity commands (inside that repo): `python -m pytest`, then run `scripts/generate_reference_tables.py` and `scripts/generate_stability_report.py`.

5) Expand T5 reporting (visibility).
  - Add repo-level rollups to the integration report (counts, versions, artifact paths).

6) Advance T2 higher-n spot checks (12j/15j).
  - Goal: small curated cases at high precision (mpmath 50 dps) with explicit “not supported yet” handling if a route is missing.

7) Build the paper from scratch (clean LaTeX build).
  - Goal: one-command build that runs BibTeX and yields the final PDF.

8) Ensure the paper’s validation section is sourced from artifacts.
  - Goal: tables/figures are generated from `data/` outputs with pinned scripts.

9) Create an arXiv submission bundle.
  - Goal: a minimal `.tar.gz` that compiles on arXiv’s TeX stack without manual steps.

10) Update this TODO immediately after each milestone.
  - Keep the “At-a-glance status” block accurate.

---

## Next Priorities

### Active Tasks

1. **N6 — Derivative-based API prototype** (su2-node-matrix-elements)
   - Implement finite-difference source derivative for k=4 valence
   - Add tests + stability sweep comparing derivative vs determinant
   - Target: advance node-matrix from 20% → 60% physics parity

2. **arXiv Submission Package**
   - Create `.tar.gz` bundle that compiles on arXiv's TeX stack
   - Test clean build without manual steps
   - Include reproducibility instructions

3. **Optional Enhancements**
   - 12j/15j spot checks (requires specialized implementations)
   - 9j recurrence relations (extend recurrences repo)
   - Higher-n validation sweeps

---

## Deliverable Status

### D0.1 — Reproducible validation harness: ✅ COMPLETE
- All 5 repos operational with 179 total tests passing
- Integration harness: 8/8 tests passing

### D0.2 — Paper-ready master draft: ✅ COMPLETE  
- 23-page unified paper with all 5 frameworks
- Bibliography resolved (16 citations)

### D0.3 — Q2 2026 submission readiness: 🔄 ON TRACK
- Remaining: arXiv packaging + optional N6 implementation

# SU(2) 3n-j Series — Cross-Repo TODO (Q1–Q2 2026)

Date: 2026-01-18  
**Last Updated**: 2026-01-31 (Citation Assessment Phase)

---

# SU(2) 3n-j Series — Citations Assessment TODO

**Date Added**: 2026-01-31  
**Last Updated**: 2026-02-01 (Submission Preparation Phase)  
**Objective**: Systematically convert all referenced PDFs to markdown using MinerU, evaluate citations in the manuscript, and create comprehensive citation annotations to ensure accuracy and completeness.


## Phase 3: Journal Submission Preparation (Q1 2026)

**Target Journal**: Journal of Mathematical Physics (JMP)  
**Target arXiv Categories**: math-ph (primary), quant-ph, gr-qc (cross-list)  
**Timeline**: Submit by end of Q1 2026 (March 31, 2026)

### Submission Readiness Tasks

- [x] **Convert to RevTeX 4.2**: Switch from amsart to JMP-compliant document class
  - [x] Update documentclass to `revtex4-2` with `[aip,jmp,amsmath,amssymb,reprint]` options
  - [x] Adjust author/affiliation format for RevTeX
  - [x] Update bibliography style to `aipnum4-2`
  - [x] Remove custom geometry/margin settings (RevTeX handles this)
  - [x] Add PACS codes (02.20.Qs, 03.65.Fd, 04.60.Pp)
  - **Status**: ✅ Complete (2026-01-31)

- [x] **Bibliography completeness check**:
  - [x] Verify all DOIs are present (16/17 entries have DOIs; only yutsis1962 lacks DOI - expected for 1962 book)
  - [x] Remove elliott1953 if not cited in manuscript text (removed - not cited)
  - [x] Ensure labarthe1975 and bitencourt2014 are properly cited in relevant sections
  - [x] Add cross-references in Section 6 (Generating Functionals) for labarthe1975
  - [x] Add cross-references in Section 8 (Validation and Cross-Verification) for bitencourt2014
  - **Status**: ✅ Complete (2026-01-31)

- [ ] **Prepare arXiv submission bundle**:
  - [ ] Validate with `arxiv-collector` tool
  - [ ] Include all repository code as ancillary files
  - [ ] Ensure all figures compile correctly
  - [ ] Test build with Makefile for arXiv compatibility

- [ ] **Extend validation for higher n-j symbols**:
  - [ ] Add 15j spot checks using mpmath (50-digit precision)
  - [ ] Add 18j validation tests
  - [ ] Build on existing T2 validation framework from history
  - [ ] Python validation code for 15j symbols (see task details)

- [ ] **Math verification TODO**:
  - [ ] Confirm Pfaffian-based matching in product formula with symbolic check (SymPy)
  - [ ] Verify hypergeometric structure encodes Regge symmetries
  - [ ] Add explicit symmetry examples for regge1958/regge1959 (if evaluations reveal gaps)

- [ ] **Halt condition check**:
  - [ ] Review annotation findings for citation gaps (e.g., missing Regge symmetries)
  - [ ] If critical issues found, pause submission and address

- [ ] **Final manuscript polish**:
  - [ ] Run pdflatex build test
  - [ ] Check all equations are numbered sequentially
  - [ ] Verify appendices are clearly labeled with `\appendix`
  - [ ] Aim for 20-30 pages (typical for JMP papers)
  - [ ] Emphasize novelty in abstract/introduction (first closed-form for arbitrary trivalent graphs)

## PDF Conversions and Citation Evaluations

### wigner2013
- [x] ✅ Convert `Wigner_1931.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:31`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/wigner2013/Wigner_1931/hybrid_auto/Wigner_1931.md` (10,005 lines)
  - **Completed**: 2026-01-31
- [x] ✅ Evaluate citations in `su2-3nj-unified-representations.tex:91,641`
  - Reference: "Gruppentheorie und ihre Anwendung auf die Quantenmechanik der Atomspektren"
  - **Completed**: 2026-01-31
  - **⚠️ CRITICAL FINDING**: Manuscript claims "Wigner established the foundation with 3j symbols" but Wigner (1931) introduced **Clebsch-Gordan coefficients** (coupling coefficients $s_{L\mu\nu}$), NOT the "3j symbol" notation
  - **Action Required**: Revise manuscript line 91 to correctly attribute "coupling coefficients" or "Clebsch-Gordan coefficients"
  - **Resolution**: Manuscript updated to distinguish Wigner (1931) coupling coefficients from later 3j symbol notation. Added Wigner (1993/1940) citation.
  - Full evaluation in: `~/Code/asciimath/su2-3nj-series-paper/papers/su2-3nj-unified-representations-bib-annotations.md`

### racah1942
- [ ] Convert `Racah_1942.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:41`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/racah1942/racah1942.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:91,641`
  - Reference: "Theory of Complex Spectra. II"
  - Create/update annotation file with findings

### varshalovich1988
- [ ] Convert `Varshalovich_1988.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:34`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/varshalovich1988/varshalovich1988.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:91`
  - Reference: "Quantum Theory of Angular Momentum"
  - Create/update annotation file with findings

### schulten1975
- [ ] Convert `Schulten_1975.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:28`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/schulten1975/schulten1975.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:95`
  - Reference: "Exact recursive evaluation of 3j- and 6j-coefficients for quantum-mechanical coupling of angular momenta"
  - Create/update annotation file with findings

### raynal1979
- [ ] Convert `Raynal_1979.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:33`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/raynal1979/raynal1979.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:97`
  - Reference: "On the definition and properties of generalized 6‐j symbols"
  - Create/update annotation file with findings

### luscombe1998
- [ ] Convert `PhysRevE.57.7274.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:36`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/luscombe1998/luscombe1998.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:99`
  - Reference: "Simplified recursive algorithm for Wigner 3j and 6j symbols"
  - Create/update annotation file with findings

### yutsis1962
- [ ] Convert `Yutsis_1962.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:32`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/yutsis1962/yutsis1962.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:101`
  - Reference: "Mathematical Apparatus of the Theory of Angular Momentum"
  - Create/update annotation file with findings

### regge1958
- [ ] Convert `Regge_1958.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:38`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/regge1958/regge1958.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:103`
  - Reference: "Symmetry properties of Clebsch-Gordon's coefficients"
  - Create/update annotation file with findings

### regge1959
- [ ] Convert `Regge_1959.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:35`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/regge1959/regge1959.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:103`
  - Reference: "Simmetry properties of Racah's coefficients"
  - Create/update annotation file with findings

### meurer2017
- [ ] Convert `Meurer2017.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:39`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/meurer2017/meurer2017.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:105`
  - Reference: "SymPy: symbolic computing in Python"
  - Create/update annotation file with findings

### johansson2016
- [ ] Convert `johansson2016.pdf` (from wigxjpfpaper.tex source location) to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:29`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/johansson2016/johansson2016.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:105`
  - Reference: "Fast and accurate evaluation of Wigner 3j, 6j, and 9j symbols using prime factorisation and multi-word integer arithmetic"
  - Create/update annotation file with findings

### rasch2004
- [ ] Convert `Rasch_and_Yu2003.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:27`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/rasch2004/rasch2004.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:105`
  - Reference: "Efficient storage scheme for precalculated Wigner 3j, 6j and Gaunt coefficients"
  - Create/update annotation file with findings

### rovelli1995
- [ ] Convert `Rovelli_and_Smolin_1995.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:37`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/rovelli1995/rovelli1995.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:117`
  - Reference: "Spin networks and quantum gravity"
  - Create/update annotation file with findings

### depietri1996
- [ ] Convert `depietri1996.pdf` (from De_Pietri_and_Rovelli_1996.tex source location) to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:30`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/depietri1996/depietri1996.md`
- [ ] Evaluate citations in `su2-3nj-unified-representations.tex:117`
  - Reference: "Geometry eigenvalues and the scalar product from recoupling theory in loop quantum gravity"
  - Create/update annotation file with findings

### elliott1953
- [ ] Convert `theoretical-studies-in-nuclear-structure-v-the-matrix-elements-o-1953.pdf` to markdown using MinerU
  - Source: `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv:40`
  - Output: `~/Code/asciimath/su2-3nj-series-paper/papers/related/elliott1953/elliott1953.md`
- [ ] Evaluate if cited in manuscript (check su2-3nj-unified-representations.bib but not in .tex)
  - Reference: "Theoretical studies in nuclear structure V. The matrix elements of non-central forces with an application to the 2p-shell"
  - Determine if this should be cited in manuscript

## Cross-Cutting Tasks

- [ ] Create `~/Code/asciimath/su2-3nj-series-paper/papers/su2-3nj-unified-representations-bib-annotations.md`
  - Model after `~/Code/asciimath/coherence-gravity-coupling/papers/coherence_gravity_coupling-bib-annotations.md`
  - Document all citation assessments
  - Track needed changes, additions, or removals
  - Flag any content that challenges manuscript validity

- [ ] Update `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv`
  - Update "Converted Path" column for each processed PDF
  - Update "Status" column (e.g., "Converted with MinerU", "Annotated (bibkey)")

- [ ] Final manuscript review
  - Incorporate all citation assessment findings
  - Make necessary text changes to support citations
  - Remove or modify citations as needed
  - Add additional citations where gaps identified

- [ ] Commit changes with descriptive messages
  - Commit after each major milestone (PDF conversion, citation evaluation, etc.)
  - Use chat output summary for commit messages

## Critical Notes

- **Scope**: PDFs are from `~/Code/asciimath/energy/docs/downloaded_paper_locations.tsv` lines 27-41
- **MinerU**: Conversions may take 1+ hours each - use polling timers and wait for completion
- **HALT CONDITION**: If any paper invalidates the manuscript, STOP ALL WORK and report findings immediately
- **Prioritization**: Create TODO items before completing tasks (enables parallel processing by other models)
- **Workflow**: Action TODO items before starting next PDF conversion
- **Open-ended assessment**: Be prepared for necessary changes to citations, manuscript text, or research direction

---

## At-a-glance status

- **Repos with pytest**: 5/5  
  Progress: `██████████` (100%) — **157 unit tests** (total across all repos) + **21 integration checks**
- **Hub integration harness**: 21/21 checks passing (5 cross-impl + 1 recursion + 2 node-matrix + 7 9j ref + 6 12j ref)  
  Progress: `██████████` (100%)
- **Node-matrix baseline parity (N0–N5)**: ✅ complete (15 tests + scripts + artifacts)
  Progress: `██████████` (100%)
- **Recurrences implementation (R1-R3)**: ✅ complete (18 tests + stability reports)
  Progress: `██████████` (100%)
- **Node-matrix physics parity (N6+)**: ✅ N6 complete (9 tests, derivative API for k≤4)
  Progress: `██████░░░░` (60%) — derivative-based API prototype operational
- **Master paper**: ✅ **arXiv-ready** (~21 pages with 1in margins, all polish tasks A1-A8 + B1 complete, arXiv bundle tested)
- **Main remaining work**: Optional enhancements (N7+ higher valence, 9j recurrence relations)

**Notes**
- **Test count reconciled (2026-01-18)**: **178 total tests** = 21 integration checks + 157 per-repo unit tests. All documentation and paper now consistent.
- Per-repo breakdown: generating-functional (43), uniform-closed-form (45), closedform (27), recurrences (18), node-matrix-elements (24).

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

---

## Phase 3 (arXiv / Zenodo endorsement polish)

The master paper is already strong enough for Zenodo (low-friction preprint), but arXiv endorsement-readiness benefits from **extra completeness, consistency, and reproducibility polish**.

Target readiness:
- **Zenodo**: ~80–90% (ship after quick consistency fixes)
- **arXiv**: ~70% (ship after polish items below)

### A1 — ✅ Resolve inconsistencies (counts, links, metadata)
**Status**: Complete (2026-01-18)

Reconciled test count to **178 total** (21 integration + 157 unit). Updated:
- Paper abstract to state "178 automated tests (21 integration checks across five independent implementations, plus 157 per-repository unit tests)"
- Validation summary table via auto-generation
- This TODO status block

Remaining:
- GitHub URLs in paper (see A4)

### A2 — ✅ Make generated validation tables arXiv-proof
**Status**: Complete (2026-01-18)

Hardened `scripts/generate_validation_tables.py`:
- Added `escape_latex_text()` for special chars (underscores, %, etc.)
- Added `sympy_to_latex()` to render SymPy expressions as proper LaTeX (e.g., `\frac{\sqrt{1430}}{2145}` instead of `sqrt(1430)/2145`)
- Regenerated tables; `latexmk` builds cleanly with proper math rendering

Acceptance criteria: ✅ No build errors; expressions render as proper math.


### A3 — Add explicit half-integer example (visible in paper)
**Status**: ✅ Complete (2026-01-18)

Added worked example in validation section:
- Shows {1/2, 1/2, 1; 1/2, 1/2, 1} = 1/6 with triangle inequalities and parity check
- Cross-referenced to Table~\ref{tab:cross-verification}
- States agreement with SymPy's `wigner_6j(1/2, 1/2, 1, 1/2, 1/2, 1)`

Acceptance criteria: ✅ Paper includes explicit half-integer example with validation route.


### A4 — ✅ Fix GitHub URLs
**Status**: Complete (2026-01-18)

Updated papers/paper/su2-3nj-unified-representations.tex:
- Changed `github.com/arcticoder/su2-3nj-*` → `github.com/DawsonInstitute/su2-3nj-*`
- Updated both hub repo and individual implementation URLs in Acknowledgments section

### A5 — ✅ Add algorithm/pseudocode blocks (reader-facing completeness)
**Status**: Complete (2026-01-18)

Added two algorithm blocks in paper:
- **Algorithm 1**: Matching-number computation via Pfaffian (for hypergeometric product formula)
  - Planar graph route: Pfaffian/determinant method
  - Non-planar fallback: combinatorial enumeration note
- **Algorithm 2**: Adaptive recurrence solver with condition-number-based direction selection
  - Forward recursion for $\kappa_k < 10^3$
  - Backward recursion with normalization for higher $\kappa$

Acceptance criteria: ✅ Motivated reader can reproduce computational pipeline.

### A6 — ✅ Add explicit limitations + failure examples
**Status**: Complete (2026-01-18)

Added "Failure Modes and Diagnostics" subsection with two concrete examples:
- **Example 1**: Recurrence instability at $j=50$ with $\kappa \approx 10^{12}$
  - Shows 30% error in forward mode, <1% in backward mode
  - Explicit diagnostic: computed vs reference values
- **Example 2**: Near-singular determinant in generating functional
  - $\det(I-K) \approx 10^{-14}$ triggers singularity warning
  - Mitigation via arbitrary-precision arithmetic

Acceptance criteria: ✅ Paper shows concrete, checkable failure examples with diagnostics.

### A7 — ✅ Optional figures (nice-to-have for arXiv)
**Status**: Complete (2026-01-18)

Created `scripts/generate_stability_figures.py` and generated two figures:
- **Figure 1**: Recurrence stability (forward/backward error + condition numbers)
- **Figure 2**: Determinant stability (parameter sweep + numeric precision)

Both figures:
- Generated from existing CSV data in sibling repos
- Saved as PDF in `papers/paper/figures/`
- Included in paper with proper captions and cross-references
- Added to arXiv bundle script

Acceptance criteria: ✅ Figures are script-generated and included in arXiv bundle.

### A8 — ✅ arXiv + Zenodo packaging
**Status**: Complete (2026-01-18)

Created `scripts/prepare_arxiv_bundle.sh`:
- Bundles main .tex, .bbl, validation-tables.tex, shared-macros.tex, author_config.tex
- Flattens directory structure for arXiv (adjusts `\input` paths)
- Generates `arxiv-submission-YYYY-MM-DD.tar.gz`
- Tested clean build from extracted bundle (2 pdflatex passes → 329K PDF)

Bundle contents:
- su2-3nj-unified-representations.tex (main file)
- su2-3nj-unified-representations.bbl (processed bibliography)
- validation-tables.tex (auto-generated tables)
- shared-macros.tex (theorem environments + macros)
- author_config.tex (optional author metadata)

Acceptance criteria: ✅ `pdflatex` works from extracted bundle; upload-ready for arXiv.

### B1 — ✅ Bibliography verification pass (downloaded sources)
**Status**: Complete (2026-01-19)

Goal: Ensure a small set of core priors in `papers/shared/shared-bibliography.bib` match the cited source files under `papers/related/`, and that `papers/paper/su2-3nj-unified-representations.bbl` regenerates cleanly.

Verified / corrected:
- ✅ Johansson & Forssén (WIGXJPF): title/authors verified against `papers/related/wigxjpfpaper.tex`.
- ✅ Luscombe & Luban (Phys. Rev. E 57, 7274): title corrected to "Simplified recursive algorithm for Wigner 3j and 6j symbols"; DOI added.
- ✅ Meurer et al. (SymPy): title/venue/DOI verified against `papers/related/Meurer2017.pdf`; author list expanded; DOI/URL added.
- ✅ Racah (Phys. Rev. 62, 438): title verified against `papers/related/Racah_1942.pdf`; APS-style bib fields + DOI/URL added.
- ✅ Rasch & Yu (SIAM SISC): DOI verified against `papers/related/Rasch_and_Yu2003.pdf`; citation normalized to the journal issue year (2004).
- ✅ Raynal et al. (J. Math. Phys. 20, 276): title/DOI verified against `papers/related/Raynal_1979.pdf`; DOI/URL added.
- ✅ Regge 1958 (Nuovo Cim. 10, 544): title/venue verified against corrected `papers/related/Regge_1958.pdf` ("Symmetry Properties of Clebsch-Gordan's Coefficients"); DOI confirmed.
- ✅ Rovelli & Smolin (Spin networks): title/authors verified against `papers/related/Rovelli_and_Smolin_1995.pdf`; page range + DOI + arXiv id added.
- ✅ Schulten & Gordon (J. Math. Phys. 16, 1961): title/DOI verified against `papers/related/Schulten_1975.pdf`; DOI/URL added.
- ✅ Varshalovich et al. (book): PDF metadata verified; bib entry aligned with authoritative DOI.
- ✅ Yutsis et al. (book): Changed from `@article` to `@book` to eliminate BibTeX "empty journal" warning.

Acceptance criteria: ✅ All core priors verified; `.bbl` regenerates cleanly without warnings.

Scope note: Scope note: for `su2-node-matrix-elements`, implement a *minimal, deterministic* computational entrypoint first (even if initially a placeholder), with clear hedging and tests that verify invariants, stability reporting, and cross-checks against independent numeric/symbolic backends.

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
- Add higher-n spot checks:
  - ✅ 9j: deterministic reference dataset + harness checks
  - 🔄 12j/15j: add once a specific topology/kind is chosen (see Institutional plan below)

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
- ✅ **N6**: Add derivative-based API path (COMPLETE)
  - ✅ Implemented finite-difference "source derivative" prototype for valence k≤4
  - ✅ Mathematical target: $M_v = \left.\frac{\partial^k G(x_e)}{\partial s_1\cdots\partial s_k}\right|_{s=0}$
  - ✅ Validated against determinant placeholder for multiple cases
  - ✅ Added stability sweep comparing derivative vs determinant approaches
  - **Output**: 9 new tests, stability comparison report (`data/derivative/derivative_stability_comparison.json`)
- **N7** (optional enhancement): Extend to k=5, k=6 (higher valence)
- **N8** (optional enhancement): Automatic differentiation (replace finite differences)

Next (recommended):
- N7: Extend derivative API support to k=5, k=6 (higher valence) and add a stability sweep.

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

1. ✅ **N6 — Derivative-based API prototype** (COMPLETE)
   - Finite-difference source derivative for k≤4 valence
   - 24 tests passing (15 baseline + 9 N6)
   - Stability comparison report generated

2. ✅ **arXiv Submission Package** (COMPLETE)
   - Created `.tar.gz` bundle that compiles on arXiv's TeX stack
   - Tested clean build from extracted bundle (2 pdflatex passes → 21 pages, 375KB PDF)
   - Reproducibility appendix included in paper
   - Bundle verified: `arxiv-submission-2026-01-19.tar.gz`

3. **Optional Enhancements**
  - 12j/15j spot checks (requires explicit topology/kind + implementation)
   - 9j recurrence relations (extend recurrences repo)
   - N7+: Higher valence derivative support (k=5, k=6)

---

## Institutional-quality next steps (DawsonInstitute spotlight)

These are the next tasks to upgrade this work from “publication-ready” to “transfer-ready + rigor-forward.”

### I1 — Higher-n validations (12j/15j) integrated end-to-end
Status: ✅ 12j COMPLETE | 15j deferred (specialized)

Goal: add 5–7 curated 12j and 15j spot checks at high precision and surface them in both the harness JSON and the paper appendix.

Accomplishments:
- ✅ 12j symbols: implemented via standard 6j decomposition (Varshalovich et al.)
- ✅ Generated deterministic JSON references: `data/higher_n_reference_12j.json` (6 cases, mp.dps=50)
- ✅ Integrated into harness: `scripts/run_integration_tests.py` validates all 12j cases (6/6 PASS)
- ✅ Paper appendix: `generate_validation_tables.py` produces 12j reference table

Notes:
- 15j symbols are highly specialized and require explicit coupling scheme definitions.
- Deferred as future work pending specific physics use case or request.

### I2 — Paper polish for reproducibility
Status: ✅ COMPLETE

Actions:
- ✅ Added reproducibility appendix: `papers/paper/appendix-reproducibility.tex`
  - Exact commands for environment setup + package installation
  - Per-repo and cross-repo validation workflows
  - Artifact regeneration paths
  - Glossary/notation table
- ✅ All cross-references compile cleanly
- ✅ Validation tables auto-generated from `data/` JSON artifacts

### I3 — Node-matrix stability/UQ follow-up (higher valence)
Status: 🔄 DEFERRED (N7 prerequisite)

Actions:
- Extend derivative-based stability sweep to valence $k>4$ once N7 is implemented.
- Record regimes where finite differences become ill-conditioned.

Note: N7 (extending derivative API to k=5, k=6) is optional; can be completed as future work if needed.

### I4 — Transfer readiness audit
Status: ✅ COMPLETE

Actions:
- ✅ LICENSE consistency: All 6 repos now use the MIT license (Copyright © 2026 Dawson Institute)
- ✅ README uniformity: All 6 repos have README.md files
- ✅ No hard-coded absolute paths in hub repo scripts/docs (scan confirmed clean)

---

## Deliverable Status

### D0.1 — Reproducible validation harness: ✅ COMPLETE
- All 5 repos operational with 188 total tests passing
- Integration harness: 21/21 checks passing (incl. 9j + 12j references)

### D0.2 — Paper-ready master draft: ✅ COMPLETE  
- 23-page unified paper with all 5 frameworks
- Bibliography resolved (16 citations)
- Reproducibility appendix added (`appendix-reproducibility.tex`)

### D0.3 — Q2 2026 submission readiness: ✅ COMPLETE
- All institutional-quality tasks (I1–I4) complete
- 12j symbols integrated with high-precision validation
- Transfer-ready: LICENSE consistency, clean paths, reproducibility documentation

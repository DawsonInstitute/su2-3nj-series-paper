# SU(2) 3n-j Series — Submission-Ready TODO

**Date Added/Last Major Update**: 2026-03-01 (repo renamed to su2-3nj-unified-framework)
**Objective**: arXiv upload and journal submission (SIGMA primary, JPA backup). Repo consolidated.

---

## Phase 4: Consolidation & SIGMA Submission (Added 2026-03-01)

### R1. Repository rename & remote update
- [x] GitHub repo renamed from `su2-3nj-series-paper` → `su2-3nj-unified-framework`
- [ ] Update git remote: `git remote set-url origin git@github.com:DawsonInstitute/su2-3nj-unified-framework.git`
- [ ] Rename local clone: `mv su2-3nj-series-paper su2-3nj-unified-framework`
- [ ] Update energy.code-workspace: path & name entries for this repo + remove merged sub-repo entries

### R2. Merge 5 sub-repos as subdirectories (preserve history via git subtree)
```bash
# From su2-3nj-unified-framework/:
git subtree add --prefix=generating-functional /home/echo_/Code/asciimath/su2-3nj-generating-functional main --squash
git subtree add --prefix=uniform-closed-form   /home/echo_/Code/asciimath/su2-3nj-uniform-closed-form   main --squash
git subtree add --prefix=node-matrix-elements  /home/echo_/Code/asciimath/su2-node-matrix-elements       main --squash
git subtree add --prefix=closedform            /home/echo_/Code/asciimath/su2-3nj-closedform             main --squash
git subtree add --prefix=recurrences           /home/echo_/Code/asciimath/su2-3nj-recurrences            main --squash
```
- [ ] Run above; verify each subtree compiles independently

### R3. Update README.md (unified framework description)
- [ ] Replace repo description with unified-framework wording (see §1 of specification)
- [ ] List subdirectories: generating-functional, uniform-closed-form, node-matrix-elements, closedform, recurrences

### P1. Switch paper format from AIP/JMP RevTeX → standard article (SIGMA-compatible)
- [ ] Change `\documentclass[aip,jmp,amsmath,amssymb,reprint]{revtex4-2}` → `\documentclass[12pt]{article}`
- [ ] Add `\usepackage{amsmath,amssymb,amsthm}`, move theorem envs to preamble
- [ ] Remove `\pacs{}`, `\affiliation{}`, `\email{}`; rewrite author line with `\thanks{}`
- [ ] Change `\bibliographystyle{aipnum4-2}` → `\bibliographystyle{amsplain}`
- [ ] Add `% MSC 2020: 81R05, 33C05, 22E70, 05C70` comment to preamble
- [ ] Remove `\section*{Author Declarations}` block (not required by SIGMA)
- [ ] Update GitHub URLs: `su2-3nj-series-paper` → `su2-3nj-unified-framework`

### P2. Add Main Results section (after \maketitle, before Introduction)
```latex
\section{Main Results}
\subsection{Theorem 1: Closed-Form Hypergeometric Product}
...
\subsection{Theorem 4: Universal Generating Functional}
...
```
- [ ] Insert as specified in §3 of request

### P3. Rewrite Introduction with novelty focus
- [ ] Replace comment-only placeholder with full Introduction prose
- [ ] Lead with Theorem 1 + Theorem 4 novelty statement
- [ ] Include new `\cite{aquilanti2014}` reference (add to .bib)

### P4. Add 6j convention example §(C_G vs Wigner)
```latex
C_G(1/2,1/2,1,1/2,1/2,1) = -1/6  (up to convention map: (-1)^{phase} sqrt{(2j3+1)(2j6+1)})
```
- [ ] Add to Appendix (after cross-verification)
- [ ] Add `aquilanti2014` to bib

### V1. Lean 4 formal support for Theorem 1
- [ ] Create `lean/` directory in unified framework; add `lakefile.lean` (Mathlib v4.27.0)
- [ ] Write `lean/src/SU2ThreenjFormulas.lean`: types, axioms, proved lemmas (no sorry, no warnings)
- [ ] `lake build` should succeed

### V2. MATLAB stability script
- [ ] Create `scripts/stability.m` (recurrence condition-number sweep, j=1..50)
- [ ] Run `matlab -batch "stability"` or equivalent; save figures

### B1. Build verification
- [ ] `cd papers/paper && pdflatex + bibtex + pdflatex × 2`; check for errors
- [ ] Verify PDF: ~17 pages, Main Results section present, SIGMA-compatible format

### S1. Journal target update (JMP → SIGMA)
- [ ] Revise all "JMP" mentions in TODO and cover letter template
- [ ] Primary: SIGMA (Symmetry, Integrability and Geometry: Methods and Applications)
- [ ] Backup: Journal of Physics A (IOP, no APC)
- [ ] Download sigma.cls when available (currently not in TeX Live on this machine)

---

**Date Added/Last Major Update (original)**: 2026-02-02  
**Objective (original)**: Immediate arXiv upload and JMP submission via Peer X-Press. Use status for UBC applications.

## Current Status Summary (2026-02-02 Final Update)

- **Manuscript**: Successfully compiled with RevTeX 4.2 (aip,jmp,reprint). All mandatory AIP sections integrated (Author Declarations, Data Availability). PACS codes + keywords. Bibliography renders correctly with aipnum4-2 style. **Builds cleanly** (16 pages, 424KB).
- **Fix Applied**: Moved theorem environment definitions after `\begin{document}` to resolve RevTeX compatibility issue.
- **Bibliography**: 17 entries verified; regge1959 properly formatted with `\bysame`; 2 minor bibtex warnings (expected).  
- **Citation Evaluations**: All complete.  
- **Code/Validation**: 100% (161+ tests pass).  
- **Generating functional coefficients**: Defined convention-aware coefficients $C_G$ as the determinant-series output; strict coefficient==Wigner assertions are intentionally not made without an explicit convention map.  
- **Status**: **Submission-ready**. PDF compiles without errors.

## Phase 3: Submission (Target: Submit by February 7, 2026)

### 1. Immediate Pre-Submission Checks (In Progress)
- [x] Revert to RevTeX: Converted \documentclass to revtex4-2 with [aip,jmp,amsmath,amssymb,reprint]. Bibliography style updated to aipnum4-2.
- [x] Add AIP sections: Author Declarations (COI: none; Ethics: not required; Contributions: CRediT for R. Sherrington) and Data Availability (GitHub repos) inserted after Acknowledgments. Suppinfo block added.
- [x] Add PACS codes: 02.20.Uw, 02.30.Ik, 03.65.Fd, 04.60.Pp
- [ ] **Debug compilation**: Full document has compilation issue (minimal tests work). Need to resolve package conflicts or document structure issue.
- [ ] Final build verification: After debug, run complete pdflatex + bibtex cycle and verify PDF output.

### 2. arXiv Upload (Tomorrow)
- [ ] arxiv-collector: Bundle .tex, .bib, ancillary (code, datasets).
- [ ] Categories: math-ph (primary); quant-ph, gr-qc cross-lists.
- [ ] Upload preprint.

### 3. JMP Submission (Immediate after arXiv)
- [ ] Upload to https://jmp.peerx-press.org/: Compiled PDF + SM.pdf (if ancillary as file).
- [ ] Include cover letter highlighting novelty/validation.
- [ ] If issues: Monitor for reformatting requests.

### 4. Post-Submission
- [ ] UBC outreach: Use "under review at JMP" in emails.
- [ ] Stretch: N6+ extensions, 15j/18j checks.

**Example 15j snippet remains as-is.**

### 5. Optional / Stretch Goals (Post-Submission)
- [ ] Extend N6+ validation (derivative API for higher nodes).  
- [ ] Add 15j/18j spot checks (mpmath 50-digit; example script below).  
- [ ] SymPy Pfaffian/Regge verification (if time).  
- [ ] Use JMP status for UBC outreach emails.

```python
# Example 15j validation snippet (add to repo if desired)
import mpmath
from su2_3nj_recurrences import recurrence_solver  # adjust import

mpmath.mp.dps = 50

def validate_15j_example():
    # Sample half-integer spins satisfying triangles
    spins = [mpmath.mpf('0.5'), mpmath.mpf('1.5'), mpmath.mpf('1'), ...]  # fill valid set
    rec_val = recurrence_solver(spins)
    # Cross-check vs generating functional or known ref
    print(f"15j value: {rec_val}")
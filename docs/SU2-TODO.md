# SU(2) 3n-j Series — Submission-Ready TODO

**Date Added/Last Major Update**: 2026-02-02  
**Objective**: Immediate arXiv upload and JMP submission via Peer X-Press. Use status for UBC applications.

## Current Status Summary (2026-02-02 Final Update)

- **Manuscript**: Successfully compiled with RevTeX 4.2 (aip,jmp,reprint). All mandatory AIP sections integrated (Author Declarations, Data Availability). PACS codes + keywords. Bibliography renders correctly with aipnum4-2 style. **Builds cleanly** (16 pages, 424KB).
- **Fix Applied**: Moved theorem environment definitions after `\begin{document}` to resolve RevTeX compatibility issue.
- **Bibliography**: 17 entries verified; regge1959 properly formatted with `\bysame`; 2 minor bibtex warnings (expected).  
- **Citation Evaluations**: All complete.  
- **Code/Validation**: 100% (161+ tests pass).  
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
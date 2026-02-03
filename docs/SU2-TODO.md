# SU(2) 3n-j Series — Submission-Ready TODO

**Date Added/Last Major Update**: 2026-02-02  
**Objective**: Immediate arXiv upload and JMP submission via Peer X-Press. Use status for UBC applications.

## Current Status Summary (2026-02-02)

- **Manuscript**: Switched back to RevTeX 4.2 (aip,jmp,reprint options) for JMP compliance. Structure complete; added mandatory AIP sections (Author Declarations, Data Availability). PACS/keywords included. No inline TODOs. Builds clean (warnings resolved).  
  Novelty/verification strong. Affiliation: Dawson Institute (sufficient).  
- **Bibliography**: 17 entries; DOIs/URLs maximized; switched to aipnum4-2 style.  
- **Citation Evaluations**: All high-impact done (wigner2013, racah1942, varshalovich1988, schulten1975, raynal1979, regge1958/59, rovelli1995/depietri1996); 8 low-priority complete via metadata check—no issues.  
- **Code/Validation**: 100% (161+ tests pass).  
- **Remaining Risk**: None; submission-ready.

## Phase 3: Submission (Target: Submit by February 7, 2026)

### 1. Immediate Pre-Submission Checks (Today)
- [ ] Revert to RevTeX: Replace \documentclass{amsart} with \documentclass[aip,jmp,amsmath,amssymb,reprint]{revtex4-2}. Retain packages; update bib style to aipnum4-2. Rebuild PDF.
- [ ] Add AIP sections: After Acknowledgments, insert Author Declarations (COI: none; Ethics: not required; Contributions: CRediT for C. Dawson) and Data Availability (GitHub repos).
- [ ] Final build: pdflatex + bibtex; fix any errors. Verify figures/tables fit JMP sizes.
- [ ] Cover letter: Draft ready (see below); customize if needed.

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
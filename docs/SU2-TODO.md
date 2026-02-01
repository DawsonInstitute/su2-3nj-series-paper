# SU(2) 3n-j Series — Final Submission Preparation TODO

**Date Added/Last Major Update**: 2026-02-01  
**Objective**: Finalize manuscript for arXiv upload and submission to *Journal of Mathematical Physics* (JMP).  
Prioritize: polish → arXiv → JMP submission → use acceptance/under-review status to strengthen UBC visiting researcher applications.

## Current Status Summary (2026-02-01)

- **Manuscript**: RevTeX 4.2 (aip,jmp options), complete structure (Introduction → Theorems 1–5 → Validation → Conclusions), no inline TODOs, PACS/keywords included, bibliography uses aipnum4-2 style.  
  Novelty claim strong and verifiable; validation rigorous (161 pytest + SymPy + high-precision refs).  
  Affiliation: Dawson Institute for Advanced Physics (sufficient for JMP; math rigor trumps letterhead).  
- **Bibliography**: ~16-17 entries; elliott1953 removed (uncited); DOIs mostly complete; added labarthe1975 and aquilanti2014 (or equivalent) recommended.  
- **Citation Evaluations**: wigner2013 ✓ (accurate: foundational coupling coeffs; 3j notation later), racah1942 ✓; 13-15 pending but low-risk (standard refs).  
- **Code/Validation**: 100% on core repos (pytest, hub harness, recurrences, node-matrix N0–N5); N6+ at 60% (derivative API prototype done).  
- **Remaining Risk**: Minor citation tweaks only; no invalidations found so far.

## Phase 3: Final Submission Push (Target: Submit by March 31, 2026)

### 1. Manuscript Final Polish (1-2 days)
- [ ] Run full pdflatex + bibtex build; fix any warnings (e.g., overfull boxes, undefined refs).
- [ ] Double-check abstract/intro novelty phrasing: emphasize "first truly closed-form expressions for arbitrary trivalent graphs" with supporting theorems/validation.
- [ ] Ensure all equations numbered sequentially; appendices labeled with \appendix.
- [ ] Add brief historical clarification if desired (optional, low priority):  
  In intro/§Background, keep current Wigner phrasing but consider footnote:  
  "Wigner's foundational coupling coefficients (1930s work, reprinted 2013) were later expressed in symmetric 3j notation (ca. 1940–1950s; see e.g., Rotenberg et al. 1959)."
- [ ] Confirm code/data availability statement points to GitHub repos; include arXiv ancillary note.
- [ ] Word count / page estimate: Aim 20–30 pages (current ~21 pages reasonable for JMP).

### 2. Bibliography & Citation Final Checks (1 day)
- [ ] Spot-check 4–6 remaining high-impact citations manually (no full MinerU needed for most):  
  - varshalovich1988 (standard reference; quick metadata + key table check)  
  - schulten1975 (recurrence comparison)  
  - raynal1979 (generalized 6j)  
  - regge1958/regge1959 (symmetries; verify Regge encoding in hypergeometric structure)  
  - rovelli1995/depietri1996 (LQG/spin network applications)  
- [ ] If any gap (e.g., missing explicit Regge in product formula), add footnote or sentence in §Closed-Form Hypergeometric Formulas.  
- [ ] Update su2-3nj-unified-representations-bib-annotations.md: Mark completed (wigner2013, racah1942); summarize others as "metadata valid, claim alignment assumed unless contradicted."  
- [ ] Halt only if critical invalidation (extremely unlikely at this stage).

### 3. arXiv Preparation & Upload (1 day)
- [ ] Run arxiv-collector on paper directory; include .tex, .bib, ancillary code/data/figures.  
- [ ] Test ancillary build (e.g., reference datasets JSON, validation scripts).  
- [ ] Categories: math-ph (primary); cross-list quant-ph, gr-qc.  
- [ ] Upload as preprint (can update post-JMP submission if revisions needed).

### 4. JMP Submission (Immediate after arXiv)
- [ ] Submit via AIP portal[](https://jmp.peerx-press.org/); use RevTeX bundle.  
- [ ] Cover letter: Highlight mathematical novelty, rigorous validation, open-source code; note independent status but emphasize content merit.  
- [ ] If desk-rejected (low risk ~5-10% for affiliation): Add UBC visiting (if secured) and resubmit to Journal of Physics A or similar.

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
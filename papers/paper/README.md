# LaTeX Paper Bundle

This directory contains the master LaTeX sources for the SU(2) 3nj series paper(s).

## Structure

- `su2-3nj-unified-representations.tex` — Main comprehensive paper (single-paper option)
- `../shared/shared-macros.tex` — Common LaTeX macros
- `../shared/shared-bibliography.bib` — Unified bibliography

## Building

### Prerequisites

```bash
# LaTeX distribution (texlive or mactex)
sudo apt-get install texlive-full  # Ubuntu/Debian
# or
brew install --cask mactex          # macOS
```

### Compile

```bash
# Quick build
pdflatex su2-3nj-unified-representations.tex

# Full build with bibliography
pdflatex su2-3nj-unified-representations.tex
bibtex su2-3nj-unified-representations
pdflatex su2-3nj-unified-representations.tex
pdflatex su2-3nj-unified-representations.tex

# Or use latexmk (recommended)
latexmk -pdf su2-3nj-unified-representations.tex
```

### Clean

```bash
latexmk -c                 # Remove intermediate files
latexmk -C                 # Remove all generated files including PDF
```

## Status

**Current**: Scaffold structure with section placeholders

**Next steps**:
1. Import actual content from individual repo .tex files
2. Harmonize notation across sections
3. Add validation tables from JSON data
4. Create figures for stability analysis
5. Finalize author list and acknowledgments

## Alternative: Paper Series

For a 3-paper series instead of single comprehensive paper:
- Paper I: `paper-1-closed-forms.tex` (TBD)
- Paper II: `paper-2-recurrences.tex` (TBD)
- Paper III: `paper-3-generating-functionals.tex` (TBD)

Each would share the `../shared/` resources.

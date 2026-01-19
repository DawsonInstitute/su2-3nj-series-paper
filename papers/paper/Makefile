# Makefile for SU(2) 3nj series papers

.PHONY: all clean cleanall view help

# Default target
all: su2-3nj-unified-representations.pdf

# Master comprehensive paper
su2-3nj-unified-representations.pdf: su2-3nj-unified-representations.tex ../shared/shared-macros.tex ../shared/shared-bibliography.bib
	latexmk -pdf su2-3nj-unified-representations.tex

# Quick build (no bibliography)
quick:
	-pdflatex su2-3nj-unified-representations.tex

# View PDF
view: su2-3nj-unified-representations.pdf
	xdg-open su2-3nj-unified-representations.pdf || open su2-3nj-unified-representations.pdf || start su2-3nj-unified-representations.pdf

# Clean intermediate files
clean:
	latexmk -c
	rm -f *.bbl *.run.xml *.bcf

# Clean everything including PDF
cleanall:
	latexmk -C
	rm -f *.bbl *.run.xml *.bcf

# Help
help:
	@echo "SU(2) 3nj Series Paper Build System"
	@echo ""
	@echo "Targets:"
	@echo "  all       - Build su2-3nj-unified-representations.pdf (default)"
	@echo "  quick     - Quick build without bibliography"
	@echo "  view      - Open PDF in default viewer"
	@echo "  clean     - Remove intermediate files"
	@echo "  cleanall  - Remove all generated files including PDF"
	@echo "  help      - Show this help message"

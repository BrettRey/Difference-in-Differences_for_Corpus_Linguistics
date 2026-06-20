# Makefile for LaTeX paper compilation

# Configuration
LATEX = xelatex
BIBER = biber
MAIN = main
OUTDIR = .

# Targets
.PHONY: all quick blind lualatex clean distclean view help

# Default target: build the PDF
all: $(MAIN).pdf

# Full build sequence with bibliography
$(MAIN).pdf: $(MAIN).tex sections/*.tex references.bib references-local.bib
	@echo "==> First LaTeX pass..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Running Biber..."
	$(BIBER) $(MAIN)
	@echo "==> Second LaTeX pass..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Third LaTeX pass (finalizing)..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Build complete: $(MAIN).pdf"

# Quick build (single pass, no bibliography update)
quick: $(MAIN).tex
	@echo "==> Quick build (single pass)..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex

# Blinded build for double-blind review (author block removed) -> main-blind.pdf
blind: $(MAIN).tex sections/*.tex references.bib references-local.bib
	@echo "==> Blinded build (anonymized)..."
	$(LATEX) -output-directory=$(OUTDIR) -jobname=$(MAIN)-blind "\def\blindbuild{}\input{$(MAIN).tex}"
	$(BIBER) $(MAIN)-blind
	$(LATEX) -output-directory=$(OUTDIR) -jobname=$(MAIN)-blind "\def\blindbuild{}\input{$(MAIN).tex}"
	$(LATEX) -output-directory=$(OUTDIR) -jobname=$(MAIN)-blind "\def\blindbuild{}\input{$(MAIN).tex}"
	@echo "==> Blinded build complete: $(MAIN)-blind.pdf"

# Use LuaLaTeX instead of XeLaTeX (not recommended - breaks PDF text layer)
lualatex: LATEX = lualatex
lualatex: all

# Clean build artifacts (keep PDF)
clean:
	@echo "==> Cleaning build artifacts..."
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).bcf $(MAIN).blg $(MAIN).log
	rm -f $(MAIN).out $(MAIN).run.xml $(MAIN).toc $(MAIN).fdb_latexmk
	rm -f $(MAIN).fls $(MAIN).synctex.gz
	rm -f $(MAIN)-blind.aux $(MAIN)-blind.bbl $(MAIN)-blind.bcf $(MAIN)-blind.blg $(MAIN)-blind.log
	rm -f $(MAIN)-blind.out $(MAIN)-blind.run.xml $(MAIN)-blind.toc
	@echo "==> Clean complete"

# Clean everything including PDF
distclean: clean
	@echo "==> Removing PDF..."
	rm -f $(MAIN).pdf
	@echo "==> Deep clean complete"

# Open PDF viewer (macOS)
view: $(MAIN).pdf
	@echo "==> Opening PDF..."
	open $(MAIN).pdf

# Show available targets
help:
	@echo "Available targets:"
	@echo "  make          - Build PDF with full bibliography (default)"
	@echo "  make quick    - Quick build (single pass, no bib update)"
	@echo "  make blind    - Blinded PDF for double-blind review (main-blind.pdf)"
	@echo "  make lualatex - Build using LuaLaTeX (not recommended)"
	@echo "  make clean    - Remove build artifacts (keep PDF)"
	@echo "  make distclean- Remove everything including PDF"
	@echo "  make view     - Open PDF (macOS only)"
	@echo "  make help     - Show this help message"

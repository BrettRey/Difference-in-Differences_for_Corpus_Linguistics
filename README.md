# Difference-in-Differences for Corpus Linguistics

Working title:

*Difference-in-differences for corpus linguistics: Causal inference, corpus composition, and linguistic change after shocks*

## Build

```bash
make
```

Manual build:

```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

## Structure

- `main.tex` orchestrates the paper.
- `sections/` holds section-level source files.
- `notes/source-verification.md` tracks sources to verify before citation.
- `STATUS.md` records current state and next action.
- `DECISIONS.md` records durable setup and framing decisions.
- `references.bib` points to the central bibliography.
- `references-local.bib` is for verified project-specific entries only.

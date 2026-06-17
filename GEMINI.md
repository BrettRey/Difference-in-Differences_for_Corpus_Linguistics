# CLAUDE.md

This file provides project-specific guidance for Brett Reynolds's methods paper:

**Difference-in-differences for corpus linguistics: Causal inference, corpus composition, and linguistic change after shocks**

## Project Role

This is a corpus-methods paper. It should not be framed as a generic introduction to difference-in-differences. The contribution is the translation from DiD assumptions and estimands into corpus-linguistic problems.

Core local questions:

1. What is the treatment or shock?
2. What is the unit of identifying variation?
3. What corpus outcome is being measured?
4. What comparison series makes the counterfactual plausible?
5. What corpus-specific threat could explain the apparent effect?
6. What diagnostic would expose that threat?

## Build System

Use XeLaTeX, not pdfLaTeX or LuaLaTeX.

```bash
make
make quick
make clean
```

Manual full build:

```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

## File Structure

```text
Difference-in-Differences_for_Corpus_Linguistics/
|-- main.tex
|-- sections/
|-- notes/
|-- submission/
|-- STATUS.md
|-- DECISIONS.md
|-- README.md
|-- references.bib          # symlink to ../../.house-style/references.bib
|-- references-local.bib    # verified project-specific additions only
`-- .house-style/           # symlinks to central house-style files
```

## House Style

The project points to central house style by symlink. Follow `.house-style/style-rules.yaml` and the workspace rules.

Important local emphases:

- No local house-style snapshot. Keep `.house-style/preamble.tex` and `.house-style/style-rules.yaml` as symlinks.
- Do not add citations or BibTeX entries from memory. Verify all DiD and application sources first.
- Do not treat tokens as the statistical unit unless the identification argument really supports that level.
- Mark the difference between linguistic unit, measurement unit, identifying unit, and clustering/aggregation unit.
- Avoid "DiD for corpus linguists" tutorial framing. The paper is about methodological hygiene for causal claims from corpus data.
- Keep visible keywords and `pdfkeywords` synchronized.

## Citation Discipline

Use the central bibliography when the key already exists. Add to `references-local.bib` only after source verification. Keep candidate source work in `notes/source-verification.md` until verified.

## Current State

Read `STATUS.md` and `DECISIONS.md` at the start of a session. Log durable decisions to `DECISIONS.md` as they happen.

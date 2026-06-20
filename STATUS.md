# STATUS

**Last updated:** 2026-06-20
**State:** **SUBMITTED** to *Corpus Linguistics and Linguistic Theory* (CLLT, De Gruyter Mouton) via ScholarOne. **Manuscript ID CLLT.2026.0087**, submitted 20-Jun-2026. Preprint posted at [LingBuzz 010080](https://lingbuzz.net/lingbuzz/010080) on 20-Jun-2026; cite as `lingbuzz/010080`. Manuscript complete and self-contained: 9 sections, 20 pp, abstract 199 w, 1 figure (threat DAG), 2 tables (estimand ledger + failure map), 30 references. Blind copy (`make blind`) verified leak-free (no author name, no Author metadata, no acknowledgments, no author running header). Simulations reproducible (3 stdlib-only, seeded Python scripts) shipped as supplementary material; AI-use disclosure placed in the cover letter and the declarations form (not the manuscript). Full submission package in `submission/` (copy-paste sheet, cover letter, title page, declarations, author bio, supplement zip).
**Next action:** Await editorial / peer-review response. On revision or acceptance: reformat references from biblatex-apa to the **Unified Style Sheet for Linguistics** (deferred this round); optionally deposit the scripts at Zenodo/OSF for a citable DOI; if CLLT requires the AI-use statement in the *published* version, restore an Acknowledgements/AI section at camera-ready (one-line revert flagged in `main.tex`).
**Blocker:** None. Under review.

## Working Title

*Difference-in-differences for corpus linguistics: Causal inference, corpus composition, and linguistic change after shocks*

## Current Frame

This is a corpus-methods paper, not a generic DiD explainer. The contribution is to translate the design into corpus-linguistic inference problems: corpus composition, register drift, topic shocks, author turnover, token dependence, measurement drift, and the gap between corpus frequencies and population claims.

## Infrastructure

- Created from the house-style LaTeX paper template on 2026-06-17.
- Set up under `papers/Difference-in-Differences_for_Corpus_Linguistics/`.
- `references.bib` is a symlink to the central `.house-style/references.bib`.
- `.house-style/preamble.tex` and `.house-style/style-rules.yaml` are symlinks to central house-style files.
- Project-specific verified references belong in `references-local.bib`.
- Section source lives in `sections/`.
- Source-verification notes live in `notes/`.

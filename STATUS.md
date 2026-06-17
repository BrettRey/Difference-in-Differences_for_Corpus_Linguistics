# STATUS

**Last updated:** 2026-06-17
**State:** Three advisory-board rounds done; both literature halves intaken; `DESIGN-SPEC.md` at **v2**. Orienting principle fixed: the paper improves methods, the worked examples are vehicles, the round-3 threats are the curriculum. Spine re-centered on a **progressive build** of designs on feminization: (1) Swiss French vs France clean 2x2 core, (2) scale to staggered multi-variety, (3) trilingual Switzerland as a design-choice contrast; plus the simulation spine, Italian Sabatini 1987, and Croatian/Serbian breakdown. Deepest contribution = design choice. See DECISIONS.md and DESIGN-SPEC.md (2026-06-17).
**Next action:** Rungs 1 and 2 are drafted in `sections/08` (both passed check-style); the decision ladder is validated by `simulations/rung1-ladder-sim.py`. Remaining: rung 3 (trilingual Switzerland, compact design-choice contrast), the Italian single-shock case, the Croatian/Serbian breakdown, and the simulation spine in prose. Also pending: extend the simulation (reweighting-recovery arm + actual partial-pooling estimator), the B&B-calibrated breakdown cutoff, principled thresholds, a power check, and the §11 full reads (Callaway-Sant'Anna / Rambachan-Roth / Egami). Cross-fertilization with Kinds_as_Projectibility_Profiles logged (ladder = a support-grade/demotion instance; kept out of the methods body by default).
**Blocker:** None. Two rungs drafted; ladder validated; cross-model boards endorse the architecture.

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

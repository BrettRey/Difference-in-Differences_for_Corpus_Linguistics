# Pre-submission checklist

Target venue: **International Journal of Corpus Linguistics** (IJCL,
Benjamins). Fallback venue: **Corpora** (Edinburgh UP).

Status as of 2026-07-03. `[x]` = verified; `[ ]` = open / venue-specific.

## Manuscript correctness

- [x] Full draft complete: abstract + Sections 1-9.
- [x] IJCL hard cut complete: 15 pp, 7,487 PDF words all-in; blind copy 7,488 PDF words.
- [x] Abstract current and methods-framed: 140 words.
- [x] Build clean with XeLaTeX: `make` and `make blind` both exit 0.
- [x] No undefined citations or references in the build logs.
- [x] Formal frequency notation corrected: `\hat f = f + \epsilon`; `f = \pi + b`; `b` is the corpus filter, not finite-sample noise.
- [x] Simulation numbers reconciled against source scripts: failure-map table from `rung-failure-map.py` (seed 7), recovery estimates from `rung1-recovery-sim.py` (seed 2024), routing validation from `rung1-ladder-sim.py` (seed 12345).
- [x] Worked example reframed as a stress test/non-finding, with feasibility anchors and a compact reporting table.
- [x] Factual claims ground-truthed for the worked-example dates and Swiss parliamentary coverage.
- [x] References resolve; no duplicate local keys; high-risk legal/corpus references previously source-verified.
- [x] Figure/table inventory current: 1 figure, 4 tables.

## Front Matter

- [x] Title + subtitle current.
- [x] Keywords visible line and `pdfkeywords` synchronized.
- [x] Author, ORCID, affiliation, and contact email present in the non-blind build.
- [x] Blind build strips author block and PDF Author metadata.
- [x] AI-use disclosure placed in `submission/cover-letter-ijcl.md`, not in the blinded manuscript.

## Venue-Specific

- [x] Venue choice: IJCL primary, Corpora fallback.
- [x] IJCL length checked: official Benjamins submission page gives 9,000 words including tables and references; current PDF count is below the cap.
- [x] Corpora fallback length checked: official EUP submission page gives 6,000-10,000 words for long papers, including title, abstract, references, notes, tables, and figures.
- [x] CLLT-specific `\term` macro override removed.
- [x] Anonymization for peer review: `main-blind.pdf` leak check clean.
- [x] Code/data availability: deterministic scripts and README supplied in `submission/simulations-supplement.zip`.
- [ ] Confirm IJCL/Benjamins reference-style expectations for first submission.
- [ ] Confirm the live Benjamins form's required declaration/title-page/author-bio fields.
- [x] Cover-letter salutation finalized as generic "Dear Editors".
- [x] Final submission-gate read completed after the hard cut.

## Notes

- The worked example is a teaching vehicle, not an empirical finding; keep the cover letter on the corpus-methods contribution.
- The old `submission/cllt-requirements.md` and `submission/cover-letter.md` are archived CLLT materials, not current IJCL submission documents.

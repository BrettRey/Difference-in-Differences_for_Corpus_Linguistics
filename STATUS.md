---
slug: difference-in-differences-for-corpus-linguistics
kind: paper
title: 'Difference-in-differences for corpus linguistics: Causal inference, corpus composition, and linguistic
  change after shocks'
stage: complete
external: rejected
blocked_on:
- venue-decision
updated: 2026-07-13
source:
- STATUS.md
- PORTFOLIO.md
preprints:
- lingbuzz/010080
next_action: Choose a retarget venue off the corpus-linguistics-journal track (three desk rejections on
  centrality across Reynolds methods papers have exhausted it); complete a new venue-decision record before
  repackaging
notes: 'Desk-rejected by CLLT (CLLT.2026.0087, 2026-07-01) and then IJCL (IJCL-26173, 2026-07-13), both
  on centrality/fit -- ''same grounds as Corpora''s rejection of the dative sibling'' (bresnan-dative-alternation-reanalysis).
  PORTFOLIO.md:41''s own bolded Status-column word is ''**Preprint** (IJCL + CLLT desk-rejected)'', which
  reads like external: preprint. But SCHEMA.md''s own worked example classifies the structurally identical
  bresnan-dative-alternation-reanalysis case (PORTFOLIO Status column also reads ''Preprint (Corpora desk-rejected...)'')
  as stage: complete / external: rejected / blocked_on: venue-decision. Followed that precedent rather
  than the PORTFOLIO Status-column word: ''Preprint'' there names the current public artifact (it is only
  living as a LingBuzz posting), not a considered external classification, and the schema''s own value
  table defines ''rejected'' as exactly this state (''rejected or desk-rejected, no successor submission
  yet''). PORTFOLIO.md:101 is the earlier, now-superseded Jul 3 row (before the Jul 13 IJCL rejection);
  it explicitly says ''see Active Submissions row'', pointing to line 41 as current, so this is not a
  live source conflict.'
---

# STATUS

**Last updated:** 2026-07-13
**State:** **DESK-REJECTED at IJCL (2026-07-13).** Manuscript IJCL-26173 was assigned and then desk-rejected the same day by Associate Editor Gavin Brookes: "not sufficiently situated within a corpus linguistics research context." Second corpus-linguistics desk rejection of this paper (CLLT desk-rejected it 2026-07-01 on the same grounds) and the third across Reynolds methods papers (Corpora desk-rejected the dative sibling 2026-07-12). All public surfaces reverted to Preprint. Originally submitted to IJCL via Editorial Manager on 03-Jul-2026. Track at https://www.editorialmanager.com/ijcl/. As-submitted build (the 2026-07-03 hard cut): 9 sections, 15 pp, 7,487 PDF words all-in, abstract 140 w (portal cap 150), 1 figure, 4 tables. Preprint remains live at [LingBuzz 010080](https://lingbuzz.net/lingbuzz/010080); cite as `lingbuzz/010080`. The earlier CLLT submission (CLLT.2026.0087, submitted 20-Jun-2026) was desk rejected for scope/fit on 01-Jul-2026; CLLT-specific submission files remain in `submission/` as archival material.
**Next action:** Choose a retarget venue **off the corpus-linguistics-journal track** (Brett's decision) — three corpus-linguistics desk rejections on centrality have exhausted it for this methods paper. Candidates: Journal of Quantitative Linguistics, Research Methods in Applied Linguistics, Glossa/OLH (transparency AI policy), or NLP/CL (Natural Language Engineering, LRE). Corpora is NOT a fallback (it desk-rejected the dative sibling on the same grounds). A new venue-decision record is required before repackaging; make the field-internal payoff legible on page one. Letter: `submission/ijcl-desk-rejection-2026-07-13.md`.
**Blocker:** None. In the journal's queue.

## Working Title

*Difference-in-differences for corpus linguistics: Causal inference, corpus composition, and linguistic change after shocks*

## Current Frame

This is a corpus-methods paper, not a generic DiD explainer. The contribution is to translate the design into corpus-linguistic inference problems: corpus composition, register drift, topic shocks, author turnover, token dependence, measurement drift, and the gap between corpus frequencies and population claims.

## 2026-07-01 CLLT Scope Decision

- *Corpus Linguistics and Linguistic Theory* declined CLLT.2026.0087 without external review after the editor and an editorial-board member read it.
- Signal: positive interest in the study, but mismatch with CLLT's narrow remit: the paper advances understanding of corpora and their representational limits more directly than it advances a contemporary linguistic-theory issue.
- Suggested alternatives in the decision letter: *Applied Linguistics*, *International Journal of Corpus Linguistics*, or *Corpora*.
- Interpretation: venue-fit failure, not an argument-level rejection. Brett had flagged this fit risk before submission; record as calibration for future venue selection.

## 2026-07-01 Xu Follow-Up

- Ke-Li Xu replied to Brett's query about joint categorical inference outside RD. Main use: reserve material, not an immediate manuscript change.
- Application logged at `notes/xu-joint-categorical-application-2026-07-01.md`: strategy-specific DiDs are diagnostics; a full category-level analysis would model realization strategy as a joint multinomial outcome.
- John C. Lazzaro's job-market paper, "Nonlinear Regression Discontinuity Designs with Covariates" (this version: 2026-04-15), obtained from his UW job-market page and saved at `literature/lazzaro-nonlinear-rd-covariates.pdf`.
- Correspondence summary saved at `correspondence/xu-exchange-2026-07-01.md`.

## 2026-07-01 Retarget Decision

Fit checked against each journal's recent articles via CrossRef (56 IJCL, 78 Corpora; publisher sites block automated fetch), 2026-07-01. Both are genuine corpus-methods homes and neither is theory-gated, so neither repeats CLLT's scope risk.

- **Primary:** *International Journal of Corpus Linguistics* (IJCL, Benjamins, ISSN 1384-6655). Ran a 2025 special issue on **reproducibility, replicability, and robustness in corpus linguistics** — the same epistemic-hygiene conversation this paper joins — plus recent composition/sampling methods ("Down-sampling from hierarchically structured corpus data," "Achieving stability in corpus-based analysis of word types") and variation modelling ("Not all linguistic variation is equally predictable," on the dative alternation). Higher reach. Cover letter: `submission/cover-letter-ijcl.md`.
- **Co-target:** *Corpora* (Edinburgh UP, ISSN 1749-5032). Also publishes inferential methods ("Equivalence testing techniques for corpus linguistics," "Advancing our understanding of dispersion measures," "Collocations in downsampled corpora"), but skews more to corpus-building announcements and corpus-assisted discourse. Cover letter: `submission/cover-letter-corpora.md`.
- **Deprioritized:** *Applied Linguistics* (OUP). Expects an applied empirical finding; the worked example is a deliberate non-finding.
- The intermediate flip to a Corpora lead was based on a single Corpora title; the fuller recent-issue survey supersedes it (IJCL has the closer methods thread and more reach).
- **Framing fix:** cover letter rewritten to pitch the corpus-methods/representativeness contribution, not the "intersection with linguistic theory" line that CLLT bounced. Xu multinomial stays R&R-reserve.

## 2026-07-03 IJCL Hard-Cut Revision

Fable 5's IJCL-readiness review was accepted in substance: submit to IJCL first, but not the overlength CLLT file.

- Length fixed: original PDF count was 11,443 words; current `main.pdf` is 7,487 PDF words, comfortably below IJCL's verified 9,000-word cap including tables and references.
- Abstract reframed as a methodological framework plus simulation-based failure map; the feminization case is explicitly a stress test, not an empirical finding about French.
- Formal notation fixed: `f` is the expected corpus frequency, `\hat f` is the realized sample proportion, and sampling noise is separated from the corpus-filter term `b`.
- Added a compact "minimum report" table and a feasibility-anchor table for candidate data homes, treatment dates, outcome cues, and failure modes.
- Cut and compressed Sections 3, 5, 6, and 8; detailed simulation-gate narration now lives in the simulation README rather than the article.
- Removed the CLLT-specific `\term` override; central house style now applies.
- Current blind build is leak-free and 15 pp.

### Pre-submit housekeeping (closed by the 2026-07-03 submission)

Submission gate run 2026-07-03: build/blinding/source-grounding all clean; manuscript shortened for IJCL; full record in `submission/submission-notes.md`. The live-portal items below were resolved during the upload (the form's 150-word abstract cap was the only surprise; abstract trimmed to 140 words).

1. ~~Confirm the live Benjamins submission fields and whether a separate title page, declarations file, or author bio is required.~~
2. ~~Confirm whether Benjamins requires a reference-style change at first submission.~~ Submitted with the project house `biblatex-apa` setup.
3. Verify any new citation against `notes/source-verification.md` before adding it (still applies for any R&R work).
4. ~~Reuse the blind build (`make blind`) if IJCL is double-blind.~~

## 2026-07-03 Submitted to IJCL

- Submitted via Editorial Manager (https://www.editorialmanager.com/ijcl/); receipt confirmed by the IJCL editorial office on 03-Jul-2026.
- No reference number yet; one is assigned once an editor is assigned. Progress is trackable through the Editorial Manager author login.
- Package as prepared in `submission/` (see `submission/submission-notes.md`); cover letter `submission/cover-letter-ijcl.md` carries the AI-use disclosure.
- Fallback if IJCL declines: *Corpora* (Edinburgh UP), cover letter already drafted at `submission/cover-letter-corpora.md`.

## 2026-07-03 Shutdown Notes

- Shutdown confirmed after the IJCL submission workflow. The live portal's only unexpected constraint was a 150-word abstract cap; the abstract is now 140 words in `main.tex`, `submission/copy-paste.md`, the rebuilt PDFs, and `submission/main-blind-editable.docx`.
- Current upload/reference state: submitted and editorial-office receipt confirmed; no IJCL reference number yet.
- Next action remains narrow: log the IJCL reference number when Editorial Manager assigns one. Do not revise or re-contact while the paper is in the journal queue.
- Public surfaces updated after Brett's correction (the publications page lists where each article is under review): `publications.html`, `llms.txt`, the `paper.md` mirror status field, and the CV entry now read "Under review at *International Journal of Corpus Linguistics*". CV rebuilt; website commit `2bbfb5f` pushed live.

## Infrastructure

- Created from the house-style LaTeX paper template on 2026-06-17.
- Set up under `papers/Difference-in-Differences_for_Corpus_Linguistics/`.
- `references.bib` is a symlink to the central `.house-style/references.bib`.
- `.house-style/preamble.tex` and `.house-style/style-rules.yaml` are symlinks to central house-style files.
- Project-specific verified references belong in `references-local.bib`.
- Section source lives in `sections/`.
- Source-verification notes live in `notes/`.

# Pre-submission checklist

Target venue: **CLLT** (*Corpus Linguistics and Linguistic Theory*, De Gruyter Mouton) — chosen as the best home for a methods contribution; requirements in `cllt-requirements.md`. (Earlier candidates: IJCL, Corpora.)

Status as of 2026-06-20. `[x]` = verified; `[ ]` = open / venue-specific.

## Manuscript correctness (done)

- [x] Full draft complete: abstract + §1–§9.
- [x] Build clean (XeLaTeX), 21 pp; no undefined references or citations; no overfull boxes > 20 pt.
- [x] House style: `check-style.py` clean on `main.tex` and every section; advisory rules (corrective framing, paragraph length, participial adjuncts, strong modals, opener cadence) addressed.
- [x] **Simulation numbers reconciled against source scripts** — Table 2 (`rung-failure-map.py`, seed 7) every cell exact; §8 `+0.13 / −0.000 / +0.15` (`rung1-recovery-sim.py`, seed 2024) exact. No drift. Scripts are deterministic (fixed seed, stdlib only). (2026-06-20: composition-gate logic in `verdict()` corrected to reweight-then-proceed so it matches §2's claim; change was RNG-neutral, all Table 2 cells reproduce bit-identical. Verdict terminology standardized to the four labels in abstract/body/conclusion/code.)
- [x] **Factual claims ground-truthed** — Swiss *Bulletin officiel* dates (digitized 1891; full verbatim debates from 1971) verified; PM attributions (Fabius 1986, Jospin 1998) verified via Légifrance.
- [x] **References** — all 30 cited keys resolve (28 local + 2 central); no duplicate keys; no uncited local entries; highest-risk entries web-verified to exact match (incl. both Légifrance circular IDs); no hallucinations found. (2026-06-20: added 4 corpus-methodology anchors — McEnery & Hardie 2012, Leech et al. 2009, Hinrichs et al. 2015, Poplack & Dion 2009 — full texts read in `literature/`, Crossref DOIs on all.)
- [x] Bibliography capital protection correct under biblatex-apa (proper nouns `{French}`, `{Francophonie}` survive sentence-casing; no acronyms at risk).
- [x] Grammar / weird-sentence pass and redundancy pass complete.
- [x] Figures vector (TikZ DAG); tables booktabs; `\clearpage` before bibliography.

## Front matter (mostly done; one to check)

- [x] Title + subtitle; keywords visible-line and `pdfkeywords` in sync.
- [x] Author, ORCID, affiliation (Humber Polytechnic & U Toronto), contact email present.
- [x] Acknowledgements including AI-use statement (Claude Opus 4.8, OpenAI Codex; responsibility retained).
- [x] Abstract length: **199 words**, under CLLT's ~200 target.

## Venue-specific (CLLT)

- [x] **Venue chosen**: CLLT; author guidelines summarized in `cllt-requirements.md`.
- [ ] **Reference style.** Paper uses biblatex-apa (house default); CLLT follows the *Unified Style Sheet for Linguistics Journals* (author-date). **Deferred to acceptance** — they don't require the house style reformatted on first submission. (Reformatting the bibliography is then the main house-style change.)
- [ ] Confirm word/page limit, section-numbering, and figure/table caption format against `cllt-requirements.md` (sentence-case numbered headings; table captions above, figure captions below — already followed).
- [x] **Anonymization for peer review** — `make blind` produces `main-blind.pdf`: strips author name, ORCID, affiliation, email, and PDF Author metadata (verified leak-free: 0 name hits in text, no Author field). AI-use disclosure **retained** in the blind copy (non-identifying; heading renames to "Statement on AI use"). Script paths don't deanonymize (supplementary route, no `BrettRey` URL). "the present author" avoided throughout.
- [~] **Code/data availability** — availability statement in `main.tex`; the three `simulations/*.py` scripts + README committed to git (2026-06-20) and supplied as supplementary material; seeded and stdlib-only, reproduce exactly. *Still optional for acceptance:* a public deposit + DOI (Zenodo/OSF) to replace "supplementary material" in the statement.
- [ ] **AI-use disclosure** — confirm the venue's required wording/placement (the acknowledgement carries one; some journals mandate a specific statement or a separate field).
- [ ] Competing-interests / funding / ethics statements as the venue requires.
- [ ] Cover letter.
- [ ] Suggested / excluded reviewers, if requested.
- [ ] Final spell-check and one cold read-through.

## Notes

- The worked example is a teaching vehicle, not an empirical finding (paper's north star) — keep the cover letter framing on the *method contribution*, not a French-feminization result.
- Optional hardening: compute the simulation numbers at render time (Quarto) so Table 2 can never drift from the scripts. Not required for this submission.

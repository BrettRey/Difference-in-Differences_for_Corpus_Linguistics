# Pre-submission checklist

Target readership/venues (DECISIONS 2026-06-17): **IJCL** (*International Journal of Corpus Linguistics*, Benjamins), **Corpora** (Edinburgh UP), **CLLT** (*Corpus Linguistics and Linguistic Theory*, De Gruyter Mouton). No single venue committed yet.

Status as of 2026-06-19. `[x]` = verified this session; `[ ]` = open / venue-specific.

## Manuscript correctness (done)

- [x] Full draft complete: abstract + §1–§9.
- [x] Build clean (XeLaTeX), 19 pp; no undefined references or citations; no overfull boxes > 20 pt.
- [x] House style: `check-style.py` clean on `main.tex` and every section; advisory rules (corrective framing, paragraph length, participial adjuncts, strong modals, opener cadence) addressed.
- [x] **Simulation numbers reconciled against source scripts** — Table 2 (`rung-failure-map.py`, seed 7) every cell exact; §8 `+0.13 / −0.000 / +0.15` (`rung1-recovery-sim.py`, seed 2024) exact. No drift. Scripts are deterministic (fixed seed, stdlib only).
- [x] **Factual claims ground-truthed** — Swiss *Bulletin officiel* dates (digitized 1891; full verbatim debates from 1971) verified; PM attributions (Fabius 1986, Jospin 1998) verified via Légifrance.
- [x] **References** — all 26 cited keys resolve (24 local + 2 central); no duplicate keys; no uncited local entries; 10 highest-risk entries web-verified to exact match (incl. both Légifrance circular IDs); no hallucinations found.
- [x] Bibliography capital protection correct under biblatex-apa (proper nouns `{French}`, `{Francophonie}` survive sentence-casing; no acronyms at risk).
- [x] Grammar / weird-sentence pass and redundancy pass complete.
- [x] Figures vector (TikZ DAG); tables booktabs; `\clearpage` before bibliography.

## Front matter (mostly done; one to check)

- [x] Title + subtitle; keywords visible-line and `pdfkeywords` in sync.
- [x] Author, ORCID, affiliation (Humber Polytechnic & U Toronto), contact email present.
- [x] Acknowledgements including AI-use statement (Claude Opus 4.8, OpenAI Codex; responsibility retained).
- [ ] Abstract length vs venue limit (currently ~165 words; IJCL/CLLT/Corpora each have a cap — confirm).

## Venue-specific (open — needs the chosen journal's author guidelines)

- [ ] **Choose venue** (IJCL / Corpora / CLLT) and pull its current author guidelines.
- [ ] **Reference style.** Paper uses biblatex-apa (house default). All three are likely to want a different style — IJCL and CLLT typically follow the *Unified Style Sheet for Linguistics Journals* (author-date); Corpora has its own EUP style. Reformatting the bibliography to the venue style is the most probable house-style change.
- [ ] Word/page limit; section-numbering and heading conventions; figure/table caption format and resolution requirements.
- [ ] **Anonymization for peer review** — produce a blinded manuscript: strip author name, ORCID, affiliation, email, and acknowledgements (incl. the AI statement) for the review copy; check self-citations and the simulation-script paths don't deanonymize. ("the present author" already avoided throughout.)
- [ ] **Code/data availability** — deposit the three `simulations/*.py` scripts (and any corpus pointers) in a public repo or supplementary archive; add an availability statement. Scripts are seeded and stdlib-only, so they reproduce exactly.
- [ ] **AI-use disclosure** — confirm the venue's required wording/placement (the acknowledgement carries one; some journals mandate a specific statement or a separate field).
- [ ] Competing-interests / funding / ethics statements as the venue requires.
- [ ] Cover letter.
- [ ] Suggested / excluded reviewers, if requested.
- [ ] Final spell-check and one cold read-through.

## Notes

- The worked example is a teaching vehicle, not an empirical finding (paper's north star) — keep the cover letter framing on the *method contribution*, not a French-feminization result.
- Optional hardening: compute the simulation numbers at render time (Quarto) so Table 2 can never drift from the scripts. Not required for this submission.

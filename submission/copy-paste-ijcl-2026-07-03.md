> **SUPERSEDED, ARCHIVAL ONLY. DO NOT USE AT A PORTAL.**
>
> This is the IJCL submission of 2026-07-03. It carries the old title and the
> 140-word IJCL abstract, both of which the manuscript has since replaced.
> For RMAL use `submission/portal-fields-RMAL-2026-07-31.md`, which carries the
> current values with a source pointer for each.

# Submission copy-paste sheet — IJCL

Plain-text fields for the Benjamins/IJCL manuscript form. Source of truth is
`main.tex`; this file is kept in sync with the IJCL retargeted draft
(2026-07-03).

---

## Title

Difference-in-differences for corpus linguistics: Causal inference, corpus composition, and linguistic change after shocks

### If the form splits title / subtitle

- **Title:** Difference-in-differences for corpus linguistics
- **Subtitle:** Causal inference, corpus composition, and linguistic change after shocks

---

## Abstract (140 words)

Difference-in-differences (DiD) is built for counterfactual claims about change after shocks, but a corpus frequency isn't the estimand itself. This paper translates DiD into corpus terms by treating the expected corpus frequency as a population rate plus composition-and-measurement bias, with realized proportions adding sampling noise. A causal reading requires separating the target population, corpus composition, measurement procedure, identifying unit, and dependence unit before estimation. Parallel trends have to hold twice over, in the underlying rate and in the corpus filter; diagnostics can disqualify or bound this claim, not confirm it. The paper gives a reporting discipline and pre-specified decision ladder that routes results to a bounded estimate, descriptive reading, shared wave, or not identified. Simulations map when the ladder succeeds and fails. Feminization of profession nouns under francophone language policy is used as a stress test, not an empirical finding.

---

## Keywords

Semicolon-separated:

difference-in-differences; corpus linguistics; causal inference; corpus composition; linguistic change

Comma-separated:

difference-in-differences, corpus linguistics, causal inference, corpus composition, linguistic change

---

## Author / affiliation (non-blind metadata fields)

- **Name:** Brett Reynolds
- **Affiliation:** Humber Polytechnic & University of Toronto
- **ORCID:** 0000-0003-0073-7195
- **Email:** brett.reynolds@humber.ca

---

## Files to upload

- `main-blind.pdf` — anonymized manuscript for review (`make blind`; verified leak-free)
- `submission/simulations-supplement.zip` — supplementary code archive
- `submission/cover-letter-ijcl.md` — cover letter text (paste into the form or render if a separate file is requested)

## Article type / declarations

- **Article type:** full research paper / methodological article
- **Competing interests:** none
- **Funding:** none to declare
- **Ethics:** no human-subjects data; the corpora named in the worked example are illustrative, not analyzed
- **AI use:** disclosed in the cover letter (Claude Opus 4.8, OpenAI Codex, as drafting/editing aids; author responsible for all claims)
- **Data/code:** three deterministic Python scripts, standard library only, fixed seeds, supplied as supplementary material
- **Reference style:** manuscript currently uses the house `biblatex-apa` setup; confirm whether Benjamins requires a different reference style at first submission

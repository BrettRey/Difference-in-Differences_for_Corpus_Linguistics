# Portal fields: Research Methods in Applied Linguistics, 2026-07-31

<!-- SUMMARY: Every value the RMAL portal will ask for, with a source pointer, so the portal session is transcription rather than composition · status: incomplete, see §11 · updated: 2026-07-31 -->

**Rule:** a value with no source pointer counts as unchecked. Do not type any field
from memory or from the CLLT/IJCL submissions.

Guide for authors read: the document Brett supplied 2026-07-31 (ScienceDirect 403s
automated fetch). Limits below are from that reading and should be re-confirmed on
the submission day.

## 1. Routing

| Field | Value | Source |
|---|---|---|
| Journal | Research Methods in Applied Linguistics (Elsevier, ISSN 2772-7661) | venue-decision-2026-07-31.md |
| Article type | **Research Article** (cap 10,000 all inclusive) | guide; see §11 risk |
| Section | none offered | guide |

## 2. Title, abstract, keywords

| Field | Limit | Value | Source |
|---|---|---|---|
| Title | none stated | Did the intervention change usage? Validity threats and difference-in-differences in before-and-after corpus designs | main.tex |
| Abstract | 250 words | 206 words, verbatim below | main.tex, do not retype |
| Keywords | 1--7, avoid multi-word with "and"/"of" | 6, listed below | main.tex |

**Abstract, copy verbatim:**

> Researchers routinely claim that a policy, reform, or campaign changed language use, comparing corpus frequencies before and after. A corpus frequency is a score, not the construct it stands for: it carries the population rate plus whatever the corpus's composition and coding contributed. That contribution shifts across periods for reasons unrelated to anyone's usage, and a two-point comparison can't separate it from an effect. Difference-in-differences is the standard repair, and this paper translates its assumptions into corpus terms. Its identifying assumption, that the compared series would have moved together absent the intervention, then has to hold twice: in the rate people use, and in the corpus itself. A numerical illustration shows the first holding while the second fails, producing a four-point effect where the true effect is zero. Diagnostics can disqualify or bound a causal reading, never confirm it. The paper supplies a reporting standard and a pre-specified decision procedure ending in one of four verdicts, one of which is that the effect isn't identified. Simulations map where that procedure fails, and a composition margin of one public archive is measured to show the confound is real and steep. Feminization of profession nouns under francophone language policy is a stress test, not a finding.

**Keywords:** construct validity; difference-in-differences; causal inference; corpus composition; research methods; language policy evaluation

## 3. Author

| Field | Value | Source |
|---|---|---|
| Given / family | Brett / Reynolds | submission/title-page.md |
| Affiliations | Humber Polytechnic, Toronto, Canada; University of Toronto, Toronto, Canada | title-page.md |
| ORCID | 0000-0003-0073-7195 | title-page.md |
| Corresponding | yes | title-page.md |
| Email | brett.reynolds@humber.ca | title-page.md |
| Department, postal code | NOT RECORDED | see §11 |

## 4. Files and item types

| File | Portal item type | Built? |
|---|---|---|
| main-blind.pdf | Manuscript (anonymized) | yes, verified leak-free |
| main.tex + sections/ + references | Source files (**.tex required, PDF not acceptable as source**) | yes; bundle not yet assembled |
| submission/title-page.md -> PDF | Title Page | needs rebuild with the new title |
| submission/declarations.md | Declarations | needs re-check against RMAL wording |
| supplement/supplementary-designs.pdf | Supplementary material | yes |
| simulations/*.py | Supplementary material | 4 scripts incl. speaker-pool-audit.py |
| Cover letter | Cover letter | NOT WRITTEN for RMAL |

## 5. Declarations, final wording

- Funding: none.
- Competing interests: none.
- Ethics / human subjects: none; no participant data. Corpora named are illustrative.
- Data and code: simulation scripts and the archive-query script supplied; the speaker-pool figures query a public service and need no key.
- Generative AI: declared **in the manuscript**, in a named section before the references, per Elsevier's template. Retained in the blinded build.

## 6. Preprint and overlap history

- Preprint: LingBuzz 010080. **Stale**: it is the pre-cut CLLT version, roughly 11,400 words, now several revisions behind. Preprints do not count as prior publication for RMAL, but a reviewer following the link reads a different paper.
- Prior submissions of this manuscript: CLLT (desk-rejected 2026-07-01), IJCL (desk-rejected 2026-07-13). Not under consideration anywhere as of 2026-07-31.

## 7. Reviewers

Suggested: none. Do not invent names. Leave to the editor unless the portal requires entries.

## 11. Unresolved, blocking the portal session

1. **Live submission route.** `editorialmanager.com/rmal` returns "Site under development. Do not use for live manuscript submission." Reach the portal via the journal's own Submit link on ScienceDirect and record the real URL here.
2. **Article-type risk.** Research Article caps at 10,000 and the manuscript is at 9,770. Brief Report caps at 5,000 and explicitly absorbs "commentaries... not based on empirical studies". The simulation study plus the measured archive margin are the defence for the Research Article reading.
3. **Cover letter** for RMAL not written.
4. **Title page** still carries the old title; rebuild before upload.
5. **Author department and postal code** not recorded anywhere local.
6. **Open access / licence choice** not decided; APC applicability unknown.
7. **LingBuzz preprint** decision: refresh to the current version, or leave and accept that the public copy differs.

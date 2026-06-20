# CLLT submission requirements (Corpus Linguistics and Linguistic Theory)

Gathered 2026-06-19 from the De Gruyter Mouton journal style sheet (v1.3, the authoritative formatting/reference spec) and the journal's De Gruyter Brill page. `✓` = paper already complies; `✗` = needs change; `?` = confirm from the CLLT Instructions for Authors (the journal page blocks automated fetch — view logged in or via ScholarOne).

## Journal facts

- Publisher: **De Gruyter Mouton** (now De Gruyter Brill). Editor-in-chief: **Stefanie Wulff** (U. Florida).
- Submission system: **ScholarOne** — http://mc.manuscriptcentral.com/cllt
- **Open access:** Gold OA since 2025, all articles **CC-BY**, **no article processing charge** (free to authors).
- **Scope (caveat):** "high-quality original corpus-based research that explicitly tackles an issue in contemporary theory, and/or promises to advance corpus-linguistic methodology." It **explicitly excludes** applied work including "language planning… and **policy**," pedagogy, stylistics, education, forensic, translation. → Our paper is a *methodology* contribution (fits the second clause); the feminization **policy** is a teaching vehicle, not the topic. The cover letter and abstract must make the methodological contribution unmistakable so it isn't desk-rejected as a language-policy paper.

## Reference & citation style — the main change ✗

Mouton requires the **Unified Style Sheet for Linguistics** (linguistlist.org/pubs/tocs/JournalUnifiedStyleSheet2007.pdf). The paper is in **biblatex-apa**; this must switch.

In-text (differs from APA):
- "and" not "&" between author names in running text: **(Smith and Jones 1995)**, not (Smith & Jones, 2005).
- **No comma before the year**: (Bertrand et al. 2004), not (Bertrand et al., 2004).
- 3+ authors → **et al.** in text, but list **all** authors in the reference entry.
- Full page ranges (140–145, not 140–5); "see Section 4.2", "Table 3", "Figure 2" (capitalized).

Reference list (Unified format — note differences from APA):
- **Year is not parenthesized**, sits right after the author: `Chomsky, Noam. 1986. Title…`
- **Full first names** where available (paper's bib has several initials-only — e.g., "Cameron, A. Colin", "Sun, Liyang" ok; fill in full names where the source gives them).
- `&` before the last author **in the list** (the list keeps &; only running text uses "and").
- Journal article: `Author, First & Author, First. YEAR. Title in sentence case. *Journal Name* Vol(issue). pp–pp.` (volume(issue), then a **period**, then inclusive pages; no "pp.").
- **Do not** abbreviate journal/series/publisher/conference names — ✓ paper already uses full journal names.
- **No "et al." in entries**, **no em-dash** for repeated authors, list **all** authors — ✓ paper's `.bib` already lists all.
- Books: place **and** publisher — ✓ (Moreau: Genève: Métropolis; Grimmer: Princeton: Princeton University Press).
- Titles sentence-case — ✓ (biblatex-apa already does this; capital protection verified).
- **French/German/Spanish/Italian titles are exempt from translation** — ✓ our French titles stay as-is (no bracketed English gloss needed).
- `edn.` for edition; full digits in page ranges.

Implementation: a `biblatex-unified` package implements this style but **is not installed in our TeX tree** (verify on CTAN / install, or hand-format). With only 26 references, hand-formatting to Unified is tractable. Mouton typesets from the manuscript, so the submitted PDF/source just needs to render in Unified format.

## Formatting (Mouton style sheet)

- **Headings:** numbered, flush left, **sentence case** (only first word + proper nouns capitalized), never start at 0. — ✓ all section titles comply.
- **Abstract: ~200 words.** — ✗ currently **225**; trim ~25.
- **Small caps must not be used for emphasis; key terms go in *italics* at first mention, roman after.** — ✗ our `\term{}` renders **small caps** (5 uses in §2: the five units). Redefine `\term` to italic for this venue (house-style-vs-Mouton conflict; Mouton wins for submission).
- **Quotations:** rounded double quotes, <60 words run-on. — ✓ (`\enquote`).
- **Dashes:** spaced **em-dash** for parentheticals; unspaced **en-dash** for number ranges. — ✓ by absence (paper uses commas/parens for all asides, en-dash ranges; no parenthetical dashes, so the house no-em-dash rule doesn't collide).
- **Tables:** caption **above**; **Figures:** caption **below**; number consecutively; don't end the line before a float with a colon; line art ≥1200 dpi (our DAG is vector ✓), photos ≥300 dpi; colour free. — ✓ table captions above, figure caption below, vector figure.
- One space after punctuation; brackets-within-brackets → square.
- Interlinear examples → Leipzig glossing — N/A (no glossed examples).

## Publisher policies — confirm from CLLT Instructions for Authors `?`

(Style sheet is formatting-only; these live in the IFA, which blocked automated fetch.)

- **Anonymization / double-blind:** most De Gruyter linguistics journals require an anonymized manuscript. — Produce a **blinded version** (strip author, ORCID, affiliation, email, acknowledgements incl. the AI statement; check self-citations and the `simulations/` paths don't deanonymize). "the present author" already avoided.
- **Generative-AI disclosure:** De Gruyter requires disclosure; AI cannot be an author. — We have an acknowledgement; confirm required wording/placement.
- **Data/code availability:** deposit the three seeded `simulations/*.py` scripts (public repo / supplement) and add an availability statement.
- **ORCID** present ✓; **keywords** present ✓; competing-interests / funding statements as required.
- **Length:** style sheet says "as stipulated by the editor"; a Mouton page ≈ 3000 characters, so our ~9,000 words ≈ ~18 Mouton pages — within normal CLLT research-article range; no hard cap found, but confirm in the IFA.

## Action list for a CLLT submission

1. Reformat references + in-text citations APA → Unified Style Sheet (biggest task).
2. Trim abstract 225 → ~200 words.
3. `\term{}` small caps → italics.
4. Produce an anonymized manuscript for double-blind review.
5. Data/code availability statement + deposit the simulation scripts.
6. Cover letter foregrounding the **methodological** contribution (not a French-feminization finding), pre-empting the policy-scope exclusion.
7. Confirm `?` items against the CLLT Instructions for Authors before submitting.

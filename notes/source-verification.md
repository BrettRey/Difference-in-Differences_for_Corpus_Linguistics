# Source Verification Queue

Do not add citations or BibTeX entries from the seed note until each item has been checked against an authoritative source.

## Candidate Application Sources

- Langen on judicial language after MeToo.
- Dunn on COVID-era bias in digital corpora.
- Sky et al. on tweets around marriage-equality acts.
- Zhao on generative-AI effects in EFL thesis writing.

## Candidate DiD Methods Sources

- Sun and Abraham on dynamic treatment effects in event studies.
- Callaway and Sant'Anna on DiD with multiple time periods.
- Borusyak, Jaravel, and Spiess on imputation-based DiD.
- Baker, Larcker, and Wang on staggered DiD implementation choices.

## Candidate Corpus Resources

Named in the worked example (Section 8) and outcome discussion; prose mentions are illustrative and currently carry no `\citep`. Verify and add a citation at polish, or keep informal.

- **Swiss Federal Assembly, _Bulletin officiel_ / _Amtliches Bulletin_** (rung 3 data home). Web search (parlament.ch) indicates a digitized run covering 1891--1999, trilingual (French/German/Italian), one institution. TO VERIFY: exact digitized coverage and access terms; whether the French-language portion is separable and large enough for the 1991 window; whether and when the official transcription convention on feminine forms changed (this is the rung's central confound, so it needs a dated, sourced answer, not an assumption).
- **ParlaMint (CLARIN)**, comparable parliamentary corpora. Web search confirms ~29 countries/regions, France and Belgium included, Switzerland NOT included, coverage roughly 2015 onward (≈1B+ words 2015--2022). Implication already used in prose: ParlaMint misses every policy shock (1986/1991/1993/1998) by ~two decades, so it's no use for the historical DiD. If cited, use the ParlaMint corpus paper (Erjavec et al., _Language Resources and Evaluation_); confirm author list, year, volume, DOI before adding to `references-local.bib`.
- **France, _Journal officiel_ / Assemblée nationale and Sénat _comptes rendus_** (parliamentary analogue). Historical débats digitized (Gallica/BnF; recent on the Assemblée open-data portal). TO VERIFY: whether a clean, comparable corpus exists for the 1986--1998 window before relying on it; do not name a specific French parliamentary corpus until checked.

## Adoption Dates and Instruments (load-bearing for the worked example)

Two external reviewers flagged these as empirical claims that must be source-checked (source-grounding LAW), not asserted from memory. Verify each against Burnett & Bonami (2019) and primary policy documents before polish:

- Québec 1979 (feminine-titles endorsement; OQLF).
- Suisse romande 1991 (Federal Chancellery non-sexist-language report + Moreau dictionary).
- Belgium 1993 (décret feminizing names of professions/titles/functions).
- France 1986 (Fabius circular). Reviewer note: tight against Fabius's March 1986 departure as PM, so the date and attribution need checking.
- France 1998 (Jospin circular).
- Swiss _Bulletin officiel_: confirm the multilingual record actually supports the rung-3 design, and pin the key transcription-convention change date (the rung's central confound).

## §7 Citations to Verify Before Keying (few-cluster inference + functional form)

Both reviewers asked for the standard few-cluster toolkit and a functional-form result. NONE are in `references-local.bib`; do not key from memory:

- Wild cluster bootstrap -- Cameron, Gelbach & Miller (bootstrap-t for few clusters).
- Randomization inference for few clusters -- MacKinnon & Webb.
- Functional-form sensitivity of parallel trends -- Roth & Sant'Anna, "When Is Parallel Trends Sensitive to Functional Form?" (surfaced in the Q3 search as Econometrica 2023; verify exact volume/pages/doi). Distinct from the RothSantAnnaBilinskiPoe2023 review already keyed.

## Verification Requirements

- Confirm author list, year, title, venue, DOI or stable URL, and page/article identifiers.
- Prefer journal, publisher, DOI, arXiv/NBER, author, or institutional pages.
- Add entries to `references-local.bib` only when the central bibliography lacks a verified key.

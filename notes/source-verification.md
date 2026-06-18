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

## Adoption Dates and Instruments — VERIFIED 2026-06-17

All checked against authoritative/primary sources (retrieved, not asserted from memory). **Every date in the prose is correct; no corrections needed.**

- **Québec 1979** — VERIFIED. OQLF's first _avis de recommandation_ on feminine job titles, 1979 (OQLF Vitrine linguistique; Conseil supérieur de la langue française). Québec is the recognized francophone first-mover; a second avis followed in 1981.
- **Suisse romande 1991** — VERIFIED. Federal Chancellery report _La formulation non sexiste des textes législatifs et administratifs_, published June 1991 in all three national languages (interdepartmental working group set up 1988). Moreau, _Dictionnaire féminin-masculin des professions, des titres et des fonctions_, Genève, Métropolis, 1991 (Moreau1991, keyed). The federal + trilingual scope also corroborates the rung-3 design.
- **Belgium 1993** — VERIFIED. Communauté française de Belgique, _Décret du 21 juin 1993 relatif à la féminisation des noms de métier, fonction, grade ou titre_ (axl.cefan.ulaval.ca; languefrancaise.cfwb.be). Implementing arrêté end-1993; guide _Mettre au féminin_ early 1994; superseded by a 14 Oct 2021 décret (outside the window).
- **France 1986** — VERIFIED (primary). Laurent Fabius (PM), _circulaire du 11 mars 1986_ (Légifrance JORFTEXT000000866501); rules annexed by the Roudy/Groult commission. Fabius's government fell days later (16 March 1986 elections), so the circular went unenforced — this STRENGTHENS the paper's near-null/negative-control framing (R1's "tight against his departure" worry resolves in the paper's favour).
- **France 1998** — VERIFIED (primary). Lionel Jospin (PM), _circulaire du 6 mars 1998_ (Légifrance JORFTEXT000000556183), explicitly recalling the never-applied 1986 circular.
- **Dawes 2003** — RESOLVED. _Ethnologies_ 25(2): 195--213, doi 10.7202/008054ar (Érudit). Page range + DOI added to Dawes2003; "verify before polish" note removed.

PRIMARY-SOURCE CITATIONS — DONE 2026-06-17. Added `@misc` entries, cited each at first mention: oqlf1979 (_Gazette officielle du Québec_ 111(30): 7394--7395, 28 July 1979; §8 rung 2), belgique1993decret (_décret du 21 juin 1993_; §8 rung 2), chancellerie1991 (Federal Chancellery 1991 report, Berne; §8 rung 1), france1986circ + france1998circ (Légifrance JORFTEXT...866501 / ...556183; §3). France keeps BurnettBonami2019 as a secondary anchor.

STILL OPEN (corpus-data, not blockers): the Swiss _Bulletin officiel_ coverage is now firmed — published since 1891 and digitized, but FULL VERBATIM debates only from 1971 (referendum-decree proceedings only before that); the 1991 window sits safely inside the full-text era (rung-3 prose updated to say "digitized from 1891 and carrying full verbatim debates from 1971"). The dated transcription-convention change (rung 3's central confound) remains an archival question the analyst must settle; the prose correctly treats it as a diagnostic to run, not an asserted date. The French _comptes rendus_ question is moot: rungs 1--2 use edited newspapers, not parliamentary records.

## §7 Citations to Verify Before Keying (few-cluster inference + functional form)

Both reviewers asked for the standard few-cluster toolkit and a functional-form result. NONE are in `references-local.bib`; do not key from memory:

- Wild cluster bootstrap -- Cameron, Gelbach & Miller (bootstrap-t for few clusters).
- Randomization inference for few clusters -- MacKinnon & Webb.
- Functional-form sensitivity of parallel trends -- Roth & Sant'Anna, "When Is Parallel Trends Sensitive to Functional Form?" (surfaced in the Q3 search as Econometrica 2023; verify exact volume/pages/doi). Distinct from the RothSantAnnaBilinskiPoe2023 review already keyed.

## Verification Requirements

- Confirm author list, year, title, venue, DOI or stable URL, and page/article identifiers.
- Prefer journal, publisher, DOI, arXiv/NBER, author, or institutional pages.
- Add entries to `references-local.bib` only when the central bibliography lacks a verified key.

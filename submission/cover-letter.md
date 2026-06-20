# Cover letter — CLLT submission

*Draft. Review and personalize before sending; the editors' names can go in the salutation if known.*

---

June 2026

To the Editors, *Corpus Linguistics and Linguistic Theory*

Dear Editors,

I'm submitting "Difference-in-differences for corpus linguistics: Causal inference, corpus composition, and linguistic change after shocks" for consideration as a methodological article.

The paper carries difference-in-differences, the standard tool in applied economics for reading a causal effect off a before-and-after comparison, into corpus linguistics, and works out what its assumptions become for a diachronic corpus frequency. The central move is to treat a corpus frequency not as a population rate but as a population rate plus a composition-and-measurement term. A causal reading then needs parallel trends to hold twice over, in the underlying rate and in the corpus filter, and the paper makes that split operational: it shows which part of the filter reweighting can remove and which part, hidden drift, defeats identification. A pre-specified decision ladder routes each result to one of four verdicts, and a failure-map simulation reports when the diagnostics fail (false positives under hidden drift, false negatives under thin data), not only when they work.

A worked example, the feminization of profession nouns under francophone language policy, runs through the paper. It's a teaching vehicle for the method, not an empirical finding: the case is built so that its honest verdict is often that the effect cannot be identified, which is the point. The contribution is methodological hygiene for causal claims from corpus data, not a result about French.

I think CLLT is the right home because the paper sits at the intersection of corpus data and linguistic theory: it brings causal-inference discipline to diachronic corpora while respecting the linguistic realities of change, S-curve diffusion, actuation, and register. The argument is grounded in the corpus-methodological literature on representativeness, sampling frames, and comparability, and in corpus work on prescription and usage.

The simulations are reproduced by three short, deterministic Python scripts (standard library only, fixed seeds), included as supplementary material. I used large language models (Claude Opus 4.8 and OpenAI Codex) as drafting and editing aids in preparing this manuscript; I'm responsible for all theoretical claims, arguments, errors, and interpretive choices. The work is original, single-authored, and not under consideration elsewhere.

Thank you for considering the manuscript.

Sincerely,

Brett Reynolds
Humber Polytechnic & University of Toronto
brett.reynolds@humber.ca
ORCID 0000-0003-0073-7195

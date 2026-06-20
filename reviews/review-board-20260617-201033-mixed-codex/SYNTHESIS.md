# Mixed board synthesis (non-redundant) — 2026-06-17

Full complete-draft review. Five seats, each reviewed once. **Opus:** Keith, Gelman, Eisenstein. **Codex:** Roth, Cunningham.

## Verdicts (note the cross-model split)
- Opus: Keith **Minor**, Gelman **Minor**, Eisenstein **Minor**.
- Codex: Roth **Major**, Cunningham **Major**.

Same substance, different severity weighting. Codex treats the estimand ambiguity as a blocker ("Major"); Opus treats the same issues as fixable-without-re-architecting ("Minor"). Both are right in their own terms: the estimand tension is conceptually central but bounded in effort.

## Cross-model consensus (flagged by BOTH models)

1. **Lock the estimand (THE conceptual fix).** §2's three-way decomposition says the target is the effect on the population rate π, but also says the policy-induced shift in the corpus filter (T→C→f) is "part of what the policy did," so don't reweight it away. Roth + Cunningham (Codex) and Keith (Opus): if the target is population usage π, then T→C→f is NOT part of that estimand — it's a different (edited-output) estimand. The paper must pick one and say so once. Remedy (Cunningham): a per-rung **estimand ledger** — target / treatment / control / time window / outcome / identifying unit / clustering unit / direct-vs-total. Keith: pin the population denominator for π (it drifts across rungs).

2. **Ground the simulation numbers (UNANIMOUS 5/5).** §8.3's "+0.13", "false-positive past half", "missed more than nine in ten" appear in prose with no DGP, table, or code pointer — a violation of the paper's OWN source-grounding rule. The sims exist in `simulations/`, but a reader can't see that. Remedy: a simulation table/appendix (DGP, params, threat varied, estimand, ladder verdict, failure rate), ideally Quarto so the numbers can't drift. Remove the §8 `% TODO` "simulation spine" that makes the work read as unbuilt.

3. **Diagnostics ladder under-operationalized (Roth + Gelman-adjacent).** "Plausible confound", "breakdown value beyond any plausible drift", "pre-committed non-policy margins" need concrete calibration rules, or the ladder is principled language without reproducible decisions.

4. **§7 inference remedies slightly overconfident (Roth + Gelman-adjacent).** Wild cluster bootstrap and randomization inference are not generic fixes for 4–5 politically-selected clusters (RI needs an assignment model; WCB fragile). Temper §7.

## Distinctive single-seat points (keep)
- **Gelman (Opus):** the §7 "why DiD not a multilevel model" paragraph OVERSTATES — the paper itself says no estimator removes selection-into-timing, so DiD doesn't difference the trend confound away either. Honest argument = transparency/convention, not structural testability. Also: the SECOND parallel-trends assumption (in b) is untestable in the weak pre-period sense the first enjoys, because π is latent — state this.
- **Eisenstein (Opus):** feminization is gradual logistic diffusion, so parallel pre-trends essentially never hold and "not identified" is the modal verdict BY CONSTRUCTION of the phenomenon. State that step-change is a precondition on the linguistic CHANGE, not just the policy. Promote author/topic dependence (leave-one-author-out alongside leave-one-source-out) and per-strategy *relative timing* (strategies are ordered: epicene agreement early/low-cost, novel derivation late/high-cost) to first-class diagnostics.
- **Keith (Opus):** outcome/confounder non-separability — the Madame+title cue that conditions the outcome tracks the very composition b is meant to absorb; when outcome and confounder come from overlapping text, the b parallel-trends assumption becomes untestable in exactly the cases that matter.
- **Cunningham (Codex):** rung 3 isn't as executable as rungs 1–2 (stops at the measurement threat, doesn't apply the ladder with treatment/control/counterfactual). Complete it or label it an extension.

## Non-issue (Codex artifact)
Both Codex seats flagged `weinreich1968` and `tagliamontedarcy2007` as "not in references-local.bib / need verification." They ARE in the central `references.bib` and resolve fine (the Opus seats verified this). Artifact of telling Codex to treat references-local.bib as the verified set. No action.

## Self-check
Convergence on (1) and (2) is genuine (concrete verifiable gaps), not stereotyped agreement. The Opus/Codex verdict split is real and preserved, not collapsed. Don't read 5/5 on the sims as "the field agrees" — it's that an un-sourced number in a source-grounding paper is an obvious target.

## Prioritized fixes
1. Lock the estimand + per-rung ledger (resolves Roth, Cunningham, Keith). Conceptual, central.
2. Ground the sims in a table/appendix (unanimous; surfaces existing `simulations/`).
3. Fix the §7 multilevel overclaim + state the b-assumption's untestability (Gelman).
4. Temper §7 inference remedies (Roth).
5. Operationalize the ladder thresholds (Roth).
6. Name the diffusion-shape precondition + author/topic dependence + per-strategy timing (Eisenstein).
7. Keith non-separability paragraph (§4/§5).
8. Rung 3: complete or label as extension (Cunningham).

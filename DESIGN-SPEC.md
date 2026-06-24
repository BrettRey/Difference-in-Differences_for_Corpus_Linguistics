# Design Spec — Difference-in-differences for corpus linguistics

Working blueprint, v2 (2026-06-17). Supersedes v1. Source: the decisions in `DECISIONS.md`,
the feminization and methods intakes, and three advisory-board rounds. **North star: the
paper improves methods. It teaches corpus linguists how to reason about causal claims from
corpus data. The worked examples are vehicles for that, not empirical findings to defend.**
Items marked **[open]** need resolution before the relevant section is drafted.

## 1. Contribution

Corpus linguistics routinely makes causal claims about language change from before/after
frequency comparisons with no credible counterfactual. This paper imports difference-in-
differences (DiD) as a discipline for such claims and shows what must be added to make it
work for corpora: a measurement layer connecting corpus frequency to a population quantity;
an identifying assumption stated about the composition-induced bias rather than the rate;
and diagnostics that survive the fact that corpus composition contaminates the very pre-trend
test meant to detect it.

The empirical spine is a **progressive build** of designs on one phenomenon, the feminization
of profession nouns under language policy: start with the simplest honest design, add
complexity, and watch the threats accumulate. The deepest lesson is not any single design but
**design choice**, what each strategy holds constant, what it identifies, and where it
honestly stops identifying. No worked example claims a definitive feminization finding; each
exists to make a methodological point concrete and falsifiable.

## 2. Estimand

- **Target (a):** the change in a feature's rate of use in a *population*, attributable to a
  shock. Not the rate among corpus contributors, not the corpus's textual composition.
- **Decomposition:** for variety v at time t, observed corpus rate `f_vt = π_vt + b_vt`, where
  `π_vt` is the population rate and `b_vt` is composition/measurement bias (who is in the
  corpus, which referents/professions are discussed, and the editing operator applied after
  production).
- **Identifying assumption:** DiD differences out `b` only if `b` has parallel trends across
  treated and control. So the assumption is **parallel trends in `b`**, not in `π`.
- **`b` is unobservable, so make the assumption falsifiable through proxies.** Track the
  measured composition margins (profession mix, outlet mix, register, author cohort,
  auto-detected female-referent share), each as its own outcome through the event window. A
  jump at the policy date is differential drift in `b` you can see: a placebo-on-the-
  confounder. Reweight/post-stratify to these margins before differencing; the residual
  assumption is "no unmeasured differential drift in `b`."
- **Two estimands, bound to two series (round 3).** Edited press identifies *use in the edited
  written standard* (`π + b` with the editing operator still inside). *Population use* is
  claimable only from spoken/lightly-edited corpora. State which corpus supports which; never
  let a press ATT wear the population label.
- **One sensitivity envelope.** The ideology-confounder violation and the reweighting-residual
  violation are both bounded parallel-trends violations. Put them in a single Rambachan-Roth
  envelope; do not report a tight CI from reweighting beside a separate bound from ideology.

## 3. Architecture (the fork, resolved)

Two layers, not rivals:
- **Identification design:** DiD (keeps the causal claim auditable for a linguistics audience).
- **Estimator within it:** a hierarchical count / reweighting model (overdispersed counts,
  token dependence, crossed random effects for outlet/author, composition reweighting).

DiD supplies the comparison and the assumption; the model supplies estimation and honest
uncertainty. Adding random effects does **not** solve identification, and the paper says so.

**Partial pooling for unequal and small corpora.** The estimator is a multilevel (partial-
pooling) model: shrinkage / borrowing strength, the random-effects estimator's quasi-demeaning.
Most cells (variety x period x profession x outlet) are sparse, so partial-pool the *nuisance*
dimensions (outlet, profession, period within a variety) and a small corpus like Suisse romande
or Ticino borrows strength from the larger ones instead of contributing pure noise or being
dropped. But keep **fixed effects at the variety/treatment level**: variety effects are
correlated with treatment timing (selection-into-timing), so pooling them away would reintroduce
the bias fixed effects blocks (the random-effects-vs-fixed-effects / Hausman tradeoff). Shrink
within varieties, fix across them. Scope: partial pooling cures small-corpus *noise*, not the
few-clusters identification/inference problem; with ~4-5 varieties the variety-level variance is
barely estimable and the shrinkage is itself uncertain (Gelman's caution), so it pairs with the
randomization null, it does not replace it.

**Inference posture.** With few units the standard error attaches to the *variety*, and the
claim is a structured case-comparison-with-bounds, not a powered estimate. Cluster-robust SEs
at a handful of clusters are anti-conservative (Bertrand-Duflo-Mullainathan); say so rather
than disclose it as a caveat.

**Claim discipline (the decision ladder).** Diagnostics earn their keep only if they can change
the conclusion, so each design states in advance what each verdict permits: a point or bounded
estimate, a descriptive reading only, or *not identified*. Rung 1 instantiates this and every
later rung inherits the rule. For a methods paper this is the payoff: it teaches readers when
they may claim what, not only which tests to run. (Unanimous ask of the v2 Codex board.)

**Egami split-sample applies only where a learned classifier does.** The primary outcome is a
hand-detectable agreement feature, which carries no learned-representation bias, so split-
sample is not needed there. It earns its place only if referent gender is detected with a
trained model (name-gender or coreference) beyond the `Madame`-trigger window.

## 4. The six core questions (answered per rung)

1. **Treatment/shock:** an official language-policy endorsement of feminization, dated.
2. **Unit of identifying variation:** the variety (polity), not the token; but test whether it
   is really the outlet (see 6.5, two-outlet diagnostic).
3. **Outcome measured:** proportion of feminine grammatical marking on profession/title nouns
   referring to women (strategy-agnostic; see 6.4).
4. **Comparison series:** a same-language control (rung 1) or not-yet-treated varieties
   (rung 2).
5. **Corpus-specific threat:** composition drift in `b` correlated with the policy, plus
   cross-unit interference and the ideology confounder.
6. **Diagnostic:** policy-time vs calendar-time test, composition-margin placebos, the AFP
   shared-wire check, the two-outlet check, Rambachan-Roth bounds.

## 5. Simulation (the spine, validate against known truth)

A population estimand can only be validated where the truth is known.
- Set a true population trajectory `π_vt` (logistic adoption) for treated and control
  varieties.
- **Test acceleration, not just a level shift.** If `π` is logistic and the policy is a
  waypoint on the curve, a level ATT mis-specifies the estimand; estimate a change in
  slope/hazard. (v1 imposed a logistic `π` but tested a level ATT; that inconsistency is now
  the first thing the simulation surfaces.)
- **Arms:** benign (b drifts in parallel across varieties), malign-rate (b drifts
  differentially), malign-strategy (the morphological-strategy *mix* drifts differentially
  while the rate does not), interference (treatment in one variety bleeds into controls via a
  norm-deference parameter), and null (treatment randomly reassigned or the data scrambled),
  on which an honest procedure must recover no effect.
- **Show:** naive DiD recovers `π` in the benign arm and is biased in the malign arms;
  reweighting recovers it for measured-margin drift and fails for unmeasured drift; a flat
  pre-trend can co-occur with a biased estimate; the strategy-agnostic outcome can misread a
  strategy-mix shift as a rate effect; interference biases the ATT toward zero; and the
  diagnostics in 6.5 flag the malign cases.
- Deliverable: the figure that makes the whole thesis legible before any real data.

## 6. The progressive build on French feminization

The point of the build is the design-choice lesson: each rung adds complexity and a new
threat, and the paper is honest about what each identifies.

### 6.1 Rung 1 — Swiss French vs France (the clean 2x2 core)

- **Design:** treated = Suisse romande press (Swiss feminization guidance, Moreau/Geneva,
  ~1991 **[open: operative federal/cantonal date]**); control = France press (not yet
  effectively treated until ~1998). Suisse romande leads France, so this is a clean
  treated-leads-control contrast.
- **Why it is the cleanest core:** same language, so the morphological-comparability problem
  is small (Switzerland leans on `-esse`, France resists, but both draw on the same French
  feminine resources, a far smaller gap than across languages). The control is a large,
  well-corpus'd same-language population. The continental gender-ideology wave is *shared*
  between the two, so it differences out if common, which is defensible for adjacent same-
  language populations.
- **The identifying contrast (policy-time vs calendar-time):** does Suisse romande *diverge
  from France* after the Swiss policy, or merely track Paris? Divergence on the policy date is
  a policy effect over and above the wave; co-movement in calendar time is the wave, not the
  policy (and that is still an identified, publishable reading).
- **Signature threat: SUTVA.** Suisse romande reads French media and the AFP wire, so the
  control is not insulated from the treated unit. This is the cleanest place to *teach*
  interference, with the AFP/shared-wire diagnostic (measure shared-wire content, exclude it,
  or use it as an interference probe).
- **Inference:** two groups, so the honest object is a structured comparison with bounds, not
  a powered estimate. Introduce few-clusters honesty here, cheaply, at the simplest rung.

### 6.2 Rung 2 — Scale to staggered multi-variety (what scaling costs)

- **Design:** add Québec (1979) and Belgium (21 June 1993); treatment timing now varies, so
  use Callaway-Sant'Anna group-time ATTs with not-yet-treated controls; cite Goodman-Bacon and
  de Chaisemartin-D'Haultfœuille for the TWFE-fails diagnosis and Sun-Abraham / Borusyak as
  robustness.
- **What scaling imports, and the lesson:** more units is not more identification when the
  units are confounded or interfering. Specifically:
  - *Cross-country confounders:* each variety is now a different polity with its own politics,
    media system, and economy.
  - *Morphological-strategy divergence (Dawes):* Québec `-eure`, Belgium epicene, France
    resist. The strategy-agnostic outcome buys comparability at the cost of a measurement-
    invariance assumption; state it and test it in the simulation (6.4, 5).
  - *Few clusters (~4-5):* C-S uniform bands and cluster-robust SEs do not hold; randomization
    inference has a tiny reference set.
  - *Selection into treatment timing:* which polity adopts when is plausibly selected on the
    same ideology that drives usage, so not-yet-treated controls ride the same wave. Rambachan-
    Roth bounds a violation magnitude; it does not fix selection into timing.
- **Diagnostic that rung 2 turns into content:** the policy-time vs calendar-time test across
  varieties, and the **France 1986-null as the primary internal-validity placebo** (an
  identical policy with no ideology behind it produced no jump; that is the design's logic made
  visible). Treat France's 1986/1998 contrast as the placebo, not a nuisance.

### 6.3 Rung 3 — Trilingual within-Switzerland (the design-choice contrast)

- **Design:** one federal policy, one polity; compare feminization across the French, German,
  and Italian Swiss communities, each also paired with its metropole (Romandie/France,
  Ticino/Italy, Swiss German/Germany).
- **What it uniquely buys:** it holds country-level confounders constant (politics, economy,
  federal policy, media regulation) and varies the language, which the cross-national rungs
  cannot. This is the direct answer to rung 2's selection-into-timing problem: there is no
  "which country adopts when" to be selected, because one federal act treats all three at once.
- **The lesson:** confounder control is a *design choice*, not just an estimator choice.
- **Costs, stated honestly (so this stays a compact design illustration, not a full build):**
  trilingual corpora and competence **[out of scope to execute fully]**; severe cross-language
  morphological non-comparability; and a pull toward a *linguistic* finding (morphology drives
  uptake) that is off the north star. Present the design and what it would control; do not
  promise a trilingual empirical result.

### 6.4 Outcome definition (shared across rungs)

- **Variable:** for a fixed list of profession/title nouns referring to women, the proportion
  with feminine grammatical marking.
- **Strategy-agnostic (Dawes):** count any feminine marking (feminine article/agreement or
  feminine noun form). Report a form-specific secondary analysis. State measurement invariance
  as an explicit assumption and test it in the simulation.
- **Auto-detection (B&B / Fujimura):** restrict to contexts where the female referent is
  independently flagged (terms of address *Madame* + title; or a feminine given name within a
  window), so the *le/la* or form alternation identifies feminization without hand-coding
  referent gender.
- **Choice set:** simple feminization (feminine marking vs masculine-as-generic) is the primary
  variable; inclusive-writing variants (midpoints, doublets) are a separate, stance-driven
  phenomenon (Simon & Vanhal), analyzed separately.
- **Noun list (prestige-stratified, per B&B/Fujimura):** ministre, député(e), président(e),
  secrétaire d'État, garde des sceaux, avocat(e), auteur(e/trice), professeur(e), médecin,
  écrivain(e), directeur/directrice. **[open: finalize]**

### 6.5 Threats and diagnostics (the curriculum)

| Threat (round 3) | What it teaches | Diagnostic |
|---|---|---|
| Policy timing endogenous to ideology | distinguish an intervention from a secular wave | policy-time vs calendar-time test; France 1986-null placebo |
| Cross-unit interference (SUTVA): shared media, AFP wire, norm-deference | corpus "units" are often not independent | measure/exclude shared-wire content; simulation interference arm |
| Editing operator inside `b` | corpus frequency is not population usage | split estimands; spoken/lightly-edited triangulation as a required co-primary series with a decision rule |
| Unobservable `b` | identify what you can falsify | composition-margin placebo tests |
| Few clusters (~4-5) | honest uncertainty with few units | attach SE to variety; report a structured comparison with bounds |
| Onset vs acceleration | match the estimand to how change moves | plot raw series; test slope/hazard change, not a level jump |
| Outlet vs variety | find the real identifying unit | two-outlet within-variety check (e.g. Le Monde vs Le Figaro at 1998) |
| Parallel-trends violation magnitude | bound, do not assert | Rambachan-Roth in breakdown mode (sweep the violation size; calibrate from B&B, not from contaminated pre-trends), ideology and reweighting-residual in one envelope |
| A procedure manufacturing an effect from nothing | find nothing where nothing is | randomization null: permute treatment / scramble labels (also the inference when clusters are few) |

### 6.6 Relationship to prior art (what we add)

- **Burnett & Bonami (2019):** within-France GLMM, parliamentary speech, ideology explanation,
  no cross-variety control, not framed as DiD. We add cross-variety controls, composition
  reweighting, and sensitivity-bounded conclusions, and we reuse their *Madame le/la N*
  measurement trick. Their 1986-null/1998-dramatic result is our placebo and our central
  cautionary lesson about endogenous timing.
- **Fujimura (2005):** descriptive French press trends, prestige resistance. We add
  identification.
- **Dawes (2003):** qualitative cross-variety comparison; source of both the comparability fix
  and the comparability threat.
- **Funtek (2014):** France/Québec press comparison (full MA thesis OA, **[open: read]**).

## 7. Italian single-shock (the sharper-event contrast)

- **Treatment:** Sabatini 1987 (government-commissioned *Raccomandazioni*), a sharp, datable
  event, unlike the diffuse French policies.
- **Corpus:** la Repubblica 1985-2000 (~325M words) brackets the shock with a real pre-period
  and article-level resolution; CORIS/DiaCORIS for longer span.
- **Role:** the cleaner *positive* demonstration (Gelman), with less obvious ideology
  co-movement than France's parité-era jump. Control = a within-Italy never-targeted feature or
  the pre-trend; honest that it is edited press. Nouns: ministra, deputata, sindaca, avvocata,
  ingegnera.

## 8. Croatian/Serbian (the breakdown case)

- **Shock:** the 1991 Yugoslav breakup plus Croatian purism (strong in the 1990s, weaker after
  2000).
- **Why it breaks:** the rupture reshapes the corpus-generating environment (new outlets,
  wartime sampling, changed press) at the same time as the language, so differential
  composition drift is maximally confounded with the treatment, and there is no off-the-shelf
  matched pre-1991 corpus.
- **What it teaches:** the signature threat at full strength, and that the corpus record itself
  can be disrupted by the shock. The limiting case, not a positive result.

## 9. Generalization and limits

- **Design-choice throughline:** the same phenomenon, attacked by increasingly demanding
  designs, with an honest account of what each identifies. That is the paper's deepest
  methodological contribution.
- **Francophone Africa:** not a clean control (no domestic policy plus Paris norm-deference;
  thin diachronic corpora; elite-writer vs multilingual-population gap). Use as the
  limits/external-validity discussion and the treatment-vs-norm-authority wrinkle.

## 10. Section mapping (to the nine-section outline)

- **01 Problem:** causal claims from corpus frequency without counterfactuals; the naive
  before/after as the thing to fix.
- **02 DiD estimand:** section 2 (population vs edited-standard estimands, the `f = π + b`
  decomposition, the falsifiable form of parallel-trends-in-`b`).
- **03 Treatments/shocks:** policy endorsements; discrete vs diffuse (onset vs acceleration);
  endogenous timing and the ideology confounder.
- **04 Outcomes:** the 6.4 outcome definition and measurement model.
- **05 Identification threats:** the 6.5 curriculum; text-as-confounder (Keith, Egami, Feder).
- **06 Diagnostics:** policy-vs-calendar-time, composition-margin placebos, AFP and two-outlet
  checks, Rambachan-Roth.
- **07 Modern DiD choices:** Callaway-Sant'Anna; Goodman-Bacon and dCDH diagnosis; Sun-Abraham
  / Borusyak robustness; BDM inference; the few-clusters honesty.
- **08 Worked example:** the simulation, the progressive build (rungs 1-3), Italian, and
  Croatian/Serbian.
- **09 Conclusion:** the credibility upgrade for corpus causal claims; design choice as the
  contribution.

## 11. Open items

**Cleared this session:**
- **Rung 1 Swiss date = 1991** (Swiss Federal Chancellery report on non-sexist administrative
  language; Moreau's professions dictionary). France effective 1998 (Jospin), per B&B.
- **Swissdox depth confirmed:** Swissdox@LiRI holdings reach back decades (from 1911); the
  *Le Temps* archive carries its predecessors *Journal de Genève* / *Gazette de Lausanne* for
  pre-1991 Suisse romande, so rung 1 is feasible.
- **Québec = 1979** (OQLF avis, *Gazette officielle*, 28 July 1979; 1976 was an informal
  antecedent).
- **France treatment coding = policy date** (estimand = policy effect over and above the
  ideology trend; 1986-null as placebo).
- **Rambachan-Roth and a discrete shock:** R-R's restriction classes (relative magnitudes,
  smoothness) anchor on the pre-period violation, so a confounder arriving discretely *at* the
  treatment date leaves nothing to scale from. Use R-R in **breakdown mode**: sweep the
  violation size and report what ideology shift would overturn the result, calibrating the
  plausible size from external evidence (B&B), not from contaminated pre-trends. This is itself
  a teaching point.
- **Randomization null testing added as a first-class diagnostic** (5, 6.5): permute treatment
  or scramble labels; an honest procedure recovers no effect, and at few clusters this is also
  the inference.

**Still open:**
- Read in full: Callaway & Sant'Anna, Rambachan & Roth, Egami et al.; convert the Funtek thesis
  and the full Flesch, Abbou & Burnett PDF.
- Verify the exact Egami split-sample scope (it applies to learned-representation outcomes, not
  the hand-detectable agreement feature).
- Finalize the profession-noun list and the inclusive-writing exclusion.
- Choose the corpus-access route per variety (Europresse / Eureka / Swissdox licensing).
- Complete and verify the local bib entries (e.g. Dawes page range) before polish.

**Jacob Eisenstein Review**

1. **One-Sentence Summary**

v2 uses feminization of profession nouns as a progressive methods curriculum: start with Swiss French vs France, then add staggered francophone varieties and trilingual Switzerland, so each design choice exposes a different causal threat in corpus DiD.

2. **Does v2 Resolve My Round-3 Concern?**

**Partly.** It gets the right lesson: language change diffuses through media, institutions, and prestige networks, so SUTVA is not a footnote. The AFP/shared-wire diagnostic and simulation interference arm are real improvements. But they still mostly confront **direct content sharing**, not the broader diffusion process: journalists, style guides, Paris norm-deference, metalinguistic debate, and shared professional norms can transmit treatment without leaving an AFP flag.

The missing premise is: observed shared-wire content captures the relevant spillover channel, or unobserved spillovers are small enough to bound. That premise is not yet stated or defended.

3. **Still Wrong or Underspecified**

- **SUTVA is diagnosed, not yet modeled.** Excluding AFP copy can show whether duplicated text drives the result, but it does not solve latent norm diffusion. Treat AFP share, French-media dependence, and outlet norm-deference as exposure variables. Otherwise the inference “no Swiss divergence = no Swiss policy effect” is invalid because France and Switzerland are not isolated potential-outcome units.

- **1991 is still treated too much like a step.** The spec says to test acceleration, but rung 1 still says Suisse romande should “pull away” around 1991. The missing premise is that the 1991 endorsement changed the adoption hazard, rather than codifying a trajectory already underway. Rung 1 needs pre-1991 slope/lead checks and an explicit “waypoint vs intervention” decision rule.

- **Outlet vs variety is not resolved.** The design says the identifying unit is the variety, but the draft only partial-pools outlets. That estimates around the problem. The missing premise is that outlet editorial regimes are nuisance variation, not the true treatment channel. Add within-variety outlet replication before claiming a variety-level contrast.

4. **Is Rung 1 Sound as Drafted?**

**Almost, but not yet.** As a teaching baseline, Swiss French vs France is strong: same language, clear comparison, obvious interference threat, and honest edited-standard estimand. But [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:19) overstates the two-group randomization logic. With two varieties, label permutation is a sanity check, not robust inference; random treatment-year shuffling also assumes exchangeability over time, which diffusion violates.

So rung 1 escapes the old problem only if it is framed as a structured diagnostic comparison, not as a clean inferential DiD.

5. **Single Most Important Fix**

Add a rung-1 diagnostic decision table before drafting the remaining rungs:

- local-only Swiss divergence after 1991 = plausible policy-time acceleration;
- Swiss divergence already before 1991 = 1991 is a waypoint;
- divergence only in AFP/shared material = interference/wire diffusion;
- outlet-specific jumps = outlet is the identifying unit;
- France/Switzerland co-move in calendar time = shared francophone wave, not policy.

6. **Verdict**

**Draft once the central fix is made.** The progressive build is the right teaching architecture, but rung 1 must make diffusion, interference, and identifying unit decisions operational rather than just acknowledged.

Source flag: I am relying on the project trail for Burnett & Bonami 2019, Dawes 2003, Moreau 1991, and Bertrand-Duflo-Mullainathan 2004; exact source claims still need final verification before citation polish.
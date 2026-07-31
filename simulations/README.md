# Scripts: the decision ladder, and one archive measurement

Filenames containing `rung` are retained from an earlier draft that built the
worked example in numbered rungs. The article no longer uses that vocabulary;
the names are kept so that outputs archived against them stay traceable. Where
the article says "the simulated two-variety design", these scripts say "rung 1".

Replication code for the results in Section 8 ("Evidence: simulation and a measured filter") of
*Difference-in-differences for corpus linguistics: Causal inference, corpus
composition, and linguistic change after shocks*. A corpus never reveals the
population rate, so these simulations are the one place the design can be checked
against a known truth.

## Requirements

Python 3. **Standard library only** (`math`, `random`, `statistics`) — no NumPy or
other third-party dependencies. Each script is **deterministic**: it fixes a
random seed and prints its results to stdout, so re-running reproduces the
reported numbers exactly.

## Running

    python3 rung1-ladder-sim.py     # routing validation        (seed 12345)
    python3 rung1-recovery-sim.py   # reweighting recovery       (seed 2024)
    python3 rung-failure-map.py     # operating characteristics  (seed 7)

## What each script does

### `rung-failure-map.py` (seed 7) — failure-map table
Operating characteristics of the ladder under messy conditions: 400 replications
per scenario across the realistic failure dimensions (hidden composition/editing
drift *outside* the reweighting strata, small/sparse effects, interference,
selection-into-timing). Reports the misroute rate — false-effect claims (FP) and
missed real effects (FN) — for each scenario. Generates the rates in the
failure-map table and the 56% / 94% / 8% figures quoted in that section.

### `rung1-recovery-sim.py` (seed 2024) — recovery estimates
Does reweighting *recover* the truth, not merely flag the artifact? Three arms: a
real effect (`benign`), a pure composition shift on an observable stratum
(`malign_rate`), and an unobserved within-stratum drift (`malign_unmeasured`).
Produces the naive **+0.13** / reweighted **−0.000** / both-near-**+0.15**
estimates, and the Part-2 check that partial pooling buys no variance at a
the two-period simulated design.

### `rung1-ladder-sim.py` (seed 12345) — routing validation
The earliest, minimal check: under clean/oracle conditions, does the ladder route
five canonical arms (`benign`, `malign_rate`, `interference`, `waypoint`, `null`)
to their expected verdicts? Validates the routing logic before the failure map
stresses it. (Not cited by number in the paper; included for completeness.)

## The decision ladder (shared `verdict()` logic)

Every script applies the same ladder to the reweighted treated-vs-comparison
series, in order, short-circuiting at the first gate that fires:

1. **Pre-trend gate** — if `|slope(treated, pre) − slope(comparison, pre)| > 0.03`,
   return *not identified* (the divergence predates the shock).
2. **Composition gate** — a shift on the pre-committed reweightable margin
   (proxy `> 0.05`) triggers the reweighted estimand and disqualifies the naive
   reading; the reweighted contrast then proceeds down the ladder. Only a shift on
   an *unmeasured or non-reweightable* margin returns *not identified*. That case is
   invisible to the proxy, so in these data-generating processes it surfaces
   downstream as a false *bounded* claim — the failure the `hidden` scenarios map.
   Recovery of the true rate when the shift **is** reweightable (naive `+0.13` →
   reweighted `≈0`) is shown in `rung1-recovery-sim.py`.
3. **Interference gate** — if measured cross-border exposure `> 0.25`,
   *not identified* (interference).
4. **Sensitivity gate** — a reweighted DiD that has cleared the earlier gates but
   sits inside the band `|DiD| ≤ 1.5 × (largest placebo-date contrast) + 0.01` is a
   *bounded null* (an effect too small to separate from zero). Telling a bounded
   null from a *shared wave* needs the calendar-time comparison, which these gates do not perform.
5. Otherwise → *bounded estimate*.

The placebo-date contrasts are computed at non-treatment years (1988, 2000, 2001,
2002). The thresholds are fixed before any run (DGP-tuned, not tuned per
replication); holding them fixed is itself one of the limits the failure map
exposes — a placebo-calibrated sensitivity band cannot see drift confined to
windows the placebos never touch, which is why hidden drift drives the
false-positive rate up. The *descriptive* verdict of the paper's full ladder is a
human judgment (a check that is *ambiguous* rather than passed or failed) and is
not part of the automated routine.

### `speaker-pool-audit.py` — archive measurement, not a simulation

Queries the Swiss Federal Assembly's public OData service for every parliamentary
mandate and reconstructs the composition of the sitting chamber on any date. No
key, no registration, no seed: the numbers come from the archive, so they change
only if the archive does. Produces the speaker-pool table in the article.

Validation is built in. The Nationalrat has held 200 seats since 1963, which the
reconstruction recovers for post-1963 dates, and the 2020 row returns 84 women of
200, matching the reported outcome of the 2019 federal election.

Note it reads `MemberCouncilHistory`, not `MemberCouncil`. The latter stores one
mandate per person and undercounts the chamber badly at older reference dates.

## Reproducing the reported numbers

| Reported in the paper                         | Script                  | Seed  |
|-----------------------------------------------|-------------------------|-------|
| failure-map table                             | `rung-failure-map.py`   | 7     |
| recovery estimates (+0.13, ≈0, +0.15)         | `rung1-recovery-sim.py` | 2024  |
| ladder routing validation                     | `rung1-ladder-sim.py`   | 12345 |

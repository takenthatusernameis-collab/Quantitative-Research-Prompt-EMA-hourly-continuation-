# Research Conclusion — EMA Hourly Continuation

## Program status (2026-10-21T14:25Z)

**The research program is NOT concluded.** It is in the waiting state
`AWAITING_NEW_ELIGIBLE_CANDIDATES`: the current market-cap snapshot
(`mcap_snapshot_20261021_114120`, CoinGecko, 2026-10-21T11:41:20Z) has no
eligible unseen name below the expansion floor (AGLD/USDT, $16 279 472), and
PROMPT.md §2.1.5 forbids a fresh ranking query before
**2026-10-22T11:41:20Z** (24 h refresh bound).

What the evidence says so far:

- **No edge has survived the gates.** Across **17 556 grid cells** (266 symbols
  x 66 EMA pairs, 14.2 M trades, net of costs), the pooled net profit factor is
  **0.5224**; only **36 cells (0.21 %)** reach a full-sample net PF > 1 against a
  ~50 % no-edge null, and every one of them fails the out-of-sample and 2x-cost
  gates. **0 credible candidates.**
- **The pre-registered ATR minimum-risk mutation was run over the whole grid
  and it is a cost-drag repair, not an edge.**
  `results/20261021_125403_grid/` (17 556 cells, same universe, same 66 pairs,
  same cost model; only `min_risk_atr = true, atr_threshold = 1.0` is added)
  lifts the pooled net PF from 0.5225 to **0.7347** and the pooled gross PF
  from 0.8872 to 0.9636, and it cuts the median cell's cost share of its gross
  move from 26.6 % to 13.2 % by widening the median stop from 1.35 % to 2.08 %
  of the entry price. But the yardstick that matters — the pooled **out-of-fold**
  net PF of the selection procedure under the identical walk-forward protocol —
  is **0.7390** (0.5731 under 2x costs) against the parent's 0.6409
  (0.4521). The pre-registered decision rule required above 1.0 on that number,
  so **the mutation is recorded as a rejected mutation**. Artifacts:
  `results/20261021_130500_atr_min_risk_prereg/` (written before the child run
  started), `results/20261021_135500_mutation_comparison/`.
- **The negative result is not an artefact of the selection granularity.**
  `scripts/selection_granularity.py` re-runs the walk-forward with the
  selection unit changed — per symbol (266 selections per step), per
  market-cap bucket (5) or one pair for the whole universe — and with 1, 3 or
  10 cells per unit. The control reproduces the recorded yardstick exactly
  (0.6409), the best granularity of the ladder is 0.6649 for the parent and
  0.8070 for the child, and **no granularity clears PF 1 in either arm**. The
  question "is there an edge at some selection granularity?" therefore has one
  answer at every level of the ladder: no. Artifact:
  `results/20261021_140500_selection_granularity/`.
- **One open thread, and it is the interesting one.** The child does produce
  cells the parent does not: 106 cells clear the grid-wide out-of-sample +
  2x-cost gate (parent: 10) and **10 cells pass the full §3.4 credible-candidate
  gate (parent: 0)**, and 32 of the 108 gate-clearing cells keep a stressed
  out-of-sample PF above 1 at all three window lengths (parent: 0 of 6). That
  is *not* a promotion — 106 of 17 556 is 0.60 % of the grid, the parent's own
  randomized-entry null puts the false-positive rate of the same gate at
  0.04-0.12 % of the grid, and **the child's survivors have not yet been
  through the selection-bias machinery** (child-specific null, family
  concentration, leave-one-symbol-out, walk-forward, candidate check,
  sub-period stability) that the parent's 10 had to pass. That machinery is
  the next leg.
- **The out-of-sample gate now covers the whole grid, not a selected subset.**
  The pipeline used to test only the 36 in-sample winners out of sample, which
  left 17 520 cells unexamined. `scripts/oos_grid_scan.py` applies the same
  out-of-sample window to all 17 556 cells and re-verifies the survivors with
  the real backtest: pooled out-of-sample net PF **0.5299** (0.3267 under 2x
  costs), 77 cells (0.44 %) with an out-of-sample net PF > 1, and **0 credible
  candidates** among the 180 verified survivors (76 exploratory, 104 rejected).
  The 6 closest survivors all have a full-sample net PF below 1 (0.75-0.91)
  and none keeps a stressed out-of-sample PF > 1 at 20 %, 35 % and 50 %
  window lengths.
- **The survivors are indistinguishable from noise.** A randomized-entry null
  (`scripts/null_grid_scan.py`, all 17 556 cells, three null modes run through
  the untouched backtest engine) produces 313 / 83 / 37 cells with an
  out-of-sample net PF above 1 and 21 / 7 / 0 cells clearing the §3.4 gate —
  the same order of magnitude as the rule's own 77 and 6. Re-randomizing the 10
  cells that survive the out-of-sample and 2x-cost legs, 60 times each, gives
  uncorrected p-values of 0.0164-0.0492 and **0 of 10 survive the Bonferroni
  correction over the 17 556 tests the program ran**. Artifacts:
  `results/20261021_104104_null_survivor_scan/`,
  `results/20261021_073300_null_grid_scan/`.
- **The loss is a cost story, and the cost is a stop-width story.**
  `scripts/cost_drag_leg.py` decomposes 17 491 cells: pooled gross PF 0.8877
  against pooled net PF 0.5298, costs taking 26.6 % of the gross P&L. The
  cost of a trade as a share of its gross P&L is `2 * cost_per_side /
  risk_pct`; the median cell trades at a 0.912 % stop distance, which predicts
  26.3 % against a measured 26.4 %. Without any cost 2 387 cells would show a
  PF above 1; under the registered cost model only 77 do. Artifact:
  `results/20261021_102500_cost_drag_leg/`.
- **The rejection is not an artefact of the sample.** Dropping the 5/10/20/50
  largest market caps does not change the sign or the magnitude of the result
  (pooled net PF 0.5224 -> 0.5303), every market-cap rank bucket is below 1.0,
  and 31 of the 36 above-PF cells are fragile across time slices
  (`results/20261020_235449_robustness/`).
- **The selection procedure does not survive a walk-forward.**
  `scripts/survivor_selection_audit.py` re-runs the *selection* honestly: the
  full sample of every symbol is cut into 5 sequential folds, the best cell is
  chosen on the history and scored on the next, unseen, fold. Over **1060
  walk-forward steps and 95 786 out-of-fold trades the pooled out-of-fold net
  PF is 0.6409** (0.4521 under 2x costs); only 8.1 % of the out-of-fold
  windows land above PF 1, against the 1.2-3.3 % the grid's own null produces
  on the same folds. The selected cells do rank above that null (median
  percentile 0.78), so the selection is not noise - it simply never selects
  anything that is net-profitable out of fold. The 10-cell survivor family is
  also unstable: a leave-one-symbol-out re-selection keeps only 4-7 of the
  original cells and **none of the newcomers clears the cost-stress gate**.
  Artifact: `results/20261021_121629_survivor_selection_audit/`.
- **The program continues by policy.** PROMPT.md §2.1.4 is explicit: a failed
  symbol, a failed pair, or a failed batch never stops the program. The
  universe expands with the next lower market-cap names, each through the full
  66-pair grid, until expansion is impossible or the user cancels.

## What supersedes the 2026-10-19 conclusion

The 2026-10-19 note ("research concluded, no further experiments authorised")
came from the 5-symbol baseline study (BTC/ETH/SOL/BNB/XRP) and predates the
mandatory expansion rule of PROMPT.md §2.1. It is kept in
`results/FINAL_DECISION.md` as the historical record of that study. The
baseline conclusion itself has not changed: the strategy is rejected on
out-of-sample, net-of-costs evidence — with far more evidence than it had then.

## Rules that keep applying

- Never promote a cell on in-sample performance: a credible candidate needs net
  OOS PF > 1, net OOS Sharpe > 0, >= 30 OOS trades, and net PF > 1 under 2x
  costs in both the full sample and the OOS window.
- Never treat a negative batch as a program stop; expand instead.
- No live trading.

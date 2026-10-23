# Research Conclusion — EMA Hourly Continuation

## Program status (2026-10-21T19:35Z)

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
- **The selection is not an artefact of the selection granularity.**
  `scripts/selection_granularity_leg.py` repeats the walk-forward with one
  selection per *market-cap family* instead of one per symbol, and adds a
  random control: the same walk-forward with a random eligible cell picked
  at every step, 200 replicates. The per-symbol selection scores **0.6409**
  pooled out-of-fold net PF, the whole-family selection (all 266 symbols)
  **0.6649** (0.4818 under 2x costs) on 81 254 trades, and the random control
  a median **0.5601** (p05 0.5529, p95 0.5688). The selection sits at the
  100th percentile of that control, so it does rank better than a random
  pick, and the result survives the coarser selection - but it stays below 1
  out of fold at every granularity. Artifact:
  `results/20261021_193200_selection_granularity/`.
- **The one registered mutation that moves the cost drag moves the whole
  distribution, not the edge.** The PROMPT.md §5.2 ATR minimum-risk mutation
  is running as a full 17 556-cell child grid
  (`results/20261021_172619_grid`, parent `results/20261019_135940_grid`,
  recorded in `results/mutations.json`). On the 24 largest market caps that
  are complete so far it trades 57.5 % fewer trades and lifts the pooled net
  PF from 0.4561 to 0.7320, and the walk-forward moves from 0.5942 to 0.7239
  (2x costs 0.3875 -> 0.5370) - but the child's *own* null moves with it
  (null median PF 0.4139 -> 0.7067, the selected cells rank at the 0.5177
  percentile of it, binomial p 0.71), **0 cells clear the §3.4 gate**, and the
  cost share of the gross profit falls from 75.5 % to 31.3 %: the filter buys
  back cost drag by trading less and wider, it does not create an edge.
  Artifact: `results/20261021_194500_mutation_eval_partial/`.
- **The mutation's first gate-clearing cells are a selection result, not an
  edge.** The child grid produces cells that clear the §3.4 gate out of sample
  (the parent grid never does): on the 61 symbols that were complete,
  **20 of 4 026 child cells (0.50 %)** clear it, on 7 symbols (ENA 5, POL 5,
  APT 5, WLD 2, RENDER 1, AERO 1, PYTH 1), pooling to an out-of-sample net PF
  of **1.2606** over 1 633 out-of-sample trades. The family survives
  leave-one-symbol-out (the pooled out-of-sample PF stays between 1.2177 and
  1.2765 without any symbol), but only **3 of the 20** keep a net PF above 1
  in every out-of-sample sub-period that carries trades (POL/USDT P8_200,
  P21_200, P34_200), and the walk-forward selection on the child grid ranks
  at the **0.5249 percentile of the child's own null** (one-sided binomial p
  0.1068): the procedure cannot pick these cells out of the child grid. The
  open leg is the randomized null on the child grid. Artifact:
  `results/20261021_200500_mutation_survivor_check/`.
- **Both grids are the artifacts of the same engine.**
  `scripts/mutation_repro_check.py` re-runs sampled cells of both runs through
  the real backtest on the same fixtures: 12/12 child cells and 12/12 parent
  cells reproduce the stored blotter and summary **exactly** (max metric
  delta 0). The same leg shows what the mutation does to the *path*: the
  filter skips an entry, so the position state, the equity path and the size
  of every later trade change with it - the child drops 788 of the parent's
  entry bars per cell on average and enters at 21 bars the parent never
  took, so it is a different trading path, not a pruned copy of the parent's
  trades. Artifact: `results/20261021_193500_mutation_repro_check/`.
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

---

## Update 2026-10-23T12:28Z — batch 28 refresh pass (N = 275, unchanged)

The program is **still not concluded** and is in
`AWAITING_NEW_ELIGIBLE_CANDIDATES`. The refresh bound of
`mcap_snapshot_20261022_121558` (2026-10-23T12:15:58.876534Z) opened, and at
2026-10-23T12:28:28.949476Z exactly one 20-page CoinGecko ranking pass was run
(`universe/mcap_snapshot_20261023_122828.json`, 2 000 entries, 20/20 pages,
lowest covered rank 2 000 at $3 441 774, 0 history-probe failures). The new
snapshot is frozen for 24 h; the next eligible refresh is
**2026-10-24T12:28:28.949476Z**.

**No expansion was possible from this pass.** The expansion floor moved to
`BOSON/USDT` $3 558 643 (recomputed from the fresh ranking; it rose above the
batch-27 floor of `ALPINE/USDT` $3 614 141 because BOSON's market cap grew more
than ALPINE's between the two snapshots). The pass reached below that floor
($3 441 774 < $3 558 643), so the band was genuinely inspected — this is not an
incomplete scan. The 21 entries ranking below the floor are all ineligible:
18 have no tradable KuCoin spot USDT pair and 3 (4STOCK, MANYU, EVAA Protocol)
fail the 2-year hourly-history probe. `eligible_unseen_below_floor_count = 0`,
so `universe/last_scan.json` records `state = AWAITING_NEW_ELIGIBLE_CANDIDATES`
and `batch_selected = []`. The working universe stays at **N = 275**.

**Grid outcome, unchanged.** `results/20261019_135940_grid` remains the program
grid: 18 150/18 150 cells (275 symbols × 66 EMA pairs), 0 blocked,
`all_symbols_processed = true`, `next_cell = null`. Pooled mean net PF
**0.4987**; 37 cells net PF > 1; the 36-cell survivor set (BABYDOGE × 32,
JASMY P20_200 / P21_200, SUPER P8_200, MOODENG P8_200) is unchanged and every
one of them fails OOS + cost stress. **0 credible candidates.** No second writer
touched the grid and no child grid was promoted.

**What this means.** The registered EMA continuation rule still shows no edge
after 275 symbols, and the market-cap ranking now has no eligible name left in
its 2 000-entry coverage band. Both facts are consistent with the program's
existing conclusion: the strategy is rejected on out-of-sample, net-of-costs
evidence, and the multiple-testing tail matches the null. Per PROMPT.md §2.1.5,
an empty snapshot is a temporary waiting state, not a stop — the ranking must be
refreshed again at/after 2026-10-24T12:28:28.949476Z, and the program continues
until an explicit user cancellation. See `universe/mcap_expansion_log.md`
(Batch 28) for the full pass record.

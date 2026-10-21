# Final Decision — EMA Hourly Continuation

## Program status — 2026-10-21T14:25Z (supersedes the 2026-10-21T12:20Z decision)

Strategy: EMA hourly continuation (PROMPT.md). Universe: **266 symbols** ranked by
market cap descending, full EMA period grid (**66 pairs** from
`{8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}`), hourly KuCoin OHLCV, net of
costs (10 bps taker + 2 bps slippage per side).

**Decision: still no credible edge for the rule as it stands, and the strategy
is rejected on the evidence to date. The program keeps expanding the universe
until the expansion is impossible (PROMPT.md §2.1) — a negative result is never
a program stop.**

This status adds two things to the record: the **pre-registered ATR
minimum-risk mutation** (PROMPT.md §5.2, extension #2) was run over the
**whole grid** and compared with its parent, and the walk-forward selection
audit was repeated at **several selection granularities**.

| Gate | Baseline grid (parent) | ATR minimum-risk mutation (child) |
|---|---|---|
| Grid cells | 17 556 / 17 556 | 17 556 / 17 556 (own run dir, parent untouched) |
| Trades | 14 241 237 | 6 913 033 (48.5 % of the parent's sample) |
| Pooled net PF (full sample) | 0.5225 | **0.7347** |
| Pooled net PF (2x costs) | 0.3198 | 0.5561 |
| Pooled gross PF | 0.8872 | 0.9636 |
| Median cell cost share of the gross move | 26.6 % | **13.2 %** |
| Median cell stop distance (share of entry price) | 1.35 % | 2.08 % |
| **Pooled out-of-fold net PF (walk-forward, the yardstick)** | 0.6409 | **0.7390** (0.5731 under 2x costs) |
| Out-of-fold windows above PF 1 | 86 / 1060 (8.1 %) | 175 / 1060 (16.5 %) |
| Cells with out-of-sample net PF > 1 | 77 (0.44 %) | 608 (3.46 %) |
| Cells clearing the grid-wide OOS + 2x-cost gate | 10 | **106** |
| Verified credible candidates (the full §3.4 gate) | **0** | **10** |

Artifacts: pre-registration `results/20261021_130500_atr_min_risk_prereg/`,
child grid `results/20261021_125403_grid/`, child out-of-sample audit
`results/20261021_134900_child_oos_grid_scan/`, comparison
`results/20261021_135500_mutation_comparison/`.

### The ATR minimum-risk mutation (pre-registered, parent -> child -> delta)

The pre-registration was written **before** the child run started
(2026-10-21T12:50:00Z) and fixed the decision rule in advance: the child is
promoted only if its pooled out-of-fold net PF under the identical walk-forward
protocol is above 1.0, **and** still above 1.0 under 2x costs, **and** at least
one cell clears the out-of-sample + 2x-cost gate with at least 30 out-of-sample
trades.

**The rule is NOT satisfied: the child's pooled out-of-fold net PF is 0.7390
(0.5731 under 2x costs). The mutation is recorded as a rejected mutation as a
program-level rule.** The mechanism is the one the cost-drag leg predicted: the
filter skips trades whose stop is narrower than one ATR14, so the median stop
widens from 1.35 % to 2.08 % of the entry price, the median cell's cost share
of its gross move falls from 26.6 % to 13.2 %, and the pooled gross PF moves
from 0.8872 to 0.9636. The filter buys back the cost drag and changes the
gross result — but the procedure still loses money out of sample.

**What the child does change, and what it does not.** The child's cells clear
the grid-wide out-of-sample + 2x-cost gate 106 times against the parent's 10,
and 10 cells pass the full §3.4 credible-candidate gate against the parent's
0. That is *not* a promotion: 106 of 17 556 is 0.60 % of the grid, the
parent's own randomized-entry null puts the false-positive rate of the same
gate at 0.04-0.12 % of the grid, and the child's survivors have not been
through the selection-bias machinery (null scan, survivor selection audit,
leave-one-symbol-out, candidate check, sub-period stability) that the parent's
survivors had to pass. **The next leg has to run that machinery on the child
before the child's 10 cells can be called anything.** One early warning is
already visible: only 32 of the child's 108 gate-clearing cells keep a stressed
out-of-sample PF above 1 at all three window lengths (20 %, 35 %, 50 %),
against 0 of 6 for the parent — the child's survivors are less window-fragile,
but the majority of them still are.

### Is the walk-forward result a property of the selection granularity?

`scripts/selection_granularity.py`, artifact
`results/20261021_140500_selection_granularity/`: the walk-forward of leg 3 is
re-run with the selection unit changed — one selection per symbol (266
selections per step), one per market-cap bucket (5), or one for the whole
universe — and with 1, 3 or 10 cells selected per unit. The control (per
symbol, one cell) reproduces the recorded leg-3 yardstick exactly: pooled
out-of-fold net PF **0.6409** (0.4521 under 2x costs) over 95 786 out-of-fold
trades, 8.1 % of the windows above PF 1, median percentile 0.7768 against the
grid's own null, one-sided exact binomial p 1.9e-57.

| Selection unit | Parent, pooled out-of-fold net PF | Child, pooled out-of-fold net PF |
|---|---|---|
| per symbol (K = 1) | 0.6409 | 0.7390 |
| per market-cap bucket (K = 1) | 0.6609 | 0.8069 |
| global, one pair for the universe (K = 1) | 0.6649 | 0.8030 |
| global (K = 3) | 0.6613 | 0.8070 |

**No granularity clears PF 1 out of sample, in either arm.** A coarser
selection lifts the number by 0.02-0.07 and does not change the sign, so the
negative result of the finest selection is a property of the rule, not of the
selection granularity — the question the handoff asked has one answer for every
level of the ladder.

### Engine work that made the leg possible (no change to the baseline grid)

The pre-registered mutation was a ~44 h run on the research engine
(~10 min/symbol, 266 symbols x 66 pairs). It was finished in **55 minutes**
with a proved-equivalent twin of the engine:

- `backtest/backtest.py::backtest_symbol_fast` — the same state machine on
  numpy arrays (~0.05 s against ~4.7 s per cell), plus
  `signals.signals.generate_signals_vectorized` in the fast path.
- Equivalence is proved, not assumed: `tests/test_backtest_fast.py` (15 tests
  on synthetic frames and real fixtures, trade field by trade field and equity
  curve row by row curve row), `results/signal_equivalence_check.json` (268
  symbols, 1 360 cells, no mismatch), `results/20261021_130000_grid_repro_fast`
  (**200 of 200** sampled baseline cells re-run through the fast path reproduce
  their stored summaries exactly) and `results/20261021_141000_child_grid_repro`
  (**150 of 150** sampled child cells reproduce exactly).
- The research path is untouched: `engine='reference'` is still the default of
  `scripts/run_grid.py`, and the baseline grid artifacts were not modified.
- `scripts/run_grid.py` now writes `progress.json` after every symbol, so an
  interrupted run resumes from the cells that are already on disk.
- The legs that re-run the cells of a grid now read the config of *that* run
  (`scripts/run_grid.py::run_config`), so a mutated grid is audited under the
  mutation's config instead of the default one. Before this fix the child's
  cells were audited as if they were the parent's.

### Universe status (unchanged, 2026-10-21T11:41:20Z)

A fresh ranking snapshot (`universe/mcap_snapshot_20261021_114120.json`, 10/10
pages, 1 000 entries) was taken when the 24 h bound opened. The expansion floor
is now `AGLD/USDT` $16 279 472 and the coverage reaches $15 931 465, below it:
the band holds 10 names, all excluded (4 with less than two years of hourly
history, 6 with no tradable KuCoin spot USDT pair). **0 eligible unseen names
below the floor**, so no expansion is possible from this snapshot and the
program stays in `AWAITING_NEW_ELIGIBLE_CANDIDATES` until
**2026-10-22T11:41:20Z**.

### Recommendation

- No live trading, no promotion to production. The rule as registered still has
  no out-of-sample edge, at any selection granularity, with or without the
  ATR minimum-risk filter.
- **Next, before the refresh bound opens: run the selection-bias machinery on
  the child's 10 credible candidates** — a child-specific randomized-entry null
  (the ATR filter *plus* randomized entries), the survivor selection audit
  (family concentration, leave-one-symbol-out, walk-forward), the candidate
  check and the sub-period stability. The child is the only thing in the
  program that has produced a credible candidate, and it has not yet been
  through the machinery that killed the parent's 10.
- Keep expanding the universe in market-cap descending order (§2.1) and keep
  running the full 66-pair grid per symbol. The next expansion is blocked only
  by the 24 h market-cap refresh bound, which opens **2026-10-22T11:41:20Z**.

---

## Program status — 2026-10-21T12:20Z (supersedes the 2026-10-21T11:45Z decision)

Strategy: EMA hourly continuation (PROMPT.md). Universe: **266 symbols** ranked by
market cap descending, full EMA period grid (**66 pairs** from
`{8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}`), hourly KuCoin OHLCV, net of
costs (10 bps taker + 2 bps slippage per side).

**Decision: no credible edge. The strategy is rejected on the evidence to date,
and the program keeps expanding the universe until the expansion is impossible
(PROMPT.md §2.1) — a negative result is never a program stop.**

| Gate | Result |
|---|---|
| Grid cells evaluated | **17 556 / 17 556** (266 symbols x 66 pairs), 0 blocked |
| Labels | 17 530 rejected, 26 exploratory, **0 credible candidates** |
| Cells with full-sample net PF > 1 | **36 / 17 556 = 0.21 %** against a ~50 % no-edge null (excess -49.8 %) |
| Cells with out-of-sample net PF > 1 (all 17 556 cells evaluated out of sample) | **77 / 17 556 = 0.44 %** against the same null (excess -49.6 %) |
| Mean / median net PF (per cell) | 0.4993 / 0.5205 |
| Mean / median out-of-sample net PF (per cell) | 0.4320 / 0.4343 |
| Pooled net PF (trade-level) | **0.5224** over 14 240 827 trades |
| Pooled out-of-sample net PF (trade-level) | **0.5299**; 0.3267 under 2x costs |
| Best cell | BABYDOGE/USDT P50_55, net PF 2.2274 — rejected, 0 out-of-sample trades |

### Randomized-entry null (PROMPT.md §3.3, multiple testing)

`scripts/null_grid_scan.py` re-runs the untouched backtest engine on a
randomized version of the rule, keeping the market path, the EMA geometry, the
risk distances and the cost model, and destroying only the part under test
(timing, block-shuffled timing, or the sign of the trade). All 17 556 cells,
all three null modes. Artifact: `results/20261021_104104_null_survivor_scan/`
(the grid leg of the three modes is in `results/20261021_073300_null_grid_scan/`).

| Gate (out-of-sample leg) | Real rule | block null | timing null | sign null |
|---|---|---|---|---|
| Cells with out-of-sample net PF > 1 | 77 | 313 | 83 | 37 |
| Cells clearing the §3.4 out-of-sample gate | 6 | 21 | 7 | 0 |
| Pooled out-of-sample net PF | 0.4175 | 0.5114 | 0.4698 | 0.4469 |
| Best cell of the grid | 1.4697 | 2.2215 | 1.5873 | 1.6955 |

**The observed tail is no larger than the null's own tail.** The 6 cells that
clear the gate are matched by 21 block-null cells and 7 timing-null cells: the
gate's false-positive rate under no information is 0.04-0.12 % of the grid.

Per-cell re-randomization of the 10 cells that survive the out-of-sample and
2x-cost legs (60 replicates each, plus 12 control cells): the uncorrected
p-values are 0.0164-0.0492 and **0 of 10 keep their out-of-sample net PF at a
Bonferroni-corrected level over the 17 556 tests the program ran** (every
survivor's corrected p-value is 1.0000). The survivors are what 10 cells
selected out of 17 556 by chance look like.

### Survivor selection audit (does the selection survive a walk-forward?)

`scripts/survivor_selection_audit.py`, artifact
`results/20261021_121629_survivor_selection_audit/`: the 10 cells that clear
the out-of-sample gate are audited for concentration and for selection bias.

| Leg | Result |
|---|---|
| Family | 10 cells on 4 symbols (DEXE 6, GRT 2, BRETT 1, MERL 1); pooled OOS net PF 1.3353, 1.1183 under 2x costs |
| Exact re-run of the family | reproduces the audit numbers exactly (BRETT 1.3323/1.0489, DEXE P50_200 1.3819/1.1322, GRT P20_200 1.3413/1.0976, ...) |
| Leave-one-symbol-out | the family keeps a pooled net PF above 1 without any single symbol, but re-selection keeps only **4-7 of the original cells** and **0 newcomers clear the cost-stress gate**; without DEXE the re-selected family fails the pooled 2x-cost gate (0.9680) |
| Walk-forward re-selection | 1060 steps, 95 786 out-of-fold trades, pooled out-of-fold net PF **0.6409** (0.4521 under 2x costs); median in-fold PF of the selected cell 0.8272 -> median out-of-fold PF **0.6217** |
| Out-of-fold windows above PF 1 | 8.1 % of 1060, against 1.2-3.3 % of the grid's own null on the same folds |
| Selected cells vs the grid's own null | median percentile 0.7768, 198 of 1057 above the null p95 (one-sided exact binomial p 1.9e-57) |
| Sub-period stability of the 6 closest survivors | **0 of 6** keep a net PF above 1 in every out-of-sample sub-period that carries trades |

**The selection ranks the cells but never ranks one into a net-profitable
window.** The 10 survivors are the top of a procedure whose out-of-fold
result is a loss.

### Cost-drag decomposition (why the grid loses money)

`scripts/cost_drag_leg.py`, artifact
`results/20261021_102500_cost_drag_leg/`: 17 491 cells decomposed on the
out-of-sample window, pooled gross PF **0.8877** against pooled net PF
**0.5298**; costs of 17 840 159 against a gross P&L of -3 997 685, a cost share
of **26.6 %**. The mechanism is explicit — the cost of a trade as a share of
its gross P&L is `2 * cost_per_side / risk_pct`, and the median cell trades at
a 0.912 % stop distance, which predicts 26.3 % of the gross P&L in costs
against a measured 26.4 %. **The cost of the rule is a function of the width of
the stop, not of the number of trades.** Without any cost, 2 387 cells would
show a PF above 1; under the registered cost model only 77 do, and 3 735 cells
lose more than half of their gross P&L to fees and slippage.

### Robustness legs (PROMPT.md §3.3)

- **Out-of-sample + 2x cost stress** (`scripts/candidate_check.py`): all 36
  net-PF > 1 cells rejected; 0 credible candidates. Artifact:
  `results/20261021_033219_candidate_check/summary.md`.
- **Grid-wide out-of-sample audit** (`scripts/oos_grid_scan.py`): the OOS
  window is applied to **all 17 556 cells**, not only to the 36 whose
  in-sample net PF exceeded 1. Pooled out-of-sample net PF **0.5299** (0.3267
  under 2x costs); 77 cells (0.44 %) reach an out-of-sample net PF > 1, 75
  with >= 30 OOS trades, 10 still > 1 under 2x costs. The 180 screen
  survivors were re-verified through the real backtest: **0 credible
  candidates**, 76 exploratory, 104 rejected. Artifact:
  `results/20261021_033523_oos_grid_scan/summary.md`.
- **Out-of-sample window sensitivity** (same script): the 6 closest survivors
  were re-verified at 20 %, 35 % and 50 % windows. None keeps a stressed
  out-of-sample PF > 1 at all three lengths — the profitable window is an
  artifact of the window choice.
- **Drop the N largest market caps** (`scripts/robustness_pooled.py`): pooled net
  PF 0.5224 (all) -> 0.5248 (minus top 5) -> 0.5263 (top 10) -> 0.5280 (top 20)
  -> 0.5303 (top 50). The result does not depend on the largest names.
- **Rank buckets**: 1-10 0.4083, 11-50 0.5037, 51-100 0.5188, 101-200 0.5360,
  201+ 0.5302. Every bucket is below 1.0.
- **Subperiod stability** (4 equal-time slices per cell): of the 36 net-PF > 1
  cells, 31 are fragile across slices, 4 are too thin to judge, and 1
  (BABYDOGE/USDT P50_89) is stable but has 0 out-of-sample trades. Artifact:
  `results/20261020_235449_robustness/summary.md`.
- **Conservative same-bar exit** (stop first) is the registered baseline of every
  cell in the grid.

### Universe status (2026-10-21T11:41:20Z)

A fresh ranking snapshot (`universe/mcap_snapshot_20261021_114120.json`, 10/10
pages, 1 000 entries) was taken when the 24 h bound opened. The expansion floor
is now `AGLD/USDT` $16 279 472 and the coverage reaches $15 931 465, below it:
the band holds 10 names, all excluded (4 with less than two years of hourly
history, 6 with no tradable KuCoin spot USDT pair). **0 eligible unseen names
below the floor**, so no expansion is possible from this snapshot and the
program stays in `AWAITING_NEW_ELIGIBLE_CANDIDATES` until
**2026-10-22T11:41:20Z**.

### Recommendation

- No live trading, no promotion to production: nothing in 17 556 grid cells
  survives the out-of-sample and cost-stress gates, the selection bias of the
  original gate has been removed, the surviving cells are indistinguishable
  from their own randomizations, and the selection procedure itself does not
  survive a walk-forward (pooled out-of-fold net PF 0.6409 over 95 786
  out-of-fold trades).
- Keep expanding the universe in market-cap descending order (§2.1) and keep
  running the full 66-pair grid per symbol. The next expansion is blocked only
  by the 24 h market-cap refresh bound, which opens **2026-10-22T11:41:20Z**.

---

## Program status — 2026-10-21T11:45Z (supersedes the 2026-10-21T01:05Z decision)

Strategy: EMA hourly continuation (PROMPT.md). Universe: **266 symbols** ranked by
market cap descending, full EMA period grid (**66 pairs** from
`{8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}`), hourly KuCoin OHLCV, net of
costs (10 bps taker + 2 bps slippage per side).

**Decision: no credible edge. The strategy is rejected on the evidence to date,
and the program keeps expanding the universe until the expansion is impossible
(PROMPT.md §2.1) — a negative result is never a program stop.**

| Gate | Result |
|---|---|
| Grid cells evaluated | **17 556 / 17 556** (266 symbols x 66 pairs), 0 blocked |
| Labels | 17 530 rejected, 26 exploratory, **0 credible candidates** |
| Cells with full-sample net PF > 1 | **36 / 17 556 = 0.21 %** against a ~50 % no-edge null (excess -49.8 %) |
| Cells with out-of-sample net PF > 1 (all 17 556 cells evaluated out of sample) | **77 / 17 556 = 0.44 %** against the same null (excess -49.6 %) |
| Mean / median net PF (per cell) | 0.4993 / 0.5205 |
| Mean / median out-of-sample net PF (per cell) | 0.4320 / 0.4343 |
| Pooled net PF (trade-level) | **0.5224** over 14 240 827 trades |
| Pooled out-of-sample net PF (trade-level) | **0.5299**; 0.3267 under 2x costs |
| Best cell | BABYDOGE/USDT P50_55, net PF 2.2274 — rejected, 0 out-of-sample trades |

### Randomized-entry null (PROMPT.md §3.3, multiple testing)

`scripts/null_grid_scan.py` re-runs the untouched backtest engine on a
randomized version of the rule, keeping the market path, the EMA geometry, the
risk distances and the cost model, and destroying only the part under test
(timing, block-shuffled timing, or the sign of the trade). All 17 556 cells,
all three null modes. Artifact: `results/20261021_104104_null_survivor_scan/`
(the grid leg of the three modes is in `results/20261021_073300_null_grid_scan/`).

| Gate (out-of-sample leg) | Real rule | block null | timing null | sign null |
|---|---|---|---|---|
| Cells with out-of-sample net PF > 1 | 77 | 313 | 83 | 37 |
| Cells clearing the §3.4 out-of-sample gate | 6 | 21 | 7 | 0 |
| Pooled out-of-sample net PF | 0.4175 | 0.5114 | 0.4698 | 0.4469 |
| Best cell of the grid | 1.4697 | 2.2215 | 1.5873 | 1.6955 |

**The observed tail is no larger than the null's own tail.** The 6 cells that
clear the gate are matched by 21 block-null cells and 7 timing-null cells: the
gate's false-positive rate under no information is 0.04-0.12 % of the grid.

Per-cell re-randomization of the 10 cells that survive the out-of-sample and
2x-cost legs (60 replicates each, plus 12 control cells): the uncorrected
p-values are 0.0164-0.0492 and **0 of 10 keep their out-of-sample net PF at a
Bonferroni-corrected level over the 17 556 tests the program ran** (every
survivor's corrected p-value is 1.0000). The survivors are what 10 cells
selected out of 17 556 by chance look like.

### Cost-drag decomposition (why the grid loses money)

`scripts/cost_drag_leg.py`, artifact
`results/20261021_102500_cost_drag_leg/`: 17 491 cells decomposed on the
out-of-sample window, pooled gross PF **0.8877** against pooled net PF
**0.5298**; costs of 17 840 159 against a gross P&L of -3 997 685, a cost share
of **26.6 %**. The mechanism is explicit — the cost of a trade as a share of
its gross P&L is `2 * cost_per_side / risk_pct`, and the median cell trades at
a 0.912 % stop distance, which predicts 26.3 % of the gross P&L in costs
against a measured 26.4 %. **The cost of the rule is a function of the width of
the stop, not of the number of trades.** Without any cost, 2 387 cells would
show a PF above 1; under the registered cost model only 77 do, and 3 735 cells
lose more than half of their gross P&L to fees and slippage.

### Robustness legs (PROMPT.md §3.3)

- **Out-of-sample + 2x cost stress** (`scripts/candidate_check.py`): all 36
  net-PF > 1 cells rejected; 0 credible candidates. Artifact:
  `results/20261021_033219_candidate_check/summary.md`.
- **Grid-wide out-of-sample audit** (`scripts/oos_grid_scan.py`): the OOS
  window is applied to **all 17 556 cells**, not only to the 36 whose
  in-sample net PF exceeded 1. Pooled out-of-sample net PF **0.5299** (0.3267
  under 2x costs); 77 cells (0.44 %) reach an out-of-sample net PF > 1, 75
  with >= 30 OOS trades, 10 still > 1 under 2x costs. The 180 screen
  survivors were re-verified through the real backtest: **0 credible
  candidates**, 76 exploratory, 104 rejected. Artifact:
  `results/20261021_033523_oos_grid_scan/summary.md`.
- **Out-of-sample window sensitivity** (same script): the 6 closest survivors
  were re-verified at 20 %, 35 % and 50 % windows. None keeps a stressed
  out-of-sample PF > 1 at all three lengths — the profitable window is an
  artifact of the window choice.
- **Drop the N largest market caps** (`scripts/robustness_pooled.py`): pooled net
  PF 0.5224 (all) -> 0.5248 (minus top 5) -> 0.5263 (top 10) -> 0.5280 (top 20)
  -> 0.5303 (top 50). The result does not depend on the largest names.
- **Rank buckets**: 1-10 0.4083, 11-50 0.5037, 51-100 0.5188, 101-200 0.5360,
  201+ 0.5302. Every bucket is below 1.0.
- **Subperiod stability** (4 equal-time slices per cell): of the 36 net-PF > 1
  cells, 31 are fragile across slices, 4 are too thin to judge, and 1
  (BABYDOGE/USDT P50_89) is stable but has 0 out-of-sample trades. Artifact:
  `results/20261020_235449_robustness/summary.md`.
- **Conservative same-bar exit** (stop first) is the registered baseline of every
  cell in the grid.

### Universe status (2026-10-21T11:41:20Z)

A fresh ranking snapshot (`universe/mcap_snapshot_20261021_114120.json`, 10/10
pages, 1 000 entries) was taken when the 24 h bound opened. The expansion floor
is now `AGLD/USDT` $16 279 472 and the coverage reaches $15 931 465, below it:
the band holds 10 names, all excluded (4 with less than two years of hourly
history, 6 with no tradable KuCoin spot USDT pair). **0 eligible unseen names
below the floor**, so no expansion is possible from this snapshot and the
program stays in `AWAITING_NEW_ELIGIBLE_CANDIDATES` until
**2026-10-22T11:41:20Z**.

### Recommendation

- No live trading, no promotion to production: nothing in 17 556 grid cells
  survives the out-of-sample and cost-stress gates, the selection bias of the
  original gate has been removed, and the surviving cells are indistinguishable
  from their own randomizations.
- Keep expanding the universe in market-cap descending order (§2.1) and keep
  running the full 66-pair grid per symbol. The next expansion is blocked only
  by the 24 h market-cap refresh bound, which opens **2026-10-22T11:41:20Z**.

---

## Program status — 2026-10-21T01:05Z (supersedes the 2026-10-20T23:47Z decision)

Strategy: EMA hourly continuation (PROMPT.md). Universe: **266 symbols** ranked by
market cap descending, full EMA period grid (**66 pairs** from
`{8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}`), hourly KuCoin OHLCV, net of
costs (10 bps taker + 2 bps slippage per side).

**Decision: no credible edge. The strategy is rejected on the evidence to date,
and the program keeps expanding the universe until the expansion is impossible
(PROMPT.md §2.1) — a negative result is never a program stop.**

| Gate | Result |
|---|---|
| Grid cells evaluated | **17 556 / 17 556** (266 symbols x 66 pairs), 0 blocked |
| Labels | 17 530 rejected, 26 exploratory, **0 credible candidates** |
| Cells with full-sample net PF > 1 | **36 / 17 556 = 0.21 %** against a ~50 % no-edge null (excess -49.8 %) |
| Cells with out-of-sample net PF > 1 (all 17 556 cells evaluated out of sample) | **77 / 17 556 = 0.44 %** against the same null (excess -49.6 %) |
| Mean / median net PF (per cell) | 0.4993 / 0.5205 |
| Mean / median out-of-sample net PF (per cell) | 0.4320 / 0.4343 |
| Pooled net PF (trade-level) | **0.5224** over 14 240 827 trades |
| Pooled out-of-sample net PF (trade-level) | **0.5299**; 0.3267 under 2x costs |
| Best cell | BABYDOGE/USDT P50_55, net PF 2.2274 — rejected, 0 out-of-sample trades |

### Robustness legs (PROMPT.md §3.3)

- **Out-of-sample + 2x cost stress** (`scripts/candidate_check.py`): all 36
  net-PF > 1 cells rejected; 0 credible candidates. Artifact:
  `results/20261020_233737_candidate_check/summary.md`.
- **Grid-wide out-of-sample audit** (`scripts/oos_grid_scan.py`, new): the OOS
  window is applied to **all 17 556 cells**, not only to the 36 whose
  in-sample net PF exceeded 1. Pooled out-of-sample net PF **0.5299** (0.3267
  under 2x costs); 77 cells (0.44 %) reach an out-of-sample net PF > 1, 75
  with >= 30 OOS trades, 10 still > 1 under 2x costs. The 180 screen
  survivors were re-verified through the real backtest: **0 credible
  candidates**, 76 exploratory, 104 rejected. Artifact:
  `results/20261021_005234_oos_grid_scan/summary.md`.
- **Out-of-sample window sensitivity** (same script): the 6 closest survivors
  were re-verified at 20 %, 35 % and 50 % windows. None keeps a stressed
  out-of-sample PF > 1 at all three lengths — the profitable window is an
  artifact of the window choice.
- **Drop the N largest market caps** (`scripts/robustness_pooled.py`): pooled net
  PF 0.5224 (all) -> 0.5248 (minus top 5) -> 0.5263 (top 10) -> 0.5280 (top 20)
  -> 0.5303 (top 50). The result does not depend on the largest names.
- **Rank buckets**: 1-10 0.4083, 11-50 0.5037, 51-100 0.5188, 101-200 0.5360,
  201+ 0.5302. Every bucket is below 1.0.
- **Subperiod stability** (4 equal-time slices per cell): of the 36 net-PF > 1
  cells, 31 are fragile across slices, 4 are too thin to judge, and 1
  (BABYDOGE/USDT P50_89) is stable but has 0 out-of-sample trades. Artifact:
  `results/20261020_235449_robustness/summary.md`.
- **Conservative same-bar exit** (stop first) is the registered baseline of every
  cell in the grid.

### Recommendation

- No live trading, no promotion to production: nothing in 17 556 grid cells
  survives the out-of-sample and cost-stress gates, and the selection bias of
  the original gate has now been removed — the out-of-sample window was
  applied to every cell, not only to the in-sample winners.
- Keep expanding the universe in market-cap descending order (§2.1) and keep
  running the full 66-pair grid per symbol. The next expansion is blocked only
  by the 24 h market-cap refresh bound, which opens **2026-10-21T11:30:04Z**.

---

## Baseline study (2026-10-19, 5 symbols) — historical record

Date: 2026-10-19
Strategy: EMA hourly continuation (PROMPT.md)
Sample: Real hourly OHLCV only (BTC/USDT 25k, ETH/SOL/BNB/XRP 22k; UTC). Data in `data/fixtures/`, `fetch_manifest.json`.

## Acceptance OOS (reproduced)
- Command: `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5`
- Results: `results/20261019_064215_oos_pooled/`
- Pooled: 666 trades, net PF=0.6890, net Sharpe=-1.9443, max DD=0.6663
- Per-symbol: BTC 124 (PF 0.6860, Sharpe -0.9004); ETH 119 (PF 0.7861, Sharpe -1.8710); SOL 132 (PF 0.8792, Sharpe -1.1395); BNB 150 (PF 0.6955, Sharpe -2.8661); XRP 141 (PF 0.8006, Sharpe -1.8986)

## Robustness
- Cost stress (2x, full sample): base 0.6906 → stress 0.4691; Sharpe 0.8550 → -0.7038; max DD 1.89 → 4.09
- ATR grid (OOS): atr 0.5 (826 tr, PF 0.6354, Sharpe -2.1419), atr 1.0 (517 tr, PF 0.6501, Sharpe -2.0586), atr 1.5 (302 tr, PF 0.7922, Sharpe -1.2193)
- Same-bar exit: conservative vs aggressive TP-first — negligible delta (PF 0.6890→0.6952, Sharpe -1.9443→-1.9169)
- Stricter trend: no-op; same metrics

## Decision
**REJECTED**. Strategy fails on OOS net-of-costs (negative Sharpe, PF<1, substantial max drawdown). Larger real sample did not improve profitability; cost stress materially worsens results; no tested robustness variant reaches profitability. Adequate sample size (666 pooled trades, 22k–25k bars/symbol).

## Recommendation
- No live trading. Do not promote to production.
- Do not continue parameter tuning of this baseline. Only pursue if a new, pre-specified hypothesis is formulated (with clear theoretical rationale and falsifiable acceptance criteria) before testing.

> This 5-symbol section is the historical record of the first study. It did not
> account for the mandatory expanding-universe rule of PROMPT.md §2.1, so the
> program continued to larger, lower-market-cap names; the decision above is
> unchanged in substance and is now supported by 17 556 grid cells instead of
> 666 pooled trades.

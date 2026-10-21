# Robustness Summary — EMA Hourly Continuation

## Program-level robustness (2026-10-21T01:05Z, universe N = 266)

Grid run: `results/20261019_135940_grid` — 17 556 cells (266 symbols x 66 EMA
pairs), net of costs (10 bps taker + 2 bps slippage per side).

| Leg | Script | Result |
|---|---|---|
| Out-of-sample (trailing 35 %) + 2x cost stress | `scripts/candidate_check.py` | 36 cells with full-sample net PF > 1, **36 rejected, 0 credible candidates** (`results/20261020_233737_candidate_check/`) |
| **Grid-wide out-of-sample audit (all 17 556 cells)** | `scripts/oos_grid_scan.py` | 77 cells (0.44 %) reach an out-of-sample net PF > 1, 75 with >= 30 OOS trades, 10 still > 1 under 2x costs; 180 screen survivors re-verified with a real backtest -> **0 credible candidates, 76 exploratory** (`results/20261021_005234_oos_grid_scan/`) |
| Drop the N largest market caps | `scripts/robustness_pooled.py` | pooled net PF 0.5224 (all) -> 0.5248 (top 5) -> 0.5263 (top 10) -> 0.5280 (top 20) -> 0.5303 (top 50) |
| Market-cap rank buckets | `scripts/robustness_pooled.py` | 1-10 0.4083, 11-50 0.5037, 51-100 0.5188, 101-200 0.5360, 201+ 0.5302 |
| Subperiod stability (4 time slices per cell) | `scripts/robustness_pooled.py` | of the 36 above-PF cells: 31 fragile, 4 insufficient, 1 stable-but-no-OOS-trades |
| Out-of-sample window sensitivity (20 % / 35 % / 50 %) | `scripts/oos_grid_scan.py` | none of the 6 closest survivors keeps a stressed out-of-sample PF > 1 at all three window lengths |
| Conservative same-bar exit (stop first) | registered baseline of every grid cell | applied to all 17 556 cells |

Artifacts: `results/20261021_005234_oos_grid_scan/summary.md` (+ `summary.json`,
`cells.jsonl`), `results/20261020_235449_robustness/summary.md` (+ `summary.json`),
`results/20261020_233737_candidate_check/summary.md`,
`results/20261019_135940_grid/pooled.md`.

### Why the grid-wide out-of-sample leg matters

`scripts/candidate_check.py` only ever applies the out-of-sample and 2x-cost
gates to the cells whose **in-sample** net PF exceeded 1 — 36 of 17 556. The
other 17 520 cells were never looked at out of sample, so the decision rested
on a selected subset. `scripts/oos_grid_scan.py` removes that selection: the
out-of-sample window is applied to every cell, and the survivors are then
re-verified through the real backtest.

- Pooled out-of-sample net PF over the whole grid: **0.5299** (0.3267 under 2x
  costs) — the grid is no better out of sample than in sample.
- Out-of-sample net PF per cell: mean 0.4320, median 0.4343, max 1.9955.
- 77 cells (0.44 %) reach an out-of-sample net PF > 1; **0** survive the
  §3.4 gate, in the in-sample winners and in the rest of the grid alike.
- The 6 closest survivors (BRETT P8_200, DEXE P50_200, DEXE P55_200,
  GRT P20_200, MERL P8_200, ZEN P12_200) all have a **full-sample** net PF
  below 1 (0.75-0.91): the profitable out-of-sample window is a lucky slice
  of a strategy that loses money over the whole sample.
- The screen is validated against the authoritative candidate-check numbers:
  mean absolute net PF difference 0.0603 on the 4 comparable cells, and
  0 disagreements on the 32 cells with no out-of-sample trade in either run.

**Read-out:** the strategy fails on net-of-costs evidence at every robustness
level. The failure is stable across market-cap sizes, rank buckets, time
slices, out-of-sample windows and cost assumptions, and it is not produced by
a handful of large-cap names.


## Baseline study (2026-10-19, 5 symbols) — historical record

Config: rr=1.5, min_risk_atr=True, atr_threshold=0.75, stricter_trend=False.

## Threshold sweep (n=5, pooled)
| atr_threshold | trades | net PF | net WR | Sharpe |
|---|---|---|---|---|
| 0.70 | 39 | 0.3680 | 0.3846 | -9.3864 |
| 0.75 | 36 | 0.4257 | 0.3889 | -7.9898 |
| 0.80 | 34 | 0.4171 | 0.3824 | -8.0183 |

0.75 remains best among tested.

## Walk-forward (BTC/USDT, expanding windows)
All 4 test windows produced 0 trades (windows too short / no qualifying signals). No OOS trades to evaluate; indicates need larger OOS windows or pooled cross-symbol OOS.

## OOS split (pooled, last 20%)
0 trades. Same limitation.

## stricter_trend variation
No change in metrics vs base Child C (36 trades, net PF 0.4257).

## Conclusion
Tuned config improves vs unfiltered but remains negative Sharpe; OOS validation inconclusive due to sparse signals. Next: pooled OOS with larger test windows and per-symbol OOS aggregation.

> The pooled out-of-sample leg that this baseline study could not run was
> completed later on the full universe: 36 above-PF cells, 0 credible
> candidates.

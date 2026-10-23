# Randomized-Entry Null — EMA Hourly Continuation Grid

**Source run:** `results/20261022_134500_grid`
**Generated:** 2026-10-23T09:29:22.772607+00:00
**Universe:** 275 symbols, 18150 grid cells
**Out-of-sample window:** trailing 35% of each symbol's bars, entries restricted to the window
**Cost stress:** 2x fees and slippage

## What the leg asks

How many of the 17 556 cells would clear the out-of-sample gates if the entry rule carried no information? The null keeps the market path, the EMA geometry, the risk distances and the cost model, and destroys only the part of the rule under test:

- **block** - the same number of entries, with the same direction mix, moved to random bars inside their own 240-bar block. The entry stops being a cross but stays in the same stretch of the market, so the risk distance and the cost drag stay comparable.
- **timing** - the same number of entries, at uniformly random bars over the out-of-sample window, with the same multiset of directions.
- **sign** - the same entry bars, with every direction redrawn from a fair coin.

Both are run through the untouched backtest engine, so the null is produced by the same code that produced the real numbers. The null is matched to the rule inside the window: the entries the rule fires on inside the window are the entries the null randomizes, so both sides are scored on the same sample.

## Leg 0 — The harness reproduces the grid run

| Check | Result |
|---|---|
| Cells re-run on the full history | 200 |
| Recomputed full-sample net PF equals the stored grid summary | 200 of 200 |
| Windowed run equals the full-history in-window trades | 200 of 200 |
| Vectorized signal generator equals the reference generator | 200 of 200 |

## Leg 1 — The null grid

| Statistic | Real rule | block null | timing null | sign null |
|---|---|---|---|---|
| mean out-of-sample net PF | 0.4304 | 0.5442 | 0.4957 | 0.4617 |
| median out-of-sample net PF | 0.4323 | 0.5285 | 0.4852 | 0.4652 |
| p95 out-of-sample net PF | 0.7177 | 0.8572 | 0.7525 | 0.7420 |
| max out-of-sample net PF | 1.4697 | 2.2215 | 1.5873 | 1.6955 |

| Gate (out-of-sample leg) | Real rule | block null | timing null | sign null |
|---|---|---|---|---|
| Cells with out-of-sample net PF > 1 | 77 | 320 | 86 | 44 |
| Cells clearing the §3.4 out-of-sample gate | 6 | 24 | 7 | 1 |
| Pooled out-of-sample net PF | 0.4163 | 0.5114 | 0.4704 | 0.4480 |
| Cells with gross out-of-sample PF > 1 | 2393 | 9450 | 4967 | 4284 |
| Median gross out-of-sample net PF | 0.8289 | 1.0095 | 0.9086 | 0.8959 |
| Median out-of-sample trades per cell | 261.0000 | 204.0000 | 202.0000 | 261.0000 |
| Median risk distance (share of entry price) | 1.1258% | 1.7234% | 1.7894% | 1.1258% |

Gate: out-of-sample net PF > 1, out-of-sample Sharpe > 0, at least min_trades out-of-sample trades, and out-of-sample net PF still > 1 under the cost stress.

## Leg 2 — The observed tail against the null tail

| Statistic | Real rule | block null | timing null | sign null |
|---|------|---|---|
| Best cell of the grid | 1.4697 | 2.2215 | 1.5873 | 1.6955 |
| Null cells at or above the real best | - | 14 | 4 | 2 |
| Family-wise probability of a null cell reaching the real best | - | 1 - 8.27e-07 | 0.9817 | 0.8647 |
| Cells where the real rule beats its own null | - | 3023 | 5488 | 6223 |
| Cells where the null beats the real rule | - | 15127 | 12662 | 11927 |
| Two-sided sign test on that comparison | - | 0.00e+00 | 0.00e+00 | 0.00e+00 |
| Same comparison on the gross profit factor (no cost drag) | - | 2638 | 5600 | 6035 |
| Two-sided sign test on the gross comparison | - | 0.00e+00 | 0.00e+00 | 0.00e+00 |

A sign test p-value this small means the two sides of the comparison are not exchangeable. The direction is the point: the counts above say which side of the comparison the rule is on.

## Verdict

- 77 of 18150 cells show an out-of-sample net PF above 1; the block null produces 320. The observed tail is no larger than what the block null delivers.
- 6 real cells clear the §3.4 out-of-sample gate against 24 block-null cells: the gate's false-positive rate under no information is 0.13% of the grid.
- The best real cell (net PF 1.4697) sits against a best block cell of 2.2215; the family-wise probability that a null cell reaches the real best is 1 - 8.27e-07.
- The real rule beats its own block null in 3023 of 18150 cells and loses to it in 15127 (sign test p = 0.00e+00).
- Grid-wide null counts (cells with an out-of-sample net PF above 1 / cells clearing the gate): real 77/6; block 320/24; timing 86/7; sign 44/1.

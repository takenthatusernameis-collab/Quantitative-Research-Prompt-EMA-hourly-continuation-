# Randomized-Entry Null — EMA Hourly Continuation Grid

**Source run:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T10:10:28.251214+00:00
**Universe:** 266 symbols, 17556 grid cells
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
| Cells re-run on the full history | 12 |
| Recomputed full-sample net PF equals the stored grid summary | 12 of 12 |
| Windowed run equals the full-history in-window trades | 12 of 12 |
| Vectorized signal generator equals the reference generator | 12 of 12 |

## Leg 1 — The null grid

| Statistic | Real rule | timing null | block null | sign null |
|---|---|---|---|---|
| mean out-of-sample net PF | 0.4321 | 0.4952 | 0.5444 | 0.4605 |
| median out-of-sample net PF | 0.4342 | 0.4849 | 0.5285 | 0.4644 |
| p95 out-of-sample net PF | 0.7200 | 0.7505 | 0.8581 | 0.7383 |
| max out-of-sample net PF | 1.4697 | 1.5873 | 2.2215 | 1.6955 |

| Gate (out-of-sample leg) | Real rule | timing null | block null | sign null |
|---|---|---|---|---|
| Cells with out-of-sample net PF > 1 | 77 | 83 | 313 | 37 |
| Cells clearing the §3.4 out-of-sample gate | 6 | 7 | 21 | 0 |
| Pooled out-of-sample net PF | 0.4175 | 0.4698 | 0.5114 | 0.4469 |
| Cells with gross out-of-sample PF > 1 | 2384 | 4806 | 9188 | 4176 |
| Median gross out-of-sample net PF | 0.8326 | 0.9086 | 1.0109 | 0.8964 |
| Median out-of-sample trades per cell | 262.0000 | 202.0000 | 205.0000 | 262.0000 |
| Median risk distance (share of entry price) | 1.1191% | 1.7847% | 1.7215% | 1.1191% |

Gate: out-of-sample net PF > 1, out-of-sample Sharpe > 0, at least min_trades out-of-sample trades, and out-of-sample net PF still > 1 under the cost stress.

## Leg 2 — The observed tail against the null tail

| Statistic | Real rule | timing null | block null | sign null |
|---|------|---|---|
| Best cell of the grid | 1.4697 | 1.5873 | 2.2215 | 1.6955 |
| Null cells at or above the real best | - | 4 | 14 | 2 |
| Family-wise probability of a null cell reaching the real best | - | 0.9817 | 1 - 8.27e-07 | 0.8647 |
| Cells where the real rule beats its own null | - | 5382 | 2964 | 6131 |
| Cells where the null beats the real rule | - | 12174 | 14592 | 11425 |
| Two-sided sign test on that comparison | - | 0.00e+00 | 0.00e+00 | 0.00e+00 |
| Same comparison on the gross profit factor (no cost drag) | - | 5534 | 2606 | 5947 |
| Two-sided sign test on the gross comparison | - | 0.00e+00 | 0.00e+00 | 0.00e+00 |

A sign test p-value this small means the two sides of the comparison are not exchangeable. The direction is the point: the counts above say which side of the comparison the rule is on.

## Verdict

- 77 of 17556 cells show an out-of-sample net PF above 1; the timing null produces 83. The observed tail is no larger than what the timing null delivers.
- 6 real cells clear the §3.4 out-of-sample gate against 7 timing-null cells: the gate's false-positive rate under no information is 0.04% of the grid.
- The best real cell (net PF 1.4697) sits against a best timing cell of 1.5873; the family-wise probability that a null cell reaches the real best is 0.9817.
- The real rule beats its own timing null in 5382 of 17556 cells and loses to it in 12174 (sign test p = 0.00e+00).
- Grid-wide null counts (cells with an out-of-sample net PF above 1 / cells clearing the gate): real 77/6; timing 83/7; block 313/21; sign 37/0.

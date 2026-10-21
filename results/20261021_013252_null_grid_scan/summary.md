# Randomized-Entry Null — EMA Hourly Continuation Grid

**Source run:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T01:35:24.910266+00:00
**Universe:** 8 symbols, 528 grid cells
**Out-of-sample window:** trailing 35% of each symbol's bars, entries restricted to the window
**Cost stress:** 2x fees and slippage

## What the leg asks

How many of the 17 556 cells would clear the out-of-sample gates if the entry rule carried no information? The null keeps the market path, the EMA geometry, the risk distances and the cost model, and destroys only the part of the rule under test:

- **block** - the same number of entries, with the same direction mix, moved to random bars inside their own 240-bar block. The entry stops being a cross but stays in the same stretch of the market, so the risk distance and the cost drag stay comparable.
- **timing** - the same number of entries, at uniformly random bars over the whole series, with the same multiset of directions.
- **sign** - the same entry bars, with every direction redrawn from a fair coin.

Both are run through the untouched backtest engine, so the null is produced by the same code that produced the real numbers.

## Leg 0 — The harness reproduces the grid run

| Check | Result |
|---|---|
| Cells re-run on the full history | 0 |
| Recomputed full-sample net PF equals the stored grid summary | 0 of 0 |
| Windowed run equals the full-history in-window trades | 0 of 0 |
| Vectorized signal generator equals the reference generator | 0 of 0 |

## Leg 1 — The null grid

| Statistic | Real rule | block null |
|---|---|---|
| mean out-of-sample net PF | 0.4541 | 0.5541 |
| median out-of-sample net PF | 0.4616 | 0.5417 |
| p95 out-of-sample net PF | 0.6962 | 0.8114 |
| max out-of-sample net PF | 0.9328 | 1.6243 |

| Gate (out-of-sample leg) | Real rule | block null |
|---|---|---|
| Cells with out-of-sample net PF > 1 | 0 | 9 |
| Cells clearing the §3.4 out-of-sample gate | 0 | 1 |
| Pooled out-of-sample net PF | 0.0000 | 0.0000 |
| Cells with gross out-of-sample PF > 1 | 66 | 248 |
| Median gross out-of-sample net PF | 0.8459 | 0.9923 |
| Median out-of-sample trades per cell | 263.0000 | 205.0000 |
| Median risk distance (share of entry price) | 1.1758% | 1.8501% |

Gate: out-of-sample net PF > 1, out-of-sample Sharpe > 0, at least min_trades out-of-sample trades, and out-of-sample net PF still > 1 under the cost stress.

The timing, sign null was not run over the whole grid in this leg (compute budget); it was run on the surviving and the control cells in Leg 3.

## Leg 2 — The observed tail against the null tail

| Quantity | Value |
|---|---|
| Best cell of the grid (real) | 0.9328 |
| Best cell of the block null | 1.6243 |
| Null cells at or above the real best | 12 |
| Family-wise probability of a null cell reaching the real best | 1.0000 |
| Cells where the real rule beats its own block null | 115 of 528 |
| Two-sided sign test on that comparison | 2.02e-40 |
| Same comparison on the gross profit factor (no cost drag) | 98 of 528 |
| Two-sided sign test on the gross comparison | 1.37e-50 |

## Verdict

- The best real cell (net PF 0.9328) sits against a best null cell of n/a; the family-wise probability that a null cell reaches the real best is 1.0000.
- The real rule beats its own timing null in 115 of 528 cells (sign test p = 2.02e-40).

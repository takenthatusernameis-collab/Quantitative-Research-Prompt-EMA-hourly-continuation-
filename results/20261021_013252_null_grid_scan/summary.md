# Randomized-Entry Null — EMA Hourly Continuation Grid

**Source run:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T02:52:25.167585+00:00
**Universe:** 266 symbols, 17556 grid cells
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
| Cells re-run on the full history | 200 |
| Recomputed full-sample net PF equals the stored grid summary | 192 of 200 |
| Windowed run equals the full-history in-window trades | 200 of 200 |
| Vectorized signal generator equals the reference generator | 200 of 200 |

## Leg 1 — The null grid

| Statistic | Real rule | block null |
|---|---|---|
| mean out-of-sample net PF | 0.4321 | 0.5443 |
| median out-of-sample net PF | 0.4342 | 0.5308 |
| p95 out-of-sample net PF | 0.7200 | 0.8548 |
| max out-of-sample net PF | 1.4697 | 9.6992 |

| Gate (out-of-sample leg) | Real rule | block null |
|---|---|---|
| Cells with out-of-sample net PF > 1 | 77 | 276 |
| Cells clearing the §3.4 out-of-sample gate | 6 | 35 |
| Pooled out-of-sample net PF | 0.0000 | 0.0000 |
| Cells with gross out-of-sample PF > 1 | 2384 | 9259 |
| Median gross out-of-sample net PF | 0.8326 | 1.0122 |
| Median out-of-sample trades per cell | 262.0000 | 205.0000 |
| Median risk distance (share of entry price) | 1.1191% | 1.7194% |

Gate: out-of-sample net PF > 1, out-of-sample Sharpe > 0, at least min_trades out-of-sample trades, and out-of-sample net PF still > 1 under the cost stress.

The timing, sign null was not run over the whole grid in this leg (compute budget); it was run on the surviving and the control cells in Leg 3.

## Leg 2 — The observed tail against the null tail

| Quantity | Value |
|---|---|
| Best cell of the grid (real) | 1.4697 |
| Best cell of the block null | 9.6992 |
| Null cells at or above the real best | 16 |
| Family-wise probability of a null cell reaching the real best | 1.0000 |
| Cells where the real rule beats its own block null | 3000 of 17556 |
| Two-sided sign test on that comparison | 0.00e+00 |
| Same comparison on the gross profit factor (no cost drag) | 2678 of 17556 |
| Two-sided sign test on the gross comparison | 0.00e+00 |

## Verdict

- 6 real cells clear the §3.4 out-of-sample gate against None timing-null cells: the gate's false-positive rate under no information is 0.00% of the grid.
- The best real cell (net PF 1.4697) sits against a best null cell of n/a; the family-wise probability that a null cell reaches the real best is 1.0000.
- The real rule beats its own timing null in 3000 of 17556 cells (sign test p = 0.00e+00).

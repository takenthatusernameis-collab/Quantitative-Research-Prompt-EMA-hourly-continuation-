# Randomized-Entry Null — EMA Hourly Continuation Grid

**Source run:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T11:11:27.003510+00:00
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
| Cells re-run on the full history | 24 |
| Recomputed full-sample net PF equals the stored grid summary | 24 of 24 |
| Windowed run equals the full-history in-window trades | 24 of 24 |
| Vectorized signal generator equals the reference generator | 24 of 24 |

## Leg 1 — The null grid

| Statistic | Real rule | block null | timing null | sign null |
|---|---|---|---|---|
| mean out-of-sample net PF | 0.4321 | 0.5444 | 0.4952 | 0.4605 |
| median out-of-sample net PF | 0.4342 | 0.5285 | 0.4849 | 0.4644 |
| p95 out-of-sample net PF | 0.7200 | 0.8581 | 0.7505 | 0.7383 |
| max out-of-sample net PF | 1.4697 | 2.2215 | 1.5873 | 1.6955 |

| Gate (out-of-sample leg) | Real rule | block null | timing null | sign null |
|---|---|---|---|---|
| Cells with out-of-sample net PF > 1 | 77 | 313 | 83 | 37 |
| Cells clearing the §3.4 out-of-sample gate | 6 | 21 | 7 | 0 |
| Pooled out-of-sample net PF | 0.4175 | 0.5114 | 0.4698 | 0.4469 |
| Cells with gross out-of-sample PF > 1 | 2384 | 9188 | 4806 | 4176 |
| Median gross out-of-sample net PF | 0.8326 | 1.0109 | 0.9086 | 0.8964 |
| Median out-of-sample trades per cell | 262.0000 | 205.0000 | 202.0000 | 262.0000 |
| Median risk distance (share of entry price) | 1.1191% | 1.7215% | 1.7847% | 1.1191% |

Gate: out-of-sample net PF > 1, out-of-sample Sharpe > 0, at least min_trades out-of-sample trades, and out-of-sample net PF still > 1 under the cost stress.

## Leg 2 — The observed tail against the null tail

| Statistic | Real rule | block null | timing null | sign null |
|---|------|---|---|
| Best cell of the grid | 1.4697 | 2.2215 | 1.5873 | 1.6955 |
| Null cells at or above the real best | - | 14 | 4 | 2 |
| Family-wise probability of a null cell reaching the real best | - | 1 - 8.27e-07 | 0.9817 | 0.8647 |
| Cells where the real rule beats its own null | - | 2964 | 5382 | 6131 |
| Cells where the null beats the real rule | - | 14592 | 12174 | 11425 |
| Two-sided sign test on that comparison | - | 0.00e+00 | 0.00e+00 | 0.00e+00 |
| Same comparison on the gross profit factor (no cost drag) | - | 2606 | 5534 | 5947 |
| Two-sided sign test on the gross comparison | - | 0.00e+00 | 0.00e+00 | 0.00e+00 |

A sign test p-value this small means the two sides of the comparison are not exchangeable. The direction is the point: the counts above say which side of the comparison the rule is on.

## Leg 3 — The surviving cells against their own randomizations

Each cell is re-randomized many times. The p-value is the share of randomizations that reach the observed out-of-sample net PF, corrected for the number of cells the program tested (Bonferroni over 17556 cells). The control cells are ordinary cells that did not survive the audit; they show what the same test does on a cell with no reason to look good.

| Symbol | Cell | Group | OOS PF | Null mean PF | Null max PF | p-value | p x grid | Null gate pass rate |
|---|---|---|---|---|---|---|---|---|
| BRETT/USDT | P8_200 | survivor | 1.3323 | 0.6790 | 1.4531 | 0.0328 | 1.0000 | 1.7% |
| MERL/USDT | P8_200 | survivor | 1.2518 | 0.6489 | 1.0318 | 0.0164 | 1.0000 | 0.0% |
| GRT/USDT | P20_200 | survivor | 1.3413 | 0.6818 | 1.5706 | 0.0328 | 1.0000 | 3.3% |
| GRT/USDT | P8_200 | survivor | 1.1224 | 0.6374 | 0.9973 | 0.0164 | 1.0000 | 0.0% |
| DEXE/USDT | P12_200 | survivor | 1.1885 | 0.6893 | 1.1631 | 0.0164 | 1.0000 | 0.0% |
| DEXE/USDT | P20_200 | survivor | 1.1492 | 0.7367 | 1.1361 | 0.0164 | 1.0000 | 0.0% |
| DEXE/USDT | P21_200 | survivor | 1.1552 | 0.7307 | 1.2601 | 0.0492 | 1.0000 | 1.7% |
| DEXE/USDT | P26_200 | survivor | 1.0253 | 0.7244 | 1.0324 | 0.0328 | 1.0000 | 0.0% |
| DEXE/USDT | P50_200 | survivor | 1.3819 | 0.7749 | 1.3315 | 0.0164 | 1.0000 | 3.3% |
| DEXE/USDT | P55_200 | survivor | 1.3647 | 0.7339 | 1.2777 | 0.0164 | 1.0000 | 3.3% |
| BDX/USDT | P20_26 | control | 0.0282 | 0.1357 | 0.2124 | 1.0000 | 1.0000 | 0.0% |
| AGLD/USDT | P8_20 | control | 0.4745 | 0.4119 | 0.5026 | 0.1148 | 1.0000 | 0.0% |
| ANYONE/USDT | P8_100 | control | 0.6662 | 0.6270 | 0.8314 | 0.3607 | 1.0000 | 0.0% |
| APE/USDT | P50_200 | control | 0.8302 | 0.7702 | 1.6134 | 0.3443 | 1.0000 | 1.7% |
| DIA/USDT | P8_21 | control | 0.3886 | 0.3778 | 0.4895 | 0.4098 | 1.0000 | 0.0% |
| FLR/USDT | P20_26 | control | 0.1058 | 0.2998 | 0.3887 | 1.0000 | 1.0000 | 0.0% |
| BTC/USDT | P21_100 | control | 0.4453 | 0.4170 | 0.5945 | 0.3770 | 1.0000 | 0.0% |
| COMP/USDT | P12_89 | control | 0.7274 | 0.5015 | 0.7394 | 0.0328 | 1.0000 | 0.0% |
| SKL/USDT | P50_55 | control | 0.1698 | 0.4823 | 0.7161 | 1.0000 | 1.0000 | 0.0% |
| PENDLE/USDT | P50_89 | control | 0.5966 | 0.6133 | 0.9630 | 0.4426 | 1.0000 | 0.0% |
| SYN/USDT | P20_26 | control | 0.3107 | 0.4486 | 0.6251 | 0.9836 | 1.0000 | 0.0% |
| SOL/USDT | P21_89 | control | 0.4086 | 0.4212 | 0.6245 | 0.6393 | 1.0000 | 0.0% |

With 60 randomizations the smallest attainable p-value is 1/(60 + 1). The Bonferroni column can therefore not reach significance for a single cell: this leg can show that a surviving cell is *indistinguishable* from its own null, which is what it shows, but it cannot promote one.

The same cells under the sign null (same entry bars, random direction):

| Symbol | Cell | OOS PF | Sign-null mean PF | Sign-null max PF | p-value | p x grid |
|---|---|---|---|---|---|---|
| BRETT/USDT | P8_200 | 1.3323 | 0.7722 | 1.5309 | 0.0492 | 1.0000 |
| MERL/USDT | P8_200 | 1.2518 | 0.8492 | 1.5224 | 0.1639 | 1.0000 |
| GRT/USDT | P20_200 | 1.3413 | 0.8428 | 1.6017 | 0.0328 | 1.0000 |
| GRT/USDT | P8_200 | 1.1224 | 0.7640 | 1.3443 | 0.0656 | 1.0000 |
| DEXE/USDT | P12_200 | 1.1885 | 0.8435 | 1.5308 | 0.0820 | 1.0000 |
| DEXE/USDT | P20_200 | 1.1492 | 0.8189 | 1.2931 | 0.0820 | 1.0000 |
| DEXE/USDT | P21_200 | 1.1552 | 0.7955 | 1.1439 | 0.0164 | 1.0000 |
| DEXE/USDT | P26_200 | 1.0253 | 0.8615 | 1.2553 | 0.1803 | 1.0000 |
| DEXE/USDT | P50_200 | 1.3819 | 0.7932 | 1.2425 | 0.0164 | 1.0000 |
| DEXE/USDT | P55_200 | 1.3647 | 0.7563 | 1.0577 | 0.0164 | 1.0000 |
| BDX/USDT | P20_26 | 0.0282 | 0.0491 | 0.0768 | 1.0000 | 1.0000 |
| AGLD/USDT | P8_20 | 0.4745 | 0.4808 | 0.5814 | 0.5246 | 1.0000 |
| ANYONE/USDT | P8_100 | 0.6662 | 0.6892 | 0.9202 | 0.5574 | 1.0000 |
| APE/USDT | P50_200 | 0.8302 | 0.7064 | 0.9920 | 0.1475 | 1.0000 |
| DIA/USDT | P8_21 | 0.3886 | 0.4017 | 0.5263 | 0.5574 | 1.0000 |
| FLR/USDT | P20_26 | 0.1058 | 0.1673 | 0.2133 | 1.0000 | 1.0000 |
| BTC/USDT | P21_100 | 0.4453 | 0.4135 | 0.5298 | 0.2295 | 1.0000 |
| COMP/USDT | P12_89 | 0.7274 | 0.5594 | 0.7354 | 0.0492 | 1.0000 |
| SKL/USDT | P50_55 | 0.1698 | 0.1859 | 0.2528 | 0.7705 | 1.0000 |
| PENDLE/USDT | P50_89 | 0.5966 | 0.5153 | 0.6747 | 0.0656 | 1.0000 |
| SYN/USDT | P20_26 | 0.3107 | 0.3266 | 0.4179 | 0.6557 | 1.0000 |
| SOL/USDT | P21_89 | 0.4086 | 0.4084 | 0.5892 | 0.4590 | 1.0000 |

## Verdict

- 77 of 17556 cells show an out-of-sample net PF above 1; the block null produces 313. The observed tail is no larger than what the block null delivers.
- 6 real cells clear the §3.4 out-of-sample gate against 21 block-null cells: the gate's false-positive rate under no information is 0.12% of the grid.
- The best real cell (net PF 1.4697) sits against a best block cell of 2.2215; the family-wise probability that a null cell reaches the real best is 1 - 8.27e-07.
- The real rule beats its own block null in 2964 of 17556 cells and loses to it in 14592 (sign test p = 0.00e+00).
- Grid-wide null counts (cells with an out-of-sample net PF above 1 / cells clearing the gate): real 77/6; block 313/21; timing 83/7; sign 37/0.
- 10 surviving cells were re-randomized; 0 keep an out-of-sample net PF above the real one at a Bonferroni-corrected level over 17556 tests.

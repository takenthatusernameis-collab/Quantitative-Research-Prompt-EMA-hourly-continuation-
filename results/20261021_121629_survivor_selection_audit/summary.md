# Survivor Selection Audit — EMA Hourly Continuation

**Source run:** `results/20261019_135940_grid`
**Out-of-sample audit:** `results/20261021_033523_oos_grid_scan`
**Generated:** 2026-10-21T12:19:11.541019+00:00
**Universe:** 266 symbols, 17556 grid cells
**Cost model:** 10.0 bps taker + 2.0 bps slippage per side (stress leg: 2x)

## Why this leg exists

Ten cells out of 17 556 clear the out-of-sample gate. The program decision rests on them, and two questions about that set were still open: is the family a property of the rule or of the one or two symbols it sits on, and does the *selection* survive a walk-forward that never shows the selection the data it is scored on.

## Leg 1 — the family

| Symbol | Cell | OOS trades | OOS net PF | OOS PF (2x costs) | Full-sample net PF | Exact OOS PF | Exact OOS PF (2x) |
|---|---|---|---|---|---|---|---|
| DEXE/USDT | P21_200 | 75 | 1.4985 | 1.3136 | 0.8209 | 1.1552 | 0.9027 |
| DEXE/USDT | P20_200 | 77 | 1.4790 | 1.2967 | 0.7855 | 1.1492 | 0.9157 |
| GRT/USDT | P20_200 | 61 | 1.4547 | 1.2401 | 0.9087 | 1.3413 | 1.0976 |
| DEXE/USDT | P50_200 | 86 | 1.3565 | 1.1165 | 0.8058 | 1.3819 | 1.1322 |
| DEXE/USDT | P55_200 | 81 | 1.3378 | 1.0789 | 0.7535 | 1.3647 | 1.0975 |
| GRT/USDT | P8_200 | 64 | 1.3136 | 1.0548 | 0.7535 | 1.1224 | 0.8598 |
| BRETT/USDT | P8_200 | 51 | 1.3107 | 1.0111 | 0.8337 | 1.3323 | 1.0489 |
| MERL/USDT | P8_200 | 31 | 1.2518 | 1.0215 | 0.8224 | 1.2518 | 1.0101 |
| DEXE/USDT | P12_200 | 79 | 1.2103 | 1.0325 | 0.8169 | 1.1885 | 0.9892 |
| DEXE/USDT | P26_200 | 73 | 1.1484 | 1.0066 | 0.8041 | 1.0253 | 0.8405 |

Pooled over the family: net PF **1.3353**, under 2x costs **1.1183**, net P&L 6,831. The family sits on 4 symbols: BRETT/USDT, DEXE/USDT, GRT/USDT, MERL/USDT.

| Symbol | Family cells | Family trades | Share of the family net P&L | Pooled net PF | Pooled net PF (2x) |
|---|---|---|---|---|---|
| BRETT/USDT | 1 | 51 | 8.3% | 1.3107 | 1.0111 |
| DEXE/USDT | 6 | 471 | 66.5% | 1.3300 | 1.1318 |
| GRT/USDT | 2 | 125 | 21.4% | 1.3895 | 1.1525 |
| MERL/USDT | 1 | 31 | 3.8% | 1.2518 | 1.0215 |

## Leg 2 — leave-one-symbol-out

Every symbol of the family is dropped in turn. The gate family loses that symbol's cells; the ranked family is re-selected from the remaining cells, so the cells that would replace them are visible.

| Dropped symbol | Cells dropped | Family cells left | Pooled net PF without it | Pooled net PF (2x) without it | Ranked family: original cells kept | Newcomers | Newcomers that clear the gate | Ranked family net PF | Ranked family net PF (2x) | Ranked family clears the gates |
|---|---|---|---|---|---|---|---|---|---|---|
| BRETT/USDT | 1 | 9 | 1.3377 | 1.1297 | 7 | 3 | 0 | 1.3413 | 1.0846 | yes |
| DEXE/USDT | 6 | 4 | 1.3463 | 1.0914 | 4 | 6 | 0 | 1.2478 | 0.9680 | no |
| GRT/USDT | 2 | 8 | 1.3230 | 1.1106 | 6 | 4 | 0 | 1.3133 | 1.0377 | yes |
| MERL/USDT | 1 | 9 | 1.3397 | 1.1236 | 7 | 3 | 0 | 1.3429 | 1.0813 | yes |

- Without BRETT/USDT the family is topped up by W/USDT P12_200 (PF 1.2628, stress 0.9698), GMT/USDT P8_200 (PF 1.2524, stress 0.9129), DEXE/USDT P100_200 (PF 1.2440, stress 0.9975).
- Without DEXE/USDT the family is topped up by W/USDT P12_200 (PF 1.2628, stress 0.9698), GMT/USDT P8_200 (PF 1.2524, stress 0.9129), IMX/USDT P26_200 (PF 1.2361, stress 0.9136), IMX/USDT P34_200 (PF 1.2027, stress 0.9120), PUFFER/USDT P21_144 (PF 1.1866, stress 0.9929), SYN/USDT P20_200 (PF 1.1832, stress 0.9062).
- Without GRT/USDT the family is topped up by W/USDT P12_200 (PF 1.2628, stress 0.9698), GMT/USDT P8_200 (PF 1.2524, stress 0.9129), DEXE/USDT P100_200 (PF 1.2440, stress 0.9975), IMX/USDT P26_200 (PF 1.2361, stress 0.9136).
- Without MERL/USDT the family is topped up by W/USDT P12_200 (PF 1.2628, stress 0.9698), GMT/USDT P8_200 (PF 1.2524, stress 0.9129), DEXE/USDT P100_200 (PF 1.2440, stress 0.9975).

## Leg 3 — walk-forward re-selection over the whole grid

The full sample of every symbol is cut into 5 sequential folds. At step k the best cell of the symbol is chosen on the history (folds 1..k, at least 20 trades) and scored on fold k+1, which the selection never saw. Every cell of the grid takes part; nothing is selected in advance.

| Step (history -> test fold) | Symbols scored | Steps with a selection | Out-of-fold PF > 1 | Pooled out-of-fold net PF | Pooled out-of-fold net PF (2x) | Median in-fold net PF |
|---|---|---|---|---|---|---|
| 1 -> 2 | 266 | 266 | 37 (13.9%) | 0.7192 | 0.5384 | 0.9090 |
| 2 -> 3 | 266 | 266 | 12 (4.5%) | 0.6226 | 0.4361 | 0.8666 |
| 3 -> 4 | 266 | 266 | 17 (6.4%) | 0.6026 | 0.4120 | 0.8127 |
| 4 -> 5 | 266 | 266 | 20 (7.6%) | 0.5979 | 0.4016 | 0.7703 |

| Pooled over every step | Value |
|---|---|
| Walk-forward steps scored | 1060 |
| Out-of-fold trades | 95786 |
| Pooled out-of-fold net PF | 0.6409 |
| Pooled out-of-fold net PF (2x costs) | 0.4521 |
| Out-of-fold windows with net PF > 1 | 86 (8.1%) |
| Out-of-fold windows with net PF > 1 under 2x costs | 31 (2.9%) |
| Median in-fold net PF of the selected cell | 0.8272 |
| Median out-of-fold net PF of the selected cell | 0.6217 |

### Leg 3b — the selected cells against the grid's own null

The null needs no randomization: the grid itself holds 17 556 draws of what a cell scores on a fold it was not selected on. If the selection carries information, the selected cells have to sit at the top of that distribution; if it does not, they sit where a random cell would.

| Step | Null cells | Null median PF | Null mean PF | Null share above PF 1 | Null p95 | Selected cells above the null p95 |
|---|---|---|---|---|---|---|
| 1 -> 2 | 17556 | 0.5502 | 0.5623 | 3.3% | 0.9356 | 37 / 266 |
| 2 -> 3 | 17519 | 0.4957 | 0.4985 | 1.2% | 0.8198 | 12 / 266 |
| 3 -> 4 | 17487 | 0.4498 | 0.4589 | 1.4% | 0.7971 | 17 / 264 |
| 4 -> 5 | 17428 | 0.4136 | 0.4291 | 1.2% | 0.7826 | 20 / 264 |

| Measure | Value |
|---|---|
| Selected cells scored | 1057 |
| Median percentile of the selected cells in the null distribution | 0.7768 |
| Selected cells above the null 95th percentile | 198 (18.7%) |
| Expected under a null pick | 52.9 |
| One-sided exact binomial p-value, P(X >= observed) | 1.893e-57 |

## Leg 4 — sub-period stability of the closest survivors

The out-of-sample window of the 6 closest survivors is cut into 4 sequential sub-periods. An edge that is real has to show up in more than one of them.

| Symbol | Cell | PF sub 1 | PF sub 2 | PF sub 3 | PF sub 4 | Sub-periods with PF > 1 | Sub-periods with PF > 1 (2x costs) | Sub-periods with trades |
|---|---|---|---|---|---|---|---|---|
| BRETT/USDT | P8_200 | 2.8570 | 3.8129 | 1.6913 | 0.8022 | 3/4 | 3/4 | 4/4 |
| DEXE/USDT | P50_200 | 0.8737 | 2.4479 | 1.2895 | n/a | 2/3 | 2/3 | 3/4 |
| DEXE/USDT | P55_200 | 0.9321 | 2.2558 | 1.3397 | n/a | 2/3 | 2/3 | 3/4 |
| GRT/USDT | P20_200 | 2.0350 | inf | 1.7977 | 0.9909 | 3/4 | 3/4 | 4/4 |
| MERL/USDT | P8_200 | 1.2518 | n/a | n/a | n/a | 1/1 | 1/1 | 1/4 |
| ZEN/USDT | P12_200 | 1.3311 | 0.8267 | 0.8206 | 1.4530 | 2/4 | 2/4 | 4/4 |

A sub-period without a single trade has no profit factor: it is missing evidence, not a loss. The last column therefore shows how many of the sub-periods carry any trades at all.

The sub-periods are thin: the median sub-period of the closest survivors holds 22 trades, so this leg reads the stability of the edge, not its size.

| Symbol | Cell | Trades per sub-period |
|---|---|---|
| BRETT/USDT | P8_200 | 8, 5, 13, 25 |
| DEXE/USDT | P50_200 | 33, 27, 26, 0 |
| DEXE/USDT | P55_200 | 32, 22, 27, 0 |
| GRT/USDT | P20_200 | 13, 1, 22, 25 |
| MERL/USDT | P8_200 | 31, 0, 0, 0 |
| ZEN/USDT | P12_200 | 22, 4, 12, 4 |

## Verdict

- The 10-cell survivor family is concentrated in 4 symbols; dropping the dominant symbol leaves 4 of the 10 cells.
- Re-selecting the family from the remaining cells keeps 4-7 of the original cells, so the family is not stable under a leave-one-symbol-out.
- Walk-forward: the procedure picks a cell on the history (median in-fold net PF 0.8272) and the same cell nets a median out-of-fold PF of 0.6217; the pooled out-of-fold net PF is 0.6409 over 95786 trades, and 8.1% of the out-of-fold windows land above PF 1 against the 1.8% the grid's own null produces on the same folds.
- The selected cells rank at a median of the 0.7768 percentile of that null, and 198 of 1057 beat its 95th percentile (one-sided exact binomial p 1.893e-57): the selection does rank the cells, it just never ranks one into a net-profitable window.
- Sub-period stability: 0 of 6 closest survivors keep PF above 1 in every out-of-sample sub-period that carries trades.
- The out-of-sample gate is measuring a window, not a rule: the survivors do not survive their own walk-forward, and the family collapses onto a handful of symbols.

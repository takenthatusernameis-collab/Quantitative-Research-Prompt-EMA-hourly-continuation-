# Mutation Evaluation — ATR Minimum-Risk (PROMPT.md §5.2)

**Parent run:** `results/20261019_135940_grid`
**Child run:** `results/20261022_134500_grid`
**Generated:** 2026-10-23T04:56:46.385196+00:00
**Compared symbol set:** 275 symbols (66 EMA pairs each, 18150 cells per run)
**Out-of-sample window:** trailing 35% of each symbol's bars
**Cost stress:** 2x fees and slippage

## Leg 1 — the mutation is a single variable

| Config key | Parent | Child |
|---|---|---|
| atr_threshold | 1.0 | 1.0 |
| conservative_exit | True | True |
| max_notional_multiple | 10.0 | 10.0 |
| min_risk_atr | False | False |
| risk_fraction | 0.01 | 0.01 |
| rr | 1.0 | 1.0 |
| sizing | risk | risk |
| slippage_bps | 2.0 | 2.0 |
| stricter_trend | False | True **<- changed** |
| taker_fee_bps | 10.0 | 10.0 |

Changed keys: `stricter_trend`. Single-variable mutation: **False**.

## Leg 2 — parent -> child -> delta (full sample)

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Cells | 18150 | 18150 | 0 |
| Symbols | 275 | 275 | 0 |
| Trades | 14676563 | 14676563 | 0 |
| Mean cell net PF | 0.4987 | 0.4987 | 0.0000 |
| Median cell net PF | 0.5198 | 0.5198 | 0.0000 |
| Pooled net PF | 0.5219 | 0.5219 | 0.0000 |
| Pooled gross PF | 0.8853 | 0.8853 | 0.0000 |
| Pooled net P&L | -154248039.35 | -154248039.35 | 0.00 |
| Total costs | 126273955.33 | 126273955.33 | 0.00 |
| Costs per trade | 8.60 | 8.60 | 0.00 |
| Cost share of gross profit | 58.5% | 58.5% | +0.0 pp |
| Cells with net PF > 1 | 37 | 37 | 0 |
| Cells without a trade | 0 | 0 | 0 |

## Leg 3 — parent -> child -> delta (out of sample)

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Pooled OOS net PF | 0.5282 | 0.5282 | 0.0000 |
| Pooled OOS net PF (2x costs) | 0.3265 | 0.3265 | 0.0000 |
| Cells with OOS net PF > 1 | 77 | 77 | 0 |
| Cells with OOS net PF > 1 and >= 30 OOS trades | 75 | 75 | 0 |
| Cells clearing the full §3.4 gate | 10 | 10 | 0 |

### Leg 3b — the closest child cells

The cells the mutation brings closest to the gate: the out-of-sample net PF at the registered costs, the same under 2x costs, and the full-sample result a promotion would also have to survive.

| Symbol | Cell | OOS trades | OOS net PF | OOS net PF (2x costs) | Full-sample net PF | Clears the gate |
|---|---|---|---|---|---|---|
| DEXE/USDT | P21_200 | 75 | 1.4985 | 1.3136 | 0.8209 | yes |
| DEXE/USDT | P20_200 | 77 | 1.4790 | 1.2967 | 0.7855 | yes |
| GRT/USDT | P20_200 | 61 | 1.4547 | 1.2401 | 0.9087 | yes |
| DEXE/USDT | P50_200 | 86 | 1.3565 | 1.1165 | 0.8058 | yes |
| DEXE/USDT | P55_200 | 81 | 1.3378 | 1.0789 | 0.7535 | yes |
| GRT/USDT | P8_200 | 64 | 1.3136 | 1.0548 | 0.7535 | yes |
| BRETT/USDT | P8_200 | 51 | 1.3107 | 1.0111 | 0.8337 | yes |
| W/USDT | P12_200 | 101 | 1.2628 | 0.9698 | 0.9613 | no |
| GMT/USDT | P8_200 | 111 | 1.2524 | 0.9129 | 0.7126 | no |
| MERL/USDT | P8_200 | 31 | 1.2518 | 1.0215 | 0.8224 | yes |

## Leg 4 — the walk-forward selection, parent vs child

The full sample of every symbol is cut into 5 sequential folds. At step k the best cell of the symbol is chosen on the history and scored on fold k+1, which the selection never saw. This is the comparison that matters: it scores the *procedure*, not a cell that was picked because it looked good.

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Walk-forward steps scored | 1092 | 1092 | 0 |
| Out-of-fold trades | 98164 | 98164 | 0 |
| Pooled out-of-fold net PF | 0.6404 | 0.6404 | 0.0000 |
| Pooled out-of-fold net PF (2x costs) | 0.4524 | 0.4524 | 0.0000 |
| Out-of-fold windows with net PF > 1 | 90 | 90 | 0 |
| Share of out-of-fold windows with net PF > 1 | 8.2% | 8.2% | +0.0 pp |
| Median in-fold net PF of the selected cell | 0.8315 | 0.8315 | 0.0000 |
| Median out-of-fold net PF of the selected cell | 0.6217 | 0.6217 | 0.0000 |

| Selection against the grid's own null | Parent | Child |
|---|---|---|
| Median percentile of the selected cells | 0.7770 | 0.7770 |
| Selected cells above the null p95 | 207 of 1089 | 207 of 1089 |
| One-sided exact binomial p-value | 0.0000 | 0.0000 |

## Leg 5 — reproducibility of the child cells

| Symbol | Cell | Max absolute difference vs the stored summary |
|---|---|---|
| BTC/USDT | P8_12 | 0.00e+00 |
| BDX/USDT | P8_12 | 0.00e+00 |
| RSR/USDT | P8_12 | 0.00e+00 |
| CFG/USDT | P8_12 | 0.00e+00 |
| ERG/USDT | P8_12 | 0.00e+00 |

A child cell re-run through the real backtest reproduces the stored summary exactly, so the child run is the engine the baseline run used, with the mutation applied.

## Verdict

- The child grid trades 14676563 trades against the parent's 14676563 on the same 275 symbols (+0.0 %), and the pooled net profit factor moves from 0.5219 to 0.5219.
- The cost of a trade falls from 8.60 to 8.60, and the costs as a share of the gross profit move from 58.5% to 58.5%: the ATR minimum-risk filter buys back cost drag by trading less, not by trading better.
- Out of sample the child's pooled net PF is 0.5282 against the parent's 0.5282, and the cells that clear the full §3.4 gate are 10 against 10.
- The walk-forward leg, which scores the *procedure* and never shows the selection the data it is judged on, moves the pooled out-of-fold net PF from 0.6404 to 0.6404 (2x costs: 0.4524 -> 0.4524).
- The mutation does not improve the walk-forward number: it thins the sample without creating an edge, which is what the cost-drag leg predicted.
- 10 child cells clear the PROMPT.md §3.4 gate (10 of 18150 cells on 4 symbols: DEXE/USDT 6, GRT/USDT 2, BRETT/USDT 1, MERL/USDT 1). A cell that clears the gate is a selection result, not a promotion: the child grid's own null puts 1.8% of its folds above PF 1 with a median PF of 0.4746, and the walk-forward selection ranks at the 0.7770 percentile of that null (one-sided binomial p 0.0000). The gate-clearing cells have to survive the child's own null leg, the walk-forward and the sub-period leg before any of them can be promoted; until then the baseline grid stays the program's grid.

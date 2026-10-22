# Mutation Evaluation — ATR Minimum-Risk (PROMPT.md §5.2)

**Parent run:** `results/20261019_135940_grid`
**Child run:** `results/20261021_172619_grid`
**Generated:** 2026-10-22T00:29:13.449958+00:00
**Compared symbol set:** 266 symbols (66 EMA pairs each, 17556 cells per run)
**Out-of-sample window:** trailing 35% of each symbol's bars
**Cost stress:** 2x fees and slippage

## Leg 1 — the mutation is a single variable

| Config key | Parent | Child |
|---|---|---|
| atr_threshold | 1.0 | 1.0 |
| conservative_exit | True | True |
| max_notional_multiple | 10.0 | 10.0 |
| min_risk_atr | False | True **<- changed** |
| risk_fraction | 0.01 | 0.01 |
| rr | 1.0 | 1.0 |
| sizing | risk | risk |
| slippage_bps | 2.0 | 2.0 |
| stricter_trend | False | False |
| taker_fee_bps | 10.0 | 10.0 |

Changed keys: `min_risk_atr`. Single-variable mutation: **True**.

## Leg 2 — parent -> child -> delta (full sample)

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Cells | 17556 | 17556 | 0 |
| Symbols | 266 | 266 | 0 |
| Trades | 14241237 | 6913033 | -7328204 |
| Mean cell net PF | 0.4993 | 0.7264 | 0.2271 |
| Median cell net PF | 0.5205 | 0.7322 | 0.2116 |
| Pooled net PF | 0.5225 | 0.7347 | 0.2123 |
| Pooled gross PF | 0.8872 | 0.9636 | 0.0764 |
| Pooled net P&L | -149215079.23 | -79740412.85 | 69474666.38 |
| Total costs | 122586776.97 | 70115958.77 | -52470818.20 |
| Costs per trade | 8.61 | 10.14 | 1.53 |
| Cost share of gross profit | 58.5% | 27.5% | -31.0 pp |
| Cells with net PF > 1 | 36 | 287 | 251 |
| Cells without a trade | 0 | 0 | 0 |

## Leg 3 — parent -> child -> delta (out of sample)

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Pooled OOS net PF | 0.5298 | 0.6676 | 0.1378 |
| Pooled OOS net PF (2x costs) | 0.3266 | 0.4781 | 0.1515 |
| Cells with OOS net PF > 1 | 77 | 608 | 531 |
| Cells with OOS net PF > 1 and >= 30 OOS trades | 75 | 591 | 516 |
| Cells clearing the full §3.4 gate | 10 | 106 | 96 |

### Leg 3b — the closest child cells

The cells the mutation brings closest to the gate: the out-of-sample net PF at the registered costs, the same under 2x costs, and the full-sample result a promotion would also have to survive.

| Symbol | Cell | OOS trades | OOS net PF | OOS net PF (2x costs) | Full-sample net PF | Clears the gate |
|---|---|---|---|---|---|---|
| DEXE/USDT | P55_200 | 63 | 1.8907 | 1.6783 | 0.9677 | yes |
| DEXE/USDT | P50_200 | 70 | 1.7875 | 1.5833 | 1.0694 | yes |
| DEXE/USDT | P89_200 | 56 | 1.7875 | 1.5267 | 0.8904 | yes |
| BRETT/USDT | P8_200 | 42 | 1.6802 | 1.5168 | 1.0449 | yes |
| DEXE/USDT | P21_200 | 64 | 1.6713 | 1.5219 | 0.9970 | yes |
| DEXE/USDT | P20_200 | 66 | 1.6404 | 1.4926 | 0.9864 | yes |
| DEXE/USDT | P100_200 | 61 | 1.6140 | 1.3740 | 0.8062 | yes |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.3857 | 1.1216 | yes |
| XPR/USDT | P8_200 | 44 | 1.5710 | 1.3538 | 0.9178 | yes |
| FET/USDT | P12_200 | 36 | 1.5616 | 1.4435 | 1.0341 | yes |

## Leg 4 — the walk-forward selection, parent vs child

The full sample of every symbol is cut into 5 sequential folds. At step k the best cell of the symbol is chosen on the history and scored on fold k+1, which the selection never saw. This is the comparison that matters: it scores the *procedure*, not a cell that was picked because it looked good.

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Walk-forward steps scored | 1060 | 1061 | 1 |
| Out-of-fold trades | 95786 | 60853 | -34933 |
| Pooled out-of-fold net PF | 0.6409 | 0.7390 | 0.0981 |
| Pooled out-of-fold net PF (2x costs) | 0.4521 | 0.5731 | 0.1209 |
| Out-of-fold windows with net PF > 1 | 86 | 175 | 89 |
| Share of out-of-fold windows with net PF > 1 | 8.1% | 16.5% | +8.4 pp |
| Median in-fold net PF of the selected cell | 0.8272 | 1.0906 | 0.2634 |
| Median out-of-fold net PF of the selected cell | 0.6217 | 0.7347 | 0.1131 |

| Selection against the grid's own null | Parent | Child |
|---|---|---|
| Median percentile of the selected cells | 0.7768 | 0.5565 |
| Selected cells above the null p95 | 198 of 1057 | 106 of 1059 |
| One-sided exact binomial p-value | 0.0000 | 0.0000 |

## Leg 5 — reproducibility of the child cells

| Symbol | Cell | Max absolute difference vs the stored summary |
|---|---|---|
| BTC/USDT | P8_12 | 0.00e+00 |
| DASH/USDT | P8_12 | 0.00e+00 |
| XEC/USDT | P8_12 | 0.00e+00 |
| CELO/USDT | P8_12 | 0.00e+00 |
| ILV/USDT | P8_12 | 0.00e+00 |

A child cell re-run through the real backtest reproduces the stored summary exactly, so the child run is the engine the baseline run used, with the mutation applied.

## Verdict

- The child grid trades 6913033 trades against the parent's 14241237 on the same 266 symbols (-51.5 %), and the pooled net profit factor moves from 0.5225 to 0.7347.
- The cost of a trade falls from 8.61 to 10.14, and the costs as a share of the gross profit move from 58.5% to 27.5%: the ATR minimum-risk filter buys back cost drag by trading less, not by trading better.
- Out of sample the child's pooled net PF is 0.6676 against the parent's 0.5298, and the cells that clear the full §3.4 gate are 106 against 10.
- The walk-forward leg, which scores the *procedure* and never shows the selection the data it is judged on, moves the pooled out-of-fold net PF from 0.6409 to 0.7390 (2x costs: 0.4521 -> 0.5731).
- The yardstick is the parent's walk-forward pooled out-of-fold net PF over the full 266 symbols: 0.6409 (0.4521 under 2x costs). The child has to beat that number on its own symbol set to be worth anything.
- The mutation improves the walk-forward number, but the improvement is a cost effect (fewer, wider trades) and not a new edge.
- 106 child cells clear the PROMPT.md §3.4 gate (106 of 17556 cells on 39 symbols: DEXE/USDT 18, IMX/USDT 7, ENA/USDT 5, POL/USDT 5, APT/USDT 5). A cell that clears the gate is a selection result, not a promotion: the child grid's own null puts 10.6% of its folds above PF 1 with a median PF of 0.7050, and the walk-forward selection ranks at the 0.5565 percentile of that null (one-sided binomial p 0.0000). The gate-clearing cells have to survive the child's own null leg, the walk-forward and the sub-period leg before any of them can be promoted; until then the baseline grid stays the program's grid.

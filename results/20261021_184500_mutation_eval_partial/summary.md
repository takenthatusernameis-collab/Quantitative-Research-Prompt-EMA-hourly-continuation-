# Mutation Evaluation — ATR Minimum-Risk (PROMPT.md §5.2)

**Parent run:** `results/20261019_135940_grid`
**Child run:** `results/20261021_172619_grid`
**Generated:** 2026-10-21T18:43:25.715649+00:00
**Compared symbol set:** 24 symbols (66 EMA pairs each, 1584 cells per run)
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
| Cells | 1584 | 1584 | 0 |
| Symbols | 24 | 24 | 0 |
| Trades | 1321166 | 561560 | -759606 |
| Mean cell net PF | 0.4254 | 0.7201 | 0.2947 |
| Median cell net PF | 0.4372 | 0.7211 | 0.2839 |
| Pooled net PF | 0.4561 | 0.7320 | 0.2759 |
| Pooled gross PF | 0.8982 | 1.0051 | 0.1069 |
| Pooled net P&L | -14156889.03 | -6655522.28 | 7501366.75 |
| Total costs | 12309042.43 | 6765954.10 | -5543088.33 |
| Costs per trade | 9.32 | 12.05 | 2.73 |
| Cost share of gross profit | 75.5% | 31.3% | -44.1 pp |
| Cells with net PF > 1 | 0 | 9 | 9 |
| Cells without a trade | 0 | 0 | 0 |

## Leg 3 — parent -> child -> delta (out of sample)

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Pooled OOS net PF | 0.4787 | 0.6759 | 0.1973 |
| Pooled OOS net PF (2x costs) | 0.2644 | 0.4585 | 0.1941 |
| Cells with OOS net PF > 1 | 2 | 44 | 42 |
| Cells with OOS net PF > 1 and >= 30 OOS trades | 1 | 38 | 37 |
| Cells clearing the full §3.4 gate | 0 | 0 | 0 |

### Leg 3b — the closest child cells

The cells the mutation brings closest to the gate: the out-of-sample net PF at the registered costs, the same under 2x costs, and the full-sample result a promotion would also have to survive.

| Symbol | Cell | OOS trades | OOS net PF | OOS net PF (2x costs) | Full-sample net PF | Clears the gate |
|---|---|---|---|---|---|---|
| NEAR/USDT | P100_144 | 76 | 1.2790 | 0.9474 | 0.8439 | no |
| ZEC/USDT | P8_12 | 61 | 1.2715 | 0.9755 | 0.8832 | no |
| UNI/USDT | P100_200 | 75 | 1.1924 | 0.9266 | 0.9594 | no |
| TAO/USDT | P8_12 | 62 | 1.1375 | 0.8113 | 1.0168 | no |
| ZEC/USDT | P12_100 | 137 | 1.1327 | 0.9739 | 0.9623 | no |
| AVAX/USDT | P26_200 | 61 | 1.1218 | 0.8621 | 0.9003 | no |
| LTC/USDT | P12_200 | 43 | 1.1151 | 0.8627 | 0.7312 | no |
| NEAR/USDT | P89_144 | 85 | 1.0923 | 0.8334 | 0.7610 | no |
| UNI/USDT | P89_200 | 74 | 1.0882 | 0.8601 | 0.9288 | no |
| SUI/USDT | P8_144 | 131 | 1.0759 | 0.8694 | 0.9520 | no |

## Leg 4 — the walk-forward selection, parent vs child

The full sample of every symbol is cut into 5 sequential folds. At step k the best cell of the symbol is chosen on the history and scored on fold k+1, which the selection never saw. This is the comparison that matters: it scores the *procedure*, not a cell that was picked because it looked good.

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Walk-forward steps scored | 96 | 96 | 0 |
| Out-of-fold trades | 8266 | 4618 | -3648 |
| Pooled out-of-fold net PF | 0.5942 | 0.7239 | 0.1297 |
| Pooled out-of-fold net PF (2x costs) | 0.3875 | 0.5370 | 0.1494 |
| Out-of-fold windows with net PF > 1 | 3 | 7 | 4 |
| Share of out-of-fold windows with net PF > 1 | 3.1% | 7.3% | +4.2 pp |
| Median in-fold net PF of the selected cell | 0.7609 | 1.0555 | 0.2946 |
| Median out-of-fold net PF of the selected cell | 0.5582 | 0.7217 | 0.1635 |

| Selection against the grid's own null | Parent | Child |
|---|---|---|
| Median percentile of the selected cells | 0.7797 | 0.5177 |
| Selected cells above the null p95 | 15 of 96 | 4 of 96 |
| One-sided exact binomial p-value | 0.0001 | 0.7128 |

## Leg 5 — reproducibility of the child cells

| Symbol | Cell | Max absolute difference vs the stored summary |
|---|---|---|
| BTC/USDT | P8_12 | 0.00e+00 |
| XRP/USDT | P8_12 | 0.00e+00 |
| XMR/USDT | P8_12 | 0.00e+00 |
| XLM/USDT | P8_12 | 0.00e+00 |
| AVAX/USDT | P8_12 | 0.00e+00 |

A child cell re-run through the real backtest reproduces the stored summary exactly, so the child run is the engine the baseline run used, with the mutation applied.

## Verdict

- The child grid trades 561560 trades against the parent's 1321166 on the same 24 symbols (-57.5 %), and the pooled net profit factor moves from 0.4561 to 0.7320.
- The cost of a trade falls from 9.32 to 12.05, and the costs as a share of the gross profit move from 75.5% to 31.3%: the ATR minimum-risk filter buys back cost drag by trading less, not by trading better.
- Out of sample the child's pooled net PF is 0.6759 against the parent's 0.4787, and the cells that clear the full §3.4 gate are 0 against 0.
- The walk-forward leg, which scores the *procedure* and never shows the selection the data it is judged on, moves the pooled out-of-fold net PF from 0.5942 to 0.7239 (2x costs: 0.3875 -> 0.5370).
- The yardstick is the parent's walk-forward pooled out-of-fold net PF over the full 266 symbols: 0.6409 (0.4521 under 2x costs). The child has to beat that number on its own symbol set to be worth anything.
- The mutation improves the walk-forward number, but the improvement is a cost effect (fewer, wider trades) and not a new edge: the program still has no cell that clears the gates out of sample.
- No child cell clears the PROMPT.md §3.4 gate, so the mutation cannot be promoted and the baseline grid stays the program's grid.

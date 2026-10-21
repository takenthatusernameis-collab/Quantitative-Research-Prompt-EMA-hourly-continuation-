# Mutation Evaluation — ATR Minimum-Risk (PROMPT.md §5.2)

**Parent run:** `results/20261019_135940_grid`
**Child run:** `results/20261021_172619_grid`
**Generated:** 2026-10-21T19:36:44.898502+00:00
**Compared symbol set:** 57 symbols (66 EMA pairs each, 3762 cells per run)
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
| Cells | 3762 | 3762 | 0 |
| Symbols | 57 | 57 | 0 |
| Trades | 3097113 | 1349555 | -1747558 |
| Mean cell net PF | 0.4548 | 0.7371 | 0.2823 |
| Median cell net PF | 0.4697 | 0.7517 | 0.2819 |
| Pooled net PF | 0.4864 | 0.7498 | 0.2635 |
| Pooled gross PF | 0.8942 | 1.0035 | 0.1093 |
| Pooled net P&L | -32617837.96 | -14977688.98 | 17640148.98 |
| Total costs | 27773657.95 | 15161516.90 | -12612141.05 |
| Costs per trade | 8.97 | 11.23 | 2.27 |
| Cost share of gross profit | 67.8% | 28.9% | -38.9 pp |
| Cells with net PF > 1 | 0 | 74 | 74 |
| Cells without a trade | 0 | 0 | 0 |

## Leg 3 — parent -> child -> delta (out of sample)

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Pooled OOS net PF | 0.5207 | 0.7041 | 0.1835 |
| Pooled OOS net PF (2x costs) | 0.3087 | 0.5015 | 0.1927 |
| Cells with OOS net PF > 1 | 12 | 176 | 164 |
| Cells with OOS net PF > 1 and >= 30 OOS trades | 10 | 164 | 154 |
| Cells clearing the full §3.4 gate | 0 | 19 | 19 |

### Leg 3b — the closest child cells

The cells the mutation brings closest to the gate: the out-of-sample net PF at the registered costs, the same under 2x costs, and the full-sample result a promotion would also have to survive.

| Symbol | Cell | OOS trades | OOS net PF | OOS net PF (2x costs) | Full-sample net PF | Clears the gate |
|---|---|---|---|---|---|---|
| POL/USDT | P8_200 | 52 | 1.6086 | 1.3857 | 1.1216 | yes |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.2155 | 1.0354 | yes |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.1151 | 1.0278 | yes |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.0315 | 1.3253 | yes |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.1647 | 0.9932 | yes |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.1617 | 1.0429 | yes |
| APT/USDT | P12_200 | 36 | 1.3367 | 1.1823 | 1.0656 | yes |
| WLD/USDT | P20_200 | 94 | 1.3171 | 1.1761 | 1.1725 | yes |
| ZRO/USDT | P50_55 | 38 | 1.2964 | 0.9794 | 0.9651 | no |
| ENA/USDT | P8_12 | 66 | 1.2792 | 0.9252 | 1.1329 | no |

## Leg 4 — the walk-forward selection, parent vs child

The full sample of every symbol is cut into 5 sequential folds. At step k the best cell of the symbol is chosen on the history and scored on fold k+1, which the selection never saw. This is the comparison that matters: it scores the *procedure*, not a cell that was picked because it looked good.

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Walk-forward steps scored | 228 | 228 | 0 |
| Out-of-fold trades | 19956 | 10843 | -9113 |
| Pooled out-of-fold net PF | 0.6186 | 0.7509 | 0.1323 |
| Pooled out-of-fold net PF (2x costs) | 0.4177 | 0.5705 | 0.1529 |
| Out-of-fold windows with net PF > 1 | 13 | 37 | 24 |
| Share of out-of-fold windows with net PF > 1 | 5.7% | 16.2% | +10.5 pp |
| Median in-fold net PF of the selected cell | 0.8090 | 1.1023 | 0.2934 |
| Median out-of-fold net PF of the selected cell | 0.5942 | 0.7502 | 0.1561 |

| Selection against the grid's own null | Parent | Child |
|---|---|---|
| Median percentile of the selected cells | 0.7713 | 0.5249 |
| Selected cells above the null p95 | 41 of 227 | 16 of 227 |
| One-sided exact binomial p-value | 0.0000 | 0.1068 |

## Leg 5 — reproducibility of the child cells

| Symbol | Cell | Max absolute difference vs the stored summary |
|---|---|---|
| BTC/USDT | P8_12 | 0.00e+00 |
| NEAR/USDT | P8_12 | 0.00e+00 |
| CRO/USDT | P8_12 | 0.00e+00 |
| HTX/USDT | P8_12 | 0.00e+00 |
| INJ/USDT | P8_12 | 0.00e+00 |

A child cell re-run through the real backtest reproduces the stored summary exactly, so the child run is the engine the baseline run used, with the mutation applied.

## Verdict

- The child grid trades 1349555 trades against the parent's 3097113 on the same 57 symbols (-56.4 %), and the pooled net profit factor moves from 0.4864 to 0.7498.
- The cost of a trade falls from 8.97 to 11.23, and the costs as a share of the gross profit move from 67.8% to 28.9%: the ATR minimum-risk filter buys back cost drag by trading less, not by trading better.
- Out of sample the child's pooled net PF is 0.7041 against the parent's 0.5207, and the cells that clear the full §3.4 gate are 19 against 0.
- The walk-forward leg, which scores the *procedure* and never shows the selection the data it is judged on, moves the pooled out-of-fold net PF from 0.6186 to 0.7509 (2x costs: 0.4177 -> 0.5705).
- The yardstick is the parent's walk-forward pooled out-of-fold net PF over the full 266 symbols: 0.6409 (0.4521 under 2x costs). The child has to beat that number on its own symbol set to be worth anything.
- The mutation improves the walk-forward number, but the improvement is a cost effect (fewer, wider trades) and not a new edge.
- 19 child cells clear the PROMPT.md §3.4 gate (19 of 3762 cells on 6 symbols: ENA/USDT 5, POL/USDT 5, APT/USDT 5, WLD/USDT 2, RENDER/USDT 1). A cell that clears the gate is a selection result, not a promotion: the child grid's own null puts 12.1% of its folds above PF 1 with a median PF of 0.7274, and the walk-forward selection ranks at the 0.5249 percentile of that null (one-sided binomial p 0.1068). The gate-clearing cells have to survive the child's own null leg, the walk-forward and the sub-period leg before any of them can be promoted; until then the baseline grid stays the program's grid.

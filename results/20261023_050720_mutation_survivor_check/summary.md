# Mutation Survivor Check — the gate-clearing cells of the child grid

**Child run:** `results/20261022_134500_grid`
**Generated:** 2026-10-23T05:10:02.522809+00:00
**Cells read:** 18150 on 275 symbols
**Gate:** OOS net PF > 1, OOS net PF under 2x costs > 1, >= 30 OOS trades

## Leg 1 — the family

| Measure | Value |
|---|---|
| Cells read | 18150 |
| Cells clearing the gate | 10 |
| Symbols with a gate-clearing cell | 4 |
| Gate cells per symbol | {'DEXE/USDT': 6, 'GRT/USDT': 2, 'BRETT/USDT': 1, 'MERL/USDT': 1} |
| Pooled OOS net PF of the family | 1.3353 |
| Pooled OOS trades of the family | 678 |
| Child cells with OOS net PF > 1 | 77 (0.4 %) |
| Child cells clearing the gate | 10 (0.06 %) |

### The gate-clearing cells

| Symbol | Cell | OOS trades | OOS net PF | OOS net PF (2x costs) | Full-sample net PF | Sub-periods with PF > 1 |
|---|---|---|---|---|---|---|
| GRT/USDT | P8_200 | 64 | 1.3136 | 1.0548 | 0.7535 | 3/4 |
| GRT/USDT | P20_200 | 61 | 1.4547 | 1.2401 | 0.9087 | 3/4 |
| DEXE/USDT | P12_200 | 79 | 1.2103 | 1.0325 | 0.8169 | 1/3 |
| DEXE/USDT | P20_200 | 77 | 1.4790 | 1.2967 | 0.7855 | 1/3 |
| DEXE/USDT | P21_200 | 75 | 1.4985 | 1.3136 | 0.8209 | 1/3 |
| DEXE/USDT | P26_200 | 73 | 1.1484 | 1.0066 | 0.8041 | 1/3 |
| DEXE/USDT | P50_200 | 86 | 1.3565 | 1.1165 | 0.8058 | 2/3 |
| DEXE/USDT | P55_200 | 81 | 1.3378 | 1.0789 | 0.7535 | 2/3 |
| BRETT/USDT | P8_200 | 51 | 1.3107 | 1.0111 | 0.8337 | 3/4 |
| MERL/USDT | P8_200 | 31 | 1.2518 | 1.0215 | 0.8224 | 1/1 |

## Leg 2 — concentration

The pooled out-of-sample profit factor of the family with each symbol dropped in turn: a family that stands on one symbol is not a family.

| Dropped symbol | Cells left | Gate cells left | Pooled OOS net PF |
|---|---|---|---|
| BRETT/USDT | 9 | 9 | 1.3377 |
| DEXE/USDT | 4 | 4 | 1.3463 |
| GRT/USDT | 8 | 8 | 1.3230 |
| MERL/USDT | 9 | 9 | 1.3397 |

## Leg 3 — sub-period stability

The out-of-sample window of every gate-clearing cell is cut into 4 sequential sub-periods.

**1 of 10** gate-clearing cells keep a net PF above 1 in every sub-period that carries trades.

| Symbol | Cell | Sub-periods with PF > 1 | Sub-periods with trades | Stable |
|---|---|---|---|---|
| GRT/USDT | P8_200 | 3 | 4 | no |
| GRT/USDT | P20_200 | 3 | 4 | no |
| DEXE/USDT | P12_200 | 1 | 3 | no |
| DEXE/USDT | P20_200 | 1 | 3 | no |
| DEXE/USDT | P21_200 | 1 | 3 | no |
| DEXE/USDT | P26_200 | 1 | 3 | no |
| DEXE/USDT | P50_200 | 2 | 3 | no |
| DEXE/USDT | P55_200 | 2 | 3 | no |
| BRETT/USDT | P8_200 | 3 | 4 | no |
| MERL/USDT | P8_200 | 1 | 1 | yes |
## Verdict

- 10 of 18150 child cells clear the §3.4 gate, on 4 symbols: {'DEXE/USDT': 6, 'GRT/USDT': 2, 'BRETT/USDT': 1, 'MERL/USDT': 1}.
- The family pools to an out-of-sample net PF of 1.3353 over 678 out-of-sample trades, and the child's own cells put 0.4 % of their out-of-sample scores above PF 1.
- 1 of 10 gate-clearing cells keep a net PF above 1 in every out-of-sample sub-period that carries trades (MERL/USDT P8_200); the other 9 work in one stretch of time only.
- A cell that clears a gate is a selection result, not a promotion: the family still has to beat its own randomizations (the null leg on the child grid) and the walk-forward has to hold up on the complete child grid before anything can be promoted.

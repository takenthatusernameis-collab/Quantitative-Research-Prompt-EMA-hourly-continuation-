# Mutation Survivor Check — the gate-clearing cells of the child grid

**Child run:** `results/20261021_172619_grid`
**Generated:** 2026-10-21T19:45:02.794634+00:00
**Cells read:** 4026 on 61 symbols
**Gate:** OOS net PF > 1, OOS net PF under 2x costs > 1, >= 30 OOS trades

## Leg 1 — the family

| Measure | Value |
|---|---|
| Cells read | 4026 |
| Cells clearing the gate | 20 |
| Symbols with a gate-clearing cell | 7 |
| Gate cells per symbol | {'ENA/USDT': 5, 'POL/USDT': 5, 'APT/USDT': 5, 'WLD/USDT': 2, 'RENDER/USDT': 1, 'AERO/USDT': 1, 'PYTH/USDT': 1} |
| Pooled OOS net PF of the family | 1.2606 |
| Pooled OOS trades of the family | 1633 |
| Child cells with OOS net PF > 1 | 180 (4.5 %) |
| Child cells clearing the gate | 20 (0.50 %) |

### The gate-clearing cells

| Symbol | Cell | OOS trades | OOS net PF | OOS net PF (2x costs) | Full-sample net PF | Sub-periods with PF > 1 |
|---|---|---|---|---|---|---|
| ENA/USDT | P8_144 | 123 | 1.2020 | 1.0456 | 1.0576 | 3/4 |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.0315 | 1.3253 | 3/4 |
| ENA/USDT | P20_200 | 106 | 1.2024 | 1.0479 | 0.9190 | 3/4 |
| ENA/USDT | P21_200 | 101 | 1.1506 | 1.0041 | 0.8941 | 3/4 |
| ENA/USDT | P34_144 | 111 | 1.2519 | 1.0555 | 0.9014 | 2/4 |
| WLD/USDT | P20_200 | 94 | 1.3171 | 1.1761 | 1.1725 | 3/4 |
| WLD/USDT | P21_200 | 103 | 1.2454 | 1.1119 | 1.0863 | 2/4 |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.3857 | 1.1216 | 4/4 |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.1617 | 1.0429 | 3/4 |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.2155 | 1.0354 | 4/4 |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.1647 | 0.9932 | 3/4 |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.1151 | 1.0278 | 4/4 |
| RENDER/USDT | P8_200 | 45 | 1.1898 | 1.0722 | 0.9713 | 3/4 |
| AERO/USDT | P12_200 | 79 | 1.1392 | 1.0084 | 1.1454 | 2/4 |
| APT/USDT | P12_144 | 86 | 1.1429 | 1.0090 | 0.9400 | 3/4 |
| APT/USDT | P12_200 | 36 | 1.3367 | 1.1823 | 1.0656 | 2/3 |
| APT/USDT | P20_144 | 90 | 1.2129 | 1.0507 | 0.9912 | 3/4 |
| APT/USDT | P21_144 | 93 | 1.2226 | 1.0567 | 1.0362 | 3/4 |
| APT/USDT | P26_200 | 80 | 1.2029 | 1.0384 | 1.0097 | 3/4 |
| PYTH/USDT | P8_200 | 82 | 1.1827 | 1.0553 | 1.0817 | 2/4 |

## Leg 2 — concentration

The pooled out-of-sample profit factor of the family with each symbol dropped in turn: a family that stands on one symbol is not a family.

| Dropped symbol | Cells left | Gate cells left | Pooled OOS net PF |
|---|---|---|---|
| AERO/USDT | 19 | 19 | 1.2688 |
| APT/USDT | 15 | 15 | 1.2765 |
| ENA/USDT | 15 | 15 | 1.2756 |
| POL/USDT | 15 | 15 | 1.2177 |
| PYTH/USDT | 19 | 19 | 1.2650 |
| RENDER/USDT | 19 | 19 | 1.2627 |
| WLD/USDT | 18 | 18 | 1.2577 |

## Leg 3 — sub-period stability

The out-of-sample window of every gate-clearing cell is cut into 4 sequential sub-periods.

**3 of 20** gate-clearing cells keep a net PF above 1 in every sub-period that carries trades.

| Symbol | Cell | Sub-periods with PF > 1 | Sub-periods with trades | Stable |
|---|---|---|---|---|
| ENA/USDT | P8_144 | 3 | 4 | no |
| ENA/USDT | P20_21 | 3 | 4 | no |
| ENA/USDT | P20_200 | 3 | 4 | no |
| ENA/USDT | P21_200 | 3 | 4 | no |
| ENA/USDT | P34_144 | 2 | 4 | no |
| WLD/USDT | P20_200 | 3 | 4 | no |
| WLD/USDT | P21_200 | 2 | 4 | no |
| POL/USDT | P8_200 | 4 | 4 | yes |
| POL/USDT | P20_200 | 3 | 4 | no |
| POL/USDT | P21_200 | 4 | 4 | yes |
| POL/USDT | P26_200 | 3 | 4 | no |
| POL/USDT | P34_200 | 4 | 4 | yes |
| RENDER/USDT | P8_200 | 3 | 4 | no |
| AERO/USDT | P12_200 | 2 | 4 | no |
| APT/USDT | P12_144 | 3 | 4 | no |
| APT/USDT | P12_200 | 2 | 3 | no |
| APT/USDT | P20_144 | 3 | 4 | no |
| APT/USDT | P21_144 | 3 | 4 | no |
| APT/USDT | P26_200 | 3 | 4 | no |
| PYTH/USDT | P8_200 | 2 | 4 | no |
## Verdict

- 20 of 4026 child cells clear the §3.4 gate, on 7 symbols: {'ENA/USDT': 5, 'POL/USDT': 5, 'APT/USDT': 5, 'WLD/USDT': 2, 'RENDER/USDT': 1, 'AERO/USDT': 1, 'PYTH/USDT': 1}.
- The family pools to an out-of-sample net PF of 1.2606 over 1633 out-of-sample trades, and the child's own cells put 4.5 % of their out-of-sample scores above PF 1.
- 3 of 20 gate-clearing cells keep a net PF above 1 in every out-of-sample sub-period that carries trades (POL/USDT P8_200, POL/USDT P21_200, POL/USDT P34_200); the other 17 work in one stretch of time only.
- A cell that clears a gate is a selection result, not a promotion: the family still has to beat its own randomizations (the null leg on the child grid) and the walk-forward has to hold up on the complete child grid before anything can be promoted.

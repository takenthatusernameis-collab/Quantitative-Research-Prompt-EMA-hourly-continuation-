# Mutation Reproduction Check

**Parent run:** `results/20261019_135940_grid`
**Child run:** `results/20261021_172619_grid`
**Generated:** 2026-10-22T00:31:51.444419+00:00
**Cells re-run:** 24

## Leg 1 - the artifacts are re-runnable

Every sampled cell is re-run through the real backtest on the same fixture and compared with the stored blotter and the stored summary, trade by trade.

| Symbol | Cell | Child reproduces | Parent reproduces | Child max metric delta | Parent max metric delta |
|---|---|---|---|---|---|
| BTC/USDT | P8_12 | yes | yes | 0.000e+00 | 0.000e+00 |
| NEAR/USDT | P8_20 | yes | yes | 0.000e+00 | 0.000e+00 |
| CRO/USDT | P8_21 | yes | yes | 0.000e+00 | 0.000e+00 |
| HTX/USDT | P8_26 | yes | yes | 0.000e+00 | 0.000e+00 |
| INJ/USDT | P8_34 | yes | yes | 0.000e+00 | 0.000e+00 |
| BDX/USDT | P8_50 | yes | yes | 0.000e+00 | 0.000e+00 |
| BTT/USDT | P8_55 | yes | yes | 0.000e+00 | 0.000e+00 |
| AR/USDT | P8_89 | yes | yes | 0.000e+00 | 0.000e+00 |
| ZBCN/USDT | P8_100 | yes | yes | 0.000e+00 | 0.000e+00 |
| ZK/USDT | P8_144 | yes | yes | 0.000e+00 | 0.000e+00 |
| RSR/USDT | P8_200 | yes | yes | 0.000e+00 | 0.000e+00 |
| GMX/USDT | P12_20 | yes | yes | 0.000e+00 | 0.000e+00 |
| KAVA/USDT | P12_21 | yes | yes | 0.000e+00 | 0.000e+00 |
| SUSHI/USDT | P12_26 | yes | yes | 0.000e+00 | 0.000e+00 |
| ASTR/USDT | P12_34 | yes | yes | 0.000e+00 | 0.000e+00 |
| CFG/USDT | P12_50 | yes | yes | 0.000e+00 | 0.000e+00 |
| BOME/USDT | P12_55 | yes | yes | 0.000e+00 | 0.000e+00 |
| OSMO/USDT | P12_89 | yes | yes | 0.000e+00 | 0.000e+00 |
| REZ/USDT | P12_100 | yes | yes | 0.000e+00 | 0.000e+00 |
| IOST/USDT | P12_144 | yes | yes | 0.000e+00 | 0.000e+00 |
| ERG/USDT | P12_200 | yes | yes | 0.000e+00 | 0.000e+00 |
| SQD/USDT | P20_21 | yes | yes | 0.000e+00 | 0.000e+00 |
| ONE/USDT | P20_26 | yes | yes | 0.000e+00 | 0.000e+00 |
| FIDA/USDT | P20_34 | yes | yes | 0.000e+00 | 0.000e+00 |

## Leg 2 - how the two paths differ

The ATR minimum-risk filter skips an entry, so the position state, the equity path and the size of every later trade change with it. The child is therefore a different path, not a subset of the parent's trades.

| Symbol | Cell | Parent trades | Child trades | Shared entry bars | Parent-only bars | Child-only bars | First divergence |
|---|---|---|---|---|---|---|---|
| BTC/USDT | P8_12 | 2075 | 237 | 213 | 1862 | 24 | 21 |
| NEAR/USDT | P8_20 | 1729 | 432 | 397 | 1332 | 35 | 30 |
| CRO/USDT | P8_21 | 1701 | 548 | 499 | 1202 | 49 | 53 |
| HTX/USDT | P8_26 | 1643 | 696 | 632 | 1011 | 64 | 59 |
| INJ/USDT | P8_34 | 1379 | 680 | 653 | 726 | 27 | 34 |
| BDX/USDT | P8_50 | 1720 | 557 | 510 | 1210 | 47 | 65 |
| BTT/USDT | P8_55 | 926 | 580 | 564 | 362 | 16 | 84 |
| AR/USDT | P8_89 | 624 | 446 | 432 | 192 | 14 | 614 |
| ZBCN/USDT | P8_100 | 871 | 549 | 536 | 335 | 13 | 114 |
| ZK/USDT | P8_144 | 574 | 439 | 428 | 146 | 11 | 470 |
| RSR/USDT | P8_200 | 288 | 228 | 222 | 66 | 6 | 293 |
| GMX/USDT | P12_20 | 1384 | 501 | 455 | 929 | 46 | 21 |
| KAVA/USDT | P12_21 | 1500 | 456 | 416 | 1084 | 40 | 22 |
| SUSHI/USDT | P12_26 | 1423 | 504 | 470 | 953 | 34 | 66 |
| ASTR/USDT | P12_34 | 1177 | 708 | 679 | 498 | 29 | 65 |
| CFG/USDT | P12_50 | 870 | 490 | 464 | 406 | 26 | 69 |
| BOME/USDT | P12_55 | 1032 | 619 | 601 | 431 | 18 | 126 |
| OSMO/USDT | P12_89 | 740 | 553 | 528 | 212 | 25 | 496 |
| REZ/USDT | P12_100 | 590 | 451 | 438 | 152 | 13 | 133 |
| IOST/USDT | P12_144 | 439 | 355 | 348 | 91 | 7 | 476 |
| ERG/USDT | P12_200 | 524 | 375 | 363 | 161 | 12 | 288 |
| SQD/USDT | P20_21 | 1128 | 187 | 176 | 952 | 11 | 23 |
| ONE/USDT | P20_26 | 1262 | 189 | 180 | 1082 | 9 | 112 |
| FIDA/USDT | P20_34 | 1105 | 492 | 473 | 632 | 19 | 95 |

## Verdict

- 24/24 re-run child cells reproduce the stored child blotter and summary exactly, and 24/24 re-run parent cells reproduce the stored parent artifacts: both grids are artifacts of the same engine.
- The mutation removes 667.8 of the parent's entry bars on average and adds 24.8 entries the parent never took: the ATR minimum-risk filter does not prune the parent's trade list, it changes the path, so the child is a different strategy instance and not a filtered view of the parent.
- No violation found: the child run is a faithful re-run of the parent engine with the ATR minimum-risk filter applied.

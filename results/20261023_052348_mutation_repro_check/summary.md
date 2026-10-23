# Mutation Reproduction Check

**Parent run:** `results/20261019_135940_grid`
**Child run:** `results/20261022_134500_grid`
**Generated:** 2026-10-23T05:28:30.879550+00:00
**Cells re-run:** 16

## Leg 1 - the artifacts are re-runnable

Every sampled cell is re-run through the real backtest on the same fixture and compared with the stored blotter and the stored summary, trade by trade.

| Symbol | Cell | Child reproduces | Parent reproduces | Child max metric delta | Parent max metric delta |
|---|---|---|---|---|---|
| BTC/USDT | P8_12 | yes | yes | 0.000e+00 | 0.000e+00 |
| SUI/USDT | P8_20 | yes | yes | 0.000e+00 | 0.000e+00 |
| ARB/USDT | P8_21 | yes | yes | 0.000e+00 | 0.000e+00 |
| ETHFI/USDT | P8_26 | yes | yes | 0.000e+00 | 0.000e+00 |
| LDO/USDT | P8_34 | yes | yes | 0.000e+00 | 0.000e+00 |
| COMP/USDT | P8_50 | yes | yes | 0.000e+00 | 0.000e+00 |
| APE/USDT | P8_55 | yes | yes | 0.000e+00 | 0.000e+00 |
| ZRX/USDT | P8_89 | yes | yes | 0.000e+00 | 0.000e+00 |
| VELO/USDT | P8_100 | yes | yes | 0.000e+00 | 0.000e+00 |
| ONT/USDT | P8_144 | yes | yes | 0.000e+00 | 0.000e+00 |
| POPCAT/USDT | P8_200 | yes | yes | 0.000e+00 | 0.000e+00 |
| OSMO/USDT | P12_20 | yes | yes | 0.000e+00 | 0.000e+00 |
| LUNA/USDT | P12_21 | yes | yes | 0.000e+00 | 0.000e+00 |
| NYM/USDT | P12_26 | yes | yes | 0.000e+00 | 0.000e+00 |
| OGN/USDT | P12_34 | yes | yes | 0.000e+00 | 0.000e+00 |
| QI/USDT | P12_50 | yes | yes | 0.000e+00 | 0.000e+00 |

## Leg 2 - how the two paths differ

The ATR minimum-risk filter skips an entry, so the position state, the equity path and the size of every later trade change with it. The child is therefore a different path, not a subset of the parent's trades.

| Symbol | Cell | Parent trades | Child trades | Shared entry bars | Parent-only bars | Child-only bars | First divergence |
|---|---|---|---|---|---|---|---|
| BTC/USDT | P8_12 | 2075 | 2075 | 2075 | 0 | 0 | None |
| SUI/USDT | P8_20 | 1743 | 1743 | 1743 | 0 | 0 | None |
| ARB/USDT | P8_21 | 1678 | 1678 | 1678 | 0 | 0 | None |
| ETHFI/USDT | P8_26 | 1603 | 1603 | 1603 | 0 | 0 | None |
| LDO/USDT | P8_34 | 1452 | 1452 | 1452 | 0 | 0 | None |
| COMP/USDT | P8_50 | 1127 | 1127 | 1127 | 0 | 0 | None |
| APE/USDT | P8_55 | 1078 | 1078 | 1078 | 0 | 0 | None |
| ZRX/USDT | P8_89 | 676 | 676 | 676 | 0 | 0 | None |
| VELO/USDT | P8_100 | 797 | 797 | 797 | 0 | 0 | None |
| ONT/USDT | P8_144 | 588 | 588 | 588 | 0 | 0 | None |
| POPCAT/USDT | P8_200 | 340 | 340 | 340 | 0 | 0 | None |
| OSMO/USDT | P12_20 | 1477 | 1477 | 1477 | 0 | 0 | None |
| LUNA/USDT | P12_21 | 1599 | 1599 | 1599 | 0 | 0 | None |
| NYM/USDT | P12_26 | 1267 | 1267 | 1267 | 0 | 0 | None |
| OGN/USDT | P12_34 | 1203 | 1203 | 1203 | 0 | 0 | None |
| QI/USDT | P12_50 | 968 | 968 | 968 | 0 | 0 | None |

## Verdict

- 16/16 re-run child cells reproduce the stored child blotter and summary exactly, and 16/16 re-run parent cells reproduce the stored parent artifacts: both grids are artifacts of the same engine.
- The mutation removes 0.0 of the parent's entry bars on average and adds 0.0 entries the parent never took: the ATR minimum-risk filter does not prune the parent's trade list, it changes the path, so the child is a different strategy instance and not a filtered view of the parent.
- No violation found: the child run is a faithful re-run of the parent engine with the ATR minimum-risk filter applied.

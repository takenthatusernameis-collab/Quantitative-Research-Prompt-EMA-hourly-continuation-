# Mutation Reproduction Check

**Parent run:** `results/20261019_135940_grid`
**Child run:** `results/20261021_172619_grid`
**Generated:** 2026-10-21T19:32:56.603827+00:00
**Cells re-run:** 12

## Leg 1 - the artifacts are re-runnable

Every sampled cell is re-run through the real backtest on the same fixture and compared with the stored blotter and the stored summary, trade by trade.

| Symbol | Cell | Child reproduces | Parent reproduces | Child max metric delta | Parent max metric delta |
|---|---|---|---|---|---|
| BTC/USDT | P8_12 | yes | yes | 0.000e+00 | 0.000e+00 |
| XRP/USDT | P8_20 | yes | yes | 0.000e+00 | 0.000e+00 |
| XMR/USDT | P8_21 | yes | yes | 0.000e+00 | 0.000e+00 |
| XLM/USDT | P8_26 | yes | yes | 0.000e+00 | 0.000e+00 |
| AVAX/USDT | P8_34 | yes | yes | 0.000e+00 | 0.000e+00 |
| TAO/USDT | P8_50 | yes | yes | 0.000e+00 | 0.000e+00 |
| ENA/USDT | P8_55 | yes | yes | 0.000e+00 | 0.000e+00 |
| WLD/USDT | P8_89 | yes | yes | 0.000e+00 | 0.000e+00 |
| ICP/USDT | P8_100 | yes | yes | 0.000e+00 | 0.000e+00 |
| JST/USDT | P8_144 | yes | yes | 0.000e+00 | 0.000e+00 |
| KAS/USDT | P8_200 | yes | yes | 0.000e+00 | 0.000e+00 |
| INJ/USDT | P12_20 | yes | yes | 0.000e+00 | 0.000e+00 |

## Leg 2 - how the two paths differ

The ATR minimum-risk filter skips an entry, so the position state, the equity path and the size of every later trade change with it. The child is therefore a different path, not a subset of the parent's trades.

| Symbol | Cell | Parent trades | Child trades | Shared entry bars | Parent-only bars | Child-only bars | First divergence |
|---|---|---|---|---|---|---|---|
| BTC/USDT | P8_12 | 2075 | 237 | 213 | 1862 | 24 | 21 |
| XRP/USDT | P8_20 | 1677 | 397 | 368 | 1309 | 29 | 53 |
| XMR/USDT | P8_21 | 1973 | 331 | 296 | 1677 | 35 | 35 |
| XLM/USDT | P8_26 | 1640 | 622 | 573 | 1067 | 49 | 40 |
| AVAX/USDT | P8_34 | 1383 | 689 | 667 | 716 | 22 | 45 |
| TAO/USDT | P8_50 | 1124 | 648 | 632 | 492 | 16 | 197 |
| ENA/USDT | P8_55 | 997 | 628 | 608 | 389 | 20 | 97 |
| WLD/USDT | P8_89 | 702 | 482 | 474 | 228 | 8 | 98 |
| ICP/USDT | P8_100 | 644 | 471 | 453 | 191 | 18 | 294 |
| JST/USDT | P8_144 | 434 | 353 | 348 | 86 | 5 | 2938 |
| KAS/USDT | P8_200 | 438 | 316 | 304 | 134 | 12 | 235 |
| INJ/USDT | P12_20 | 1530 | 241 | 222 | 1308 | 19 | 25 |

## Verdict

- 12/12 re-run child cells reproduce the stored child blotter and summary exactly, and 12/12 re-run parent cells reproduce the stored parent artifacts: both grids are artifacts of the same engine.
- The mutation removes 788.2 of the parent's entry bars on average and adds 21.4 entries the parent never took: the ATR minimum-risk filter does not prune the parent's trade list, it changes the path, so the child is a different strategy instance and not a filtered view of the parent.
- No violation found: the child run is a faithful re-run of the parent engine with the ATR minimum-risk filter applied.

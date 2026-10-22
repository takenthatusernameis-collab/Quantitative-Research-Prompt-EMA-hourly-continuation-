# Randomized-Entry Null — EMA Hourly Continuation Grid

**Source run:** `results/20261021_172619_grid`
**Generated:** 2026-10-22T02:55:59.025844+00:00
**Universe:** 266 symbols, 17556 grid cells
**Out-of-sample window:** trailing 35% of each symbol's bars, entries restricted to the window
**Cost stress:** 2x fees and slippage

## What the leg asks

How many of the 17 556 cells would clear the out-of-sample gates if the entry rule carried no information? The null keeps the market path, the EMA geometry, the risk distances and the cost model, and destroys only the part of the rule under test:

- **block** - the same number of entries, with the same direction mix, moved to random bars inside their own 240-bar block. The entry stops being a cross but stays in the same stretch of the market, so the risk distance and the cost drag stay comparable.
- **timing** - the same number of entries, at uniformly random bars over the out-of-sample window, with the same multiset of directions.
- **sign** - the same entry bars, with every direction redrawn from a fair coin.

Both are run through the untouched backtest engine, so the null is produced by the same code that produced the real numbers. The null is matched to the rule inside the window: the entries the rule fires on inside the window are the entries the null randomizes, so both sides are scored on the same sample.

## Leg 0 — The harness reproduces the grid run

| Check | Result |
|---|---|
| Cells re-run on the full history | 24 |
| Recomputed full-sample net PF equals the stored grid summary | 24 of 24 |
| Windowed run equals the full-history in-window trades | 17 of 24 |
| Vectorized signal generator equals the reference generator | 24 of 24 |

## Leg 1 — The null grid

| Statistic | Real rule | timing null | block null | sign null |
|---|---|---|---|---|
| mean out-of-sample net PF | 0.6603 | 0.7786 | 0.8808 | 0.7072 |
| median out-of-sample net PF | 0.6589 | 0.7640 | 0.8572 | 0.6979 |
| p95 out-of-sample net PF | 0.9563 | 1.0766 | 1.2583 | 0.9866 |
| max out-of-sample net PF | 1.9504 | 2.5310 | 4.0500 | 1.7989 |

| Gate (out-of-sample leg) | Real rule | timing null | block null | sign null |
|---|---|---|---|---|
| Cells with out-of-sample net PF > 1 | 613 | 1611 | 4286 | 773 |
| Cells clearing the §3.4 out-of-sample gate | 103 | 329 | 1195 | 68 |
| Pooled out-of-sample net PF | 0.6502 | 0.7606 | 0.8510 | 0.7009 |
| Cells with gross out-of-sample PF > 1 | 5458 | 8071 | 12498 | 7914 |
| Median gross out-of-sample net PF | 0.9158 | 0.9850 | 1.1042 | 0.9798 |
| Median out-of-sample trades per cell | 141.0000 | 142.0000 | 141.0000 | 141.0000 |
| Median risk distance (share of entry price) | 1.7251% | 2.6356% | 2.5847% | 1.7251% |

Gate: out-of-sample net PF > 1, out-of-sample Sharpe > 0, at least min_trades out-of-sample trades, and out-of-sample net PF still > 1 under the cost stress.

## Leg 2 — The observed tail against the null tail

| Statistic | Real rule | timing null | block null | sign null |
|---|------|---|---|
| Best cell of the grid | 1.9504 | 2.5310 | 4.0500 | 1.7989 |
| Null cells at or above the real best | - | 5 | 19 | 0 |
| Family-wise probability of a null cell reaching the real best | - | 1 - 6.73e-03 | 1 - 5.55e-09 | 0.00e+00 |
| Cells where the real rule beats its own null | - | 4521 | 2081 | 6707 |
| Cells where the null beats the real rule | - | 13035 | 15475 | 10849 |
| Two-sided sign test on that comparison | - | 0.00e+00 | 0.00e+00 | 1.97e-216 |
| Same comparison on the gross profit factor (no cost drag) | - | 6502 | 3419 | 6664 |
| Two-sided sign test on the gross comparison | - | 1.73e-261 | 0.00e+00 | 1.62e-225 |

A sign test p-value this small means the two sides of the comparison are not exchangeable. The direction is the point: the counts above say which side of the comparison the rule is on.

## Leg 3 — The surviving cells against their own randomizations

Each cell is re-randomized many times. The p-value is the share of randomizations that reach the observed out-of-sample net PF, corrected for the number of cells the program tested (Bonferroni over 17556 cells). The control cells are ordinary cells that did not survive the audit; they show what the same test does on a cell with no reason to look good.

| Symbol | Cell | Group | OOS PF | Null mean PF | Null max PF | p-value | p x grid | Null gate pass rate |
|---|---|---|---|---|---|---|---|---|
| AERO/USDT | P12_200 | survivor | 1.1491 | 0.8772 | 1.2197 | 0.1429 | 1.0000 | 10.0% |
| APT/USDT | P12_144 | survivor | 1.1583 | 0.9701 | 1.6346 | 0.2857 | 1.0000 | 25.0% |
| APT/USDT | P12_200 | survivor | 1.4628 | 1.0027 | 1.7190 | 0.1429 | 1.0000 | 15.0% |
| APT/USDT | P20_144 | survivor | 1.2432 | 0.9192 | 1.5063 | 0.1429 | 1.0000 | 10.0% |
| APT/USDT | P21_144 | survivor | 1.2517 | 0.8859 | 1.3112 | 0.0952 | 1.0000 | 10.0% |
| APT/USDT | P26_200 | survivor | 1.2284 | 0.9577 | 1.6004 | 0.2857 | 1.0000 | 25.0% |
| AVA/USDT | P20_200 | survivor | 1.2322 | 0.8564 | 1.2631 | 0.0952 | 1.0000 | 5.0% |
| AVA/USDT | P21_200 | survivor | 1.2320 | 0.8127 | 1.3937 | 0.0952 | 1.0000 | 5.0% |
| AVA/USDT | P26_200 | survivor | 1.2614 | 0.8872 | 1.2493 | 0.0476 | 1.0000 | 10.0% |
| AVA/USDT | P34_200 | survivor | 1.3090 | 0.9718 | 1.6132 | 0.2381 | 1.0000 | 30.0% |
| AVA/USDT | P50_200 | survivor | 1.3796 | 0.8325 | 1.2065 | 0.0476 | 1.0000 | 5.0% |
| BOME/USDT | P26_200 | survivor | 1.2403 | 0.7999 | 1.0370 | 0.0476 | 1.0000 | 0.0% |
| BLUR/USDT | P12_144 | survivor | 1.3406 | 0.8284 | 1.1763 | 0.0476 | 1.0000 | 0.0% |
| BLUR/USDT | P12_200 | survivor | 1.3084 | 0.9325 | 1.4906 | 0.0952 | 1.0000 | 5.0% |
| BLUR/USDT | P21_200 | survivor | 1.2169 | 0.8852 | 1.2867 | 0.0952 | 1.0000 | 10.0% |
| BLUR/USDT | P8_144 | survivor | 1.2691 | 0.8822 | 1.1778 | 0.0476 | 1.0000 | 0.0% |
| BLUR/USDT | P8_200 | survivor | 1.3389 | 0.8687 | 1.2289 | 0.0476 | 1.0000 | 5.0% |
| BRETT/USDT | P8_144 | survivor | 1.1474 | 0.9310 | 1.4013 | 0.1429 | 1.0000 | 10.0% |
| BRETT/USDT | P8_200 | survivor | 1.4071 | 1.0124 | 1.5102 | 0.1429 | 1.0000 | 20.0% |
| CETUS/USDT | P12_200 | survivor | 1.2746 | 0.8365 | 1.3047 | 0.0952 | 1.0000 | 5.0% |
| CETUS/USDT | P8_200 | survivor | 1.4565 | 0.7806 | 1.1054 | 0.0476 | 1.0000 | 5.0% |
| DAG/USDT | P8_100 | survivor | 1.3172 | 0.8440 | 1.1332 | 0.0476 | 1.0000 | 0.0% |
| CHZ/USDT | P8_200 | survivor | 1.1120 | 0.9168 | 1.3833 | 0.2381 | 1.0000 | 20.0% |
| COTI/USDT | P50_144 | survivor | 1.2656 | 0.8795 | 1.1789 | 0.0476 | 1.0000 | 5.0% |
| COTI/USDT | P50_200 | survivor | 1.3026 | 0.9589 | 1.2148 | 0.0476 | 1.0000 | 10.0% |
| COTI/USDT | P55_144 | survivor | 1.2911 | 0.8497 | 1.3743 | 0.0952 | 1.0000 | 10.0% |
| EGLD/USDT | P55_200 | survivor | 1.3233 | 0.8950 | 1.5979 | 0.0952 | 1.0000 | 5.0% |
| DIA/USDT | P12_200 | survivor | 1.5027 | 0.9266 | 1.2552 | 0.0476 | 1.0000 | 5.0% |
| DIA/USDT | P20_200 | survivor | 1.3063 | 0.8271 | 1.2223 | 0.0476 | 1.0000 | 5.0% |
| DIA/USDT | P21_200 | survivor | 1.3177 | 0.8957 | 1.6714 | 0.0952 | 1.0000 | 10.0% |
| DIA/USDT | P26_200 | survivor | 1.2581 | 0.9218 | 1.3792 | 0.1429 | 1.0000 | 10.0% |
| DIA/USDT | P8_200 | survivor | 1.2940 | 0.9175 | 1.2434 | 0.0476 | 1.0000 | 10.0% |
| ENA/USDT | P20_200 | survivor | 1.2024 | 0.8897 | 1.2205 | 0.0952 | 1.0000 | 5.0% |
| ENA/USDT | P20_21 | survivor | 1.3902 | 0.7564 | 0.9985 | 0.0476 | 1.0000 | 0.0% |
| ENA/USDT | P21_200 | survivor | 1.1506 | 0.9507 | 1.4509 | 0.2381 | 1.0000 | 20.0% |
| ENA/USDT | P34_144 | survivor | 1.2519 | 0.9343 | 1.3845 | 0.2381 | 1.0000 | 30.0% |
| ENA/USDT | P8_144 | survivor | 1.2020 | 0.9568 | 1.1621 | 0.0476 | 1.0000 | 10.0% |
| FLUX/USDT | P8_200 | survivor | 1.2695 | 0.8168 | 1.1797 | 0.0476 | 1.0000 | 5.0% |
| FET/USDT | P12_200 | survivor | 1.5616 | 1.0111 | 1.6677 | 0.1429 | 1.0000 | 30.0% |
| FET/USDT | P20_200 | survivor | 1.2336 | 0.9261 | 1.6867 | 0.1905 | 1.0000 | 20.0% |
| FET/USDT | P21_200 | survivor | 1.1274 | 0.9024 | 1.3580 | 0.1429 | 1.0000 | 10.0% |
| FET/USDT | P8_200 | survivor | 1.2115 | 0.8959 | 1.8144 | 0.1429 | 1.0000 | 15.0% |
| DEXE/USDT | P100_200 | survivor | 1.6891 | 1.0246 | 1.4890 | 0.0476 | 1.0000 | 40.0% |
| DEXE/USDT | P12_100 | survivor | 1.1871 | 0.9634 | 1.7065 | 0.1905 | 1.0000 | 15.0% |
| DEXE/USDT | P12_144 | survivor | 1.3161 | 0.8948 | 1.3450 | 0.0952 | 1.0000 | 15.0% |
| DEXE/USDT | P12_200 | survivor | 1.3598 | 0.9189 | 1.5236 | 0.1429 | 1.0000 | 30.0% |
| DEXE/USDT | P20_144 | survivor | 1.2489 | 0.9822 | 1.4533 | 0.0952 | 1.0000 | 30.0% |
| DEXE/USDT | P20_200 | survivor | 1.3381 | 1.0108 | 1.4625 | 0.1429 | 1.0000 | 25.0% |
| DEXE/USDT | P21_144 | survivor | 1.2278 | 0.8920 | 1.2641 | 0.0952 | 1.0000 | 10.0% |
| DEXE/USDT | P21_200 | survivor | 1.3506 | 0.9696 | 1.4996 | 0.1429 | 1.0000 | 30.0% |
| DEXE/USDT | P26_200 | survivor | 1.2250 | 1.0722 | 1.5873 | 0.2381 | 1.0000 | 45.0% |
| DEXE/USDT | P34_144 | survivor | 1.2222 | 0.8827 | 1.2525 | 0.0952 | 1.0000 | 15.0% |
| DEXE/USDT | P50_144 | survivor | 1.4465 | 0.8840 | 1.1863 | 0.0476 | 1.0000 | 10.0% |
| DEXE/USDT | P50_200 | survivor | 1.8239 | 1.0941 | 1.5842 | 0.0476 | 1.0000 | 45.0% |
| DEXE/USDT | P55_144 | survivor | 1.4671 | 0.9881 | 1.4736 | 0.0952 | 1.0000 | 15.0% |
| DEXE/USDT | P55_200 | survivor | 1.9333 | 0.9584 | 1.4114 | 0.0476 | 1.0000 | 35.0% |
| DEXE/USDT | P89_200 | survivor | 1.8344 | 1.0334 | 1.4561 | 0.0476 | 1.0000 | 40.0% |
| DEXE/USDT | P8_100 | survivor | 1.2388 | 0.9358 | 1.4171 | 0.1429 | 1.0000 | 20.0% |
| DEXE/USDT | P8_144 | survivor | 1.6756 | 0.8605 | 1.2372 | 0.0476 | 1.0000 | 5.0% |
| DEXE/USDT | P8_200 | survivor | 1.3095 | 0.8770 | 1.3792 | 0.1429 | 1.0000 | 20.0% |
| GMT/USDT | P12_200 | survivor | 1.1511 | 0.8958 | 1.5479 | 0.1429 | 1.0000 | 10.0% |
| GMT/USDT | P8_144 | survivor | 1.1679 | 0.8385 | 1.1320 | 0.0476 | 1.0000 | 0.0% |
| GMT/USDT | P8_200 | survivor | 1.4552 | 0.8777 | 1.3649 | 0.0476 | 1.0000 | 10.0% |
| GRT/USDT | P20_200 | survivor | 1.3953 | 1.0255 | 1.8640 | 0.1429 | 1.0000 | 20.0% |
| GRT/USDT | P8_200 | survivor | 1.2529 | 0.9167 | 1.0979 | 0.0476 | 1.0000 | 0.0% |
| JASMY/USDT | P144_200 | survivor | 1.4928 | 0.9324 | 1.5604 | 0.0952 | 1.0000 | 5.0% |
| MEW/USDT | P8_200 | survivor | 0.9385 | 1.0537 | 2.5606 | 0.6190 | 1.0000 | 15.0% |
| MINA/USDT | P12_200 | survivor | 1.3041 | 0.8462 | 1.2300 | 0.0476 | 1.0000 | 15.0% |
| PENDLE/USDT | P34_144 | survivor | 1.3020 | 1.0317 | 1.7177 | 0.2857 | 1.0000 | 25.0% |
| PUFFER/USDT | P20_200 | survivor | 1.3768 | 0.8692 | 1.1730 | 0.0476 | 1.0000 | 5.0% |
| PUFFER/USDT | P21_200 | survivor | 1.3497 | 0.8315 | 1.1901 | 0.0476 | 1.0000 | 5.0% |
| PUFFER/USDT | P26_200 | survivor | 1.2395 | 0.7953 | 1.1049 | 0.0476 | 1.0000 | 0.0% |
| PYTH/USDT | P8_200 | survivor | 1.1983 | 0.9381 | 1.3438 | 0.1429 | 1.0000 | 15.0% |
| IMX/USDT | P12_200 | survivor | 1.4025 | 0.8646 | 1.3664 | 0.0476 | 1.0000 | 10.0% |
| IMX/USDT | P20_200 | survivor | 1.3382 | 0.8359 | 1.3108 | 0.0476 | 1.0000 | 5.0% |
| IMX/USDT | P21_200 | survivor | 1.2771 | 0.8944 | 1.5427 | 0.0952 | 1.0000 | 10.0% |
| IMX/USDT | P26_200 | survivor | 1.4801 | 0.9304 | 1.3336 | 0.0476 | 1.0000 | 10.0% |
| IMX/USDT | P34_200 | survivor | 1.4172 | 0.8263 | 1.1195 | 0.0476 | 1.0000 | 0.0% |
| IMX/USDT | P50_200 | survivor | 1.2397 | 0.9340 | 1.4742 | 0.1429 | 1.0000 | 20.0% |
| IMX/USDT | P8_200 | survivor | 1.2911 | 0.9344 | 1.1944 | 0.0476 | 1.0000 | 10.0% |
| RENDER/USDT | P8_200 | survivor | 1.1898 | 0.9854 | 2.1729 | 0.1429 | 1.0000 | 15.0% |
| RUNE/USDT | P50_144 | survivor | 1.5230 | 0.8028 | 0.9806 | 0.0476 | 1.0000 | 0.0% |
| RUNE/USDT | P50_200 | survivor | 1.3239 | 0.8765 | 1.4504 | 0.1429 | 1.0000 | 15.0% |
| SUPER/USDT | P8_200 | survivor | 1.1483 | 0.7902 | 1.3455 | 0.0952 | 1.0000 | 5.0% |
| POL/USDT | P20_200 | survivor | 1.3598 | 0.8525 | 1.1099 | 0.0476 | 1.0000 | 0.0% |
| POL/USDT | P21_200 | survivor | 1.4246 | 0.9482 | 2.2514 | 0.1429 | 1.0000 | 15.0% |
| POL/USDT | P26_200 | survivor | 1.3900 | 0.9512 | 1.7154 | 0.0952 | 1.0000 | 20.0% |
| POL/USDT | P34_200 | survivor | 1.3951 | 0.8271 | 1.4665 | 0.0952 | 1.0000 | 10.0% |
| POL/USDT | P8_200 | survivor | 1.5674 | 0.8922 | 1.2930 | 0.0476 | 1.0000 | 10.0% |
| T/USDT | P12_200 | survivor | 1.4215 | 0.7737 | 1.1109 | 0.0476 | 1.0000 | 0.0% |
| ROSE/USDT | P12_200 | survivor | 1.3295 | 0.9080 | 2.0839 | 0.1429 | 1.0000 | 15.0% |
| ROSE/USDT | P34_200 | survivor | 1.3328 | 1.0814 | 2.1933 | 0.1429 | 1.0000 | 20.0% |
| ROSE/USDT | P55_200 | survivor | 1.3264 | 0.8798 | 1.1771 | 0.0476 | 1.0000 | 10.0% |
| SYN/USDT | P20_200 | survivor | 1.2628 | 0.7985 | 1.3276 | 0.0952 | 1.0000 | 5.0% |
| SYN/USDT | P26_200 | survivor | 1.1537 | 0.9247 | 1.6088 | 0.1905 | 1.0000 | 15.0% |
| W/USDT | P12_200 | survivor | 1.0707 | 0.9111 | 1.0841 | 0.0952 | 1.0000 | 0.0% |
| TWT/USDT | P8_200 | survivor | 1.2325 | 0.8075 | 1.1661 | 0.0476 | 1.0000 | 0.0% |
| VELO/USDT | P12_200 | survivor | 1.2459 | 0.8241 | 1.1831 | 0.0476 | 1.0000 | 5.0% |
| VELO/USDT | P20_200 | survivor | 1.2066 | 0.8801 | 1.2469 | 0.1429 | 1.0000 | 15.0% |
| WIN/USDT | P12_200 | survivor | 1.2438 | 0.9232 | 1.4424 | 0.0952 | 1.0000 | 5.0% |
| WIN/USDT | P8_200 | survivor | 1.2855 | 0.8455 | 1.3638 | 0.0952 | 1.0000 | 5.0% |
| WLD/USDT | P20_200 | survivor | 1.2811 | 0.8722 | 1.2411 | 0.0476 | 1.0000 | 5.0% |
| WLD/USDT | P21_200 | survivor | 1.2454 | 0.8634 | 1.1704 | 0.0476 | 1.0000 | 10.0% |
| XPR/USDT | P8_200 | survivor | 1.5710 | 0.9730 | 1.5207 | 0.0476 | 1.0000 | 15.0% |
| ZEN/USDT | P12_200 | survivor | 1.4231 | 0.8876 | 1.4236 | 0.0952 | 1.0000 | 10.0% |
| ZEN/USDT | P8_200 | survivor | 1.5295 | 1.0722 | 2.1736 | 0.1429 | 1.0000 | 40.0% |
| ANYONE/USDT | P55_89 | control | 0.7491 | 0.8417 | 1.1801 | 0.7143 | 1.0000 | 0.0% |
| AGLD/USDT | P8_12 | control | 0.5852 | 0.6360 | 0.7866 | 0.8095 | 1.0000 | 0.0% |
| APE/USDT | P34_55 | control | 0.6065 | 0.8280 | 1.0750 | 1.0000 | 1.0000 | 0.0% |
| BDX/USDT | P20_200 | control | 0.4550 | 0.5365 | 0.6571 | 0.8095 | 1.0000 | 0.0% |
| DODO/USDT | P12_50 | control | 0.6581 | 0.7805 | 1.0417 | 0.8095 | 1.0000 | 0.0% |
| BTC/USDT | P21_26 | control | 0.5727 | 0.5695 | 0.7970 | 0.5714 | 1.0000 | 0.0% |
| COMP/USDT | P12_89 | control | 0.8877 | 0.7743 | 1.0282 | 0.1429 | 1.0000 | 0.0% |
| FLR/USDT | P26_34 | control | 0.3471 | 0.6780 | 1.1042 | 1.0000 | 1.0000 | 0.0% |
| SOL/USDT | P26_89 | control | 0.7709 | 0.7211 | 1.2039 | 0.3333 | 1.0000 | 0.0% |
| PENDLE/USDT | P55_200 | control | 0.8939 | 0.9380 | 1.3132 | 0.6190 | 1.0000 | 10.0% |
| SKL/USDT | P89_200 | control | 1.0809 | 0.9525 | 1.2546 | 0.3333 | 1.0000 | 5.0% |
| SYN/USDT | P20_89 | control | 0.8390 | 0.8649 | 1.1684 | 0.5238 | 1.0000 | 5.0% |

With 20 randomizations the smallest attainable p-value is 1/(20 + 1). The Bonferroni column can therefore not reach significance for a single cell: this leg can show that a surviving cell is *indistinguishable* from its own null, which is what it shows, but it cannot promote one.

The same cells under the sign null (same entry bars, random direction):

| Symbol | Cell | OOS PF | Sign-null mean PF | Sign-null max PF | p-value | p x grid |
|---|---|---|---|---|---|---|
| AERO/USDT | P12_200 | 1.1491 | 0.8364 | 1.0995 | 0.0476 | 1.0000 |
| APT/USDT | P12_144 | 1.1583 | 0.9009 | 1.1452 | 0.0476 | 1.0000 |
| APT/USDT | P12_200 | 1.4628 | 0.8781 | 1.4496 | 0.0476 | 1.0000 |
| APT/USDT | P20_144 | 1.2432 | 0.8401 | 1.3904 | 0.0952 | 1.0000 |
| APT/USDT | P21_144 | 1.2517 | 0.8930 | 1.1826 | 0.0476 | 1.0000 |
| APT/USDT | P26_200 | 1.2284 | 0.8963 | 1.2854 | 0.0952 | 1.0000 |
| AVA/USDT | P20_200 | 1.2322 | 0.8563 | 1.1611 | 0.0476 | 1.0000 |
| AVA/USDT | P21_200 | 1.2320 | 0.8506 | 1.2009 | 0.0476 | 1.0000 |
| AVA/USDT | P26_200 | 1.2614 | 0.8294 | 1.2925 | 0.0952 | 1.0000 |
| AVA/USDT | P34_200 | 1.3090 | 0.7853 | 1.0750 | 0.0476 | 1.0000 |
| AVA/USDT | P50_200 | 1.3796 | 0.8098 | 1.4091 | 0.0952 | 1.0000 |
| BOME/USDT | P26_200 | 1.2403 | 0.8515 | 1.1928 | 0.0476 | 1.0000 |
| BLUR/USDT | P12_144 | 1.3406 | 0.7564 | 0.9892 | 0.0476 | 1.0000 |
| BLUR/USDT | P12_200 | 1.3084 | 0.8623 | 1.2825 | 0.0476 | 1.0000 |
| BLUR/USDT | P21_200 | 1.2169 | 0.8418 | 1.4040 | 0.1429 | 1.0000 |
| BLUR/USDT | P8_144 | 1.2691 | 0.7706 | 1.0375 | 0.0476 | 1.0000 |
| BLUR/USDT | P8_200 | 1.3389 | 0.8755 | 1.3368 | 0.0476 | 1.0000 |
| BRETT/USDT | P8_144 | 1.1474 | 0.8000 | 1.0641 | 0.0476 | 1.0000 |
| BRETT/USDT | P8_200 | 1.4071 | 0.8775 | 1.5490 | 0.0952 | 1.0000 |
| CETUS/USDT | P12_200 | 1.2746 | 0.9314 | 1.3930 | 0.1429 | 1.0000 |
| CETUS/USDT | P8_200 | 1.4565 | 0.8833 | 1.2610 | 0.0476 | 1.0000 |
| DAG/USDT | P8_100 | 1.3172 | 0.7548 | 1.0915 | 0.0476 | 1.0000 |
| CHZ/USDT | P8_200 | 1.1120 | 0.8658 | 1.1665 | 0.1429 | 1.0000 |
| COTI/USDT | P50_144 | 1.2656 | 0.7492 | 0.9982 | 0.0476 | 1.0000 |
| COTI/USDT | P50_200 | 1.3026 | 0.8506 | 1.1453 | 0.0476 | 1.0000 |
| COTI/USDT | P55_144 | 1.2911 | 0.7761 | 0.9425 | 0.0476 | 1.0000 |
| EGLD/USDT | P55_200 | 1.3233 | 0.7426 | 1.1688 | 0.0476 | 1.0000 |
| DIA/USDT | P12_200 | 1.5027 | 0.8381 | 1.0813 | 0.0476 | 1.0000 |
| DIA/USDT | P20_200 | 1.3063 | 0.7722 | 1.1033 | 0.0476 | 1.0000 |
| DIA/USDT | P21_200 | 1.3177 | 0.8715 | 1.1808 | 0.0476 | 1.0000 |
| DIA/USDT | P26_200 | 1.2581 | 0.8565 | 1.0865 | 0.0476 | 1.0000 |
| DIA/USDT | P8_200 | 1.2940 | 0.9439 | 1.2553 | 0.0476 | 1.0000 |
| ENA/USDT | P20_200 | 1.2024 | 0.8110 | 1.1461 | 0.0476 | 1.0000 |
| ENA/USDT | P20_21 | 1.3902 | 0.7091 | 1.0574 | 0.0476 | 1.0000 |
| ENA/USDT | P21_200 | 1.1506 | 0.8954 | 1.5523 | 0.1905 | 1.0000 |
| ENA/USDT | P34_144 | 1.2519 | 0.8735 | 1.2126 | 0.0476 | 1.0000 |
| ENA/USDT | P8_144 | 1.2020 | 0.8581 | 1.2070 | 0.0952 | 1.0000 |
| FLUX/USDT | P8_200 | 1.2695 | 0.9367 | 1.2125 | 0.0476 | 1.0000 |
| FET/USDT | P12_200 | 1.5616 | 0.9734 | 1.5680 | 0.0952 | 1.0000 |
| FET/USDT | P20_200 | 1.2336 | 0.9542 | 1.7895 | 0.2381 | 1.0000 |
| FET/USDT | P21_200 | 1.1274 | 0.9232 | 1.5940 | 0.2381 | 1.0000 |
| FET/USDT | P8_200 | 1.2115 | 0.9062 | 1.4732 | 0.0952 | 1.0000 |
| DEXE/USDT | P100_200 | 1.6891 | 0.8507 | 1.1993 | 0.0476 | 1.0000 |
| DEXE/USDT | P12_100 | 1.1871 | 0.8950 | 1.2391 | 0.0952 | 1.0000 |
| DEXE/USDT | P12_144 | 1.3161 | 0.9303 | 1.5366 | 0.0952 | 1.0000 |
| DEXE/USDT | P12_200 | 1.3598 | 0.8788 | 1.1655 | 0.0476 | 1.0000 |
| DEXE/USDT | P20_144 | 1.2489 | 0.8485 | 1.1800 | 0.0476 | 1.0000 |
| DEXE/USDT | P20_200 | 1.3381 | 0.9830 | 1.3463 | 0.0952 | 1.0000 |
| DEXE/USDT | P21_144 | 1.2278 | 0.9306 | 1.3988 | 0.1905 | 1.0000 |
| DEXE/USDT | P21_200 | 1.3506 | 0.8752 | 1.4540 | 0.1429 | 1.0000 |
| DEXE/USDT | P26_200 | 1.2250 | 0.9195 | 1.2882 | 0.1429 | 1.0000 |
| DEXE/USDT | P34_144 | 1.2222 | 0.8255 | 1.1173 | 0.0476 | 1.0000 |
| DEXE/USDT | P50_144 | 1.4465 | 0.8742 | 1.1722 | 0.0476 | 1.0000 |
| DEXE/USDT | P50_200 | 1.8239 | 0.9226 | 1.7078 | 0.0476 | 1.0000 |
| DEXE/USDT | P55_144 | 1.4671 | 0.9420 | 1.7183 | 0.1429 | 1.0000 |
| DEXE/USDT | P55_200 | 1.9333 | 0.8743 | 1.5103 | 0.0476 | 1.0000 |
| DEXE/USDT | P89_200 | 1.8344 | 0.8012 | 0.9907 | 0.0476 | 1.0000 |
| DEXE/USDT | P8_100 | 1.2388 | 0.9139 | 1.2302 | 0.0476 | 1.0000 |
| DEXE/USDT | P8_144 | 1.6756 | 0.9064 | 1.3482 | 0.0476 | 1.0000 |
| DEXE/USDT | P8_200 | 1.3095 | 1.0080 | 1.4724 | 0.1905 | 1.0000 |
| GMT/USDT | P12_200 | 1.1511 | 0.9273 | 1.5632 | 0.1905 | 1.0000 |
| GMT/USDT | P8_144 | 1.1679 | 0.8271 | 1.1274 | 0.0476 | 1.0000 |
| GMT/USDT | P8_200 | 1.4552 | 0.8437 | 1.1948 | 0.0476 | 1.0000 |
| GRT/USDT | P20_200 | 1.3953 | 0.8747 | 1.4873 | 0.0952 | 1.0000 |
| GRT/USDT | P8_200 | 1.2529 | 0.8812 | 1.4294 | 0.0952 | 1.0000 |
| JASMY/USDT | P144_200 | 1.4928 | 0.8329 | 1.2896 | 0.0476 | 1.0000 |
| MEW/USDT | P8_200 | 0.9385 | 0.8648 | 1.5859 | 0.3810 | 1.0000 |
| MINA/USDT | P12_200 | 1.3041 | 0.8945 | 1.4702 | 0.0952 | 1.0000 |
| PENDLE/USDT | P34_144 | 1.3020 | 0.8290 | 1.0593 | 0.0476 | 1.0000 |
| PUFFER/USDT | P20_200 | 1.3768 | 0.8762 | 1.3227 | 0.0476 | 1.0000 |
| PUFFER/USDT | P21_200 | 1.3497 | 0.8606 | 1.2060 | 0.0476 | 1.0000 |
| PUFFER/USDT | P26_200 | 1.2395 | 0.9163 | 1.1935 | 0.0476 | 1.0000 |
| PYTH/USDT | P8_200 | 1.1983 | 0.9482 | 1.6377 | 0.1429 | 1.0000 |
| IMX/USDT | P12_200 | 1.4025 | 0.8458 | 1.1861 | 0.0476 | 1.0000 |
| IMX/USDT | P20_200 | 1.3382 | 0.8188 | 1.0300 | 0.0476 | 1.0000 |
| IMX/USDT | P21_200 | 1.2771 | 0.9099 | 1.1478 | 0.0476 | 1.0000 |
| IMX/USDT | P26_200 | 1.4801 | 0.8251 | 1.1053 | 0.0476 | 1.0000 |
| IMX/USDT | P34_200 | 1.4172 | 0.8864 | 1.5186 | 0.0952 | 1.0000 |
| IMX/USDT | P50_200 | 1.2397 | 0.7837 | 0.9799 | 0.0476 | 1.0000 |
| IMX/USDT | P8_200 | 1.2911 | 0.8678 | 1.1454 | 0.0476 | 1.0000 |
| RENDER/USDT | P8_200 | 1.1898 | 0.9085 | 1.2994 | 0.1905 | 1.0000 |
| RUNE/USDT | P50_144 | 1.5230 | 0.7183 | 1.1635 | 0.0476 | 1.0000 |
| RUNE/USDT | P50_200 | 1.3239 | 0.7879 | 1.0996 | 0.0476 | 1.0000 |
| SUPER/USDT | P8_200 | 1.1483 | 0.8975 | 1.1465 | 0.0476 | 1.0000 |
| POL/USDT | P20_200 | 1.3598 | 0.9041 | 1.2936 | 0.0476 | 1.0000 |
| POL/USDT | P21_200 | 1.4246 | 0.8608 | 1.7255 | 0.0952 | 1.0000 |
| POL/USDT | P26_200 | 1.3900 | 0.8483 | 1.3395 | 0.0476 | 1.0000 |
| POL/USDT | P34_200 | 1.3951 | 0.8485 | 1.3898 | 0.0476 | 1.0000 |
| POL/USDT | P8_200 | 1.5674 | 0.8669 | 1.1349 | 0.0476 | 1.0000 |
| T/USDT | P12_200 | 1.4215 | 0.8463 | 1.3207 | 0.0476 | 1.0000 |
| ROSE/USDT | P12_200 | 1.3295 | 0.9213 | 1.4664 | 0.1429 | 1.0000 |
| ROSE/USDT | P34_200 | 1.3328 | 0.9386 | 1.4975 | 0.1429 | 1.0000 |
| ROSE/USDT | P55_200 | 1.3264 | 0.8194 | 1.1121 | 0.0476 | 1.0000 |
| SYN/USDT | P20_200 | 1.2628 | 0.8295 | 1.2144 | 0.0476 | 1.0000 |
| SYN/USDT | P26_200 | 1.1537 | 0.9201 | 1.2028 | 0.2381 | 1.0000 |
| W/USDT | P12_200 | 1.0707 | 0.9008 | 1.3475 | 0.3333 | 1.0000 |
| TWT/USDT | P8_200 | 1.2325 | 0.8714 | 1.2948 | 0.0952 | 1.0000 |
| VELO/USDT | P12_200 | 1.2459 | 0.8488 | 1.2314 | 0.0476 | 1.0000 |
| VELO/USDT | P20_200 | 1.2066 | 0.9019 | 1.3070 | 0.1429 | 1.0000 |
| WIN/USDT | P12_200 | 1.2438 | 0.8540 | 1.1763 | 0.0476 | 1.0000 |
| WIN/USDT | P8_200 | 1.2855 | 0.7790 | 1.0039 | 0.0476 | 1.0000 |
| WLD/USDT | P20_200 | 1.2811 | 0.9031 | 1.2226 | 0.0476 | 1.0000 |
| WLD/USDT | P21_200 | 1.2454 | 0.9375 | 1.2399 | 0.0476 | 1.0000 |
| XPR/USDT | P8_200 | 1.5710 | 0.8601 | 1.5559 | 0.0476 | 1.0000 |
| ZEN/USDT | P12_200 | 1.4231 | 0.8694 | 1.4317 | 0.0952 | 1.0000 |
| ZEN/USDT | P8_200 | 1.5295 | 0.8270 | 1.4210 | 0.0476 | 1.0000 |
| ANYONE/USDT | P55_89 | 0.7491 | 0.7752 | 1.0713 | 0.6190 | 1.0000 |
| AGLD/USDT | P8_12 | 0.5852 | 0.6213 | 0.8143 | 0.6190 | 1.0000 |
| APE/USDT | P34_55 | 0.6065 | 0.7024 | 0.9504 | 0.7143 | 1.0000 |
| BDX/USDT | P20_200 | 0.4550 | 0.6204 | 0.8224 | 0.9524 | 1.0000 |
| DODO/USDT | P12_50 | 0.6581 | 0.7361 | 0.8805 | 0.9048 | 1.0000 |
| BTC/USDT | P21_26 | 0.5727 | 0.4980 | 1.0527 | 0.3333 | 1.0000 |
| COMP/USDT | P12_89 | 0.8877 | 0.7539 | 0.9610 | 0.1429 | 1.0000 |
| FLR/USDT | P26_34 | 0.3471 | 0.5347 | 0.8084 | 0.9524 | 1.0000 |
| SOL/USDT | P26_89 | 0.7709 | 0.6316 | 0.8602 | 0.1429 | 1.0000 |
| PENDLE/USDT | P55_200 | 0.8939 | 0.8000 | 1.0896 | 0.3333 | 1.0000 |
| SKL/USDT | P89_200 | 1.0809 | 0.6986 | 1.0805 | 0.0476 | 1.0000 |
| SYN/USDT | P20_89 | 0.8390 | 0.8763 | 1.1892 | 0.6667 | 1.0000 |

## Verdict

- 613 of 17556 cells show an out-of-sample net PF above 1; the timing null produces 1611. The observed tail is no larger than what the timing null delivers.
- 103 real cells clear the §3.4 out-of-sample gate against 329 timing-null cells: the gate's false-positive rate under no information is 1.87% of the grid.
- The best real cell (net PF 1.9504) sits against a best timing cell of 2.5310; the family-wise probability that a null cell reaches the real best is 1 - 6.73e-03.
- The real rule beats its own timing null in 4521 of 17556 cells and loses to it in 13035 (sign test p = 0.00e+00).
- Grid-wide null counts (cells with an out-of-sample net PF above 1 / cells clearing the gate): real 613/103; timing 1611/329; block 4286/1195; sign 773/68.
- 106 surviving cells were re-randomized; 0 keep an out-of-sample net PF above the real one at a Bonferroni-corrected level over 17556 tests.

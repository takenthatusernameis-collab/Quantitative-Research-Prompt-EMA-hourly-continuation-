# Grid-Wide Out-of-Sample Audit — EMA Hourly Continuation

**Source run:** `results/20261021_172619_grid`
**Generated:** 2026-10-22T02:09:36.365621+00:00
**Universe:** 266 symbols, 17556 grid cells
**OOS window:** trailing 35% of each symbol's bars, entries restricted to the window
**Cost stress:** 2x fees and slippage (base 10 bps taker + 2 bps slippage per side)

## Why this leg exists

The pipeline's OOS gate was only ever applied to the 287 cells whose *in-sample* net PF exceeded 1. This leg applies the same out-of-sample window to all 17556 cells, so a cell whose in-sample window was unlucky cannot hide a survivor from the program.

## Leg 1 — Out-of-sample coverage

| Metric | Value |
|---|---|
| Cells screened | 17556 |
| Cells with at least one out-of-sample trade | 17491 |
| Cells with no out-of-sample trade | 65 |
| Cells with at least 30 out-of-sample trades | 17363 |
| Pooled out-of-sample net PF (all cells) | 0.6676 |
| Pooled out-of-sample net PF under 2x costs | 0.4781 |
| Pooled out-of-sample net P&L | -29935836 |
| Cells whose blotter net PF disagrees with the stored summary | 0 |
| Cells read from the legacy uncompressed blotter layout | 0 |

## Leg 2 — Out-of-sample net PF across the whole grid

| Statistic | Out-of-sample net PF | In-sample net PF |
|---|---|---|
| cells with a defined net PF | 17491 | 17556 |
| mean | 0.6596 | 0.7264 |
| median | 0.6584 | 0.7322 |
| p05 | 0.3602 | 0.4972 |
| p25 | 0.5512 | 0.6491 |
| p75 | 0.7647 | 0.8105 |
| p95 | 0.9561 | 0.9300 |
| max | 1.9955 | 1.7914 |

The 65 cells without a single out-of-sample trade are missing evidence, not a loss, and are excluded from the distribution.

- Cells with out-of-sample net PF > 1: **608** of 17556 (3.46%).
- Expected under a no-edge null: ~50% (excess -0.4654).
- Cells with out-of-sample net PF > 1 **and** at least 30 out-of-sample trades: **591**.
- Cells with out-of-sample net PF > 1, at least 30 out-of-sample trades, and out-of-sample net PF still > 1 under 2x costs: **106**.

## Leg 3 — Screen survivors (verified with a real backtest)

Screen: out-of-sample net PF > 0.9 with at least 30 out-of-sample trades. 120 cell(s) kept.

| Symbol | Cell | OOS trades | Screen OOS PF | Screen OOS stress PF | Exact OOS PF | Exact OOS Sharpe | Exact stress OOS PF | Label |
|---|---|---|---|---|---|---|---|---|
| DEXE/USDT | P55_200 | 63 | 1.8907 | 1.6783 | 1.9333 | 2.6319 | 1.7085 | exploratory signal |
| DEXE/USDT | P50_200 | 70 | 1.7875 | 1.5833 | 1.8239 | 2.5632 | 1.6091 | exploratory signal |
| DEXE/USDT | P89_200 | 56 | 1.7875 | 1.5267 | 1.7448 | 2.1281 | 1.4799 | exploratory signal |
| BRETT/USDT | P8_200 | 42 | 1.6802 | 1.5168 | 1.6888 | 1.9493 | 1.5322 | exploratory signal |
| DEXE/USDT | P21_200 | 64 | 1.6713 | 1.5219 | 1.3506 | 1.4994 | 1.1946 | exploratory signal |
| DEXE/USDT | P20_200 | 66 | 1.6404 | 1.4926 | 1.3381 | 1.4680 | 1.1830 | exploratory signal |
| DEXE/USDT | P100_200 | 61 | 1.6140 | 1.3740 | 1.6140 | 1.8955 | 1.3617 | exploratory signal |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.3857 | 1.6086 | 1.8688 | 1.3924 | exploratory signal |
| XPR/USDT | P8_200 | 44 | 1.5710 | 1.3538 | 1.5261 | 1.5084 | 1.3106 | exploratory signal |
| FET/USDT | P12_200 | 36 | 1.5616 | 1.4435 | 1.5616 | 1.3738 | 1.4404 | exploratory signal |
| DEXE/USDT | P8_144 | 83 | 1.5518 | 1.4012 | 1.6286 | 2.4762 | 1.4581 | exploratory signal |
| DEXE/USDT | P55_144 | 76 | 1.5373 | 1.3363 | 1.4671 | 1.8373 | 1.2660 | exploratory signal |
| RUNE/USDT | P50_144 | 120 | 1.5230 | 1.0963 | 1.5230 | 2.4239 | 1.1018 | exploratory signal |
| FLUX/USDT | P8_200 | 93 | 1.5170 | 1.2910 | 1.2427 | 1.2438 | 1.0272 | credible candidate |
| JASMY/USDT | P144_200 | 56 | 1.4928 | 1.0550 | 1.4928 | 1.5876 | 1.0619 | exploratory signal |
| ZEN/USDT | P8_200 | 33 | 1.4808 | 1.3582 | 1.6713 | 1.7541 | 1.4974 | credible candidate |
| IMX/USDT | P26_200 | 114 | 1.4801 | 1.2167 | 1.4801 | 2.2564 | 1.2246 | exploratory signal |
| GMT/USDT | P8_200 | 88 | 1.4737 | 1.2727 | 1.4743 | 1.9895 | 1.2697 | exploratory signal |
| IMX/USDT | P50_55 | 44 | 1.4581 | 0.9954 | 1.4581 | 1.3460 | 1.0113 | exploratory signal |
| CETUS/USDT | P8_200 | 85 | 1.4565 | 1.2715 | 1.4174 | 1.7508 | 1.2401 | credible candidate |
| DEXE/USDT | P50_144 | 89 | 1.4465 | 1.2605 | 1.4465 | 1.8547 | 1.2581 | exploratory signal |
| GRT/USDT | P20_200 | 57 | 1.4433 | 1.2623 | 1.3953 | 1.4236 | 1.2070 | exploratory signal |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.2155 | 1.4246 | 1.6027 | 1.2175 | exploratory signal |
| DIA/USDT | P12_200 | 84 | 1.4204 | 1.1836 | 1.5029 | 2.0308 | 1.2510 | exploratory signal |
| DEXE/USDT | P12_200 | 65 | 1.3968 | 1.2667 | 1.3235 | 1.4204 | 1.1782 | exploratory signal |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.1151 | 1.3951 | 1.7600 | 1.1220 | exploratory signal |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.0315 | 1.3902 | 1.1879 | 1.0324 | credible candidate |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.1647 | 1.3900 | 1.5210 | 1.1701 | exploratory signal |
| IMX/USDT | P12_200 | 94 | 1.3886 | 1.1734 | 1.4025 | 1.8017 | 1.1843 | exploratory signal |
| AVA/USDT | P50_200 | 88 | 1.3796 | 1.0974 | 1.3796 | 1.6157 | 1.0947 | exploratory signal |
| PUFFER/USDT | P20_200 | 81 | 1.3768 | 1.2245 | 1.4038 | 1.8699 | 1.2514 | credible candidate |
| IMX/USDT | P34_200 | 101 | 1.3729 | 1.1217 | 1.3871 | 1.8507 | 1.1430 | exploratory signal |
| GRT/USDT | P8_200 | 57 | 1.3602 | 1.2002 | 1.2529 | 0.9465 | 1.0880 | exploratory signal |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.1617 | 1.3597 | 1.3904 | 1.1649 | exploratory signal |
| DEXE/USDT | P8_200 | 56 | 1.3520 | 1.2415 | 1.2721 | 1.1854 | 1.1409 | exploratory signal |
| PUFFER/USDT | P21_200 | 75 | 1.3497 | 1.1974 | 1.3789 | 1.7012 | 1.2253 | exploratory signal |
| RUNE/USDT | P55_144 | 112 | 1.3458 | 0.9527 | 1.3458 | 1.6928 | 0.9594 | exploratory signal |
| APT/USDT | P12_200 | 36 | 1.3367 | 1.1823 | 1.4641 | 1.2354 | 1.2962 | exploratory signal |
| ROSE/USDT | P34_200 | 88 | 1.3328 | 1.1080 | 1.3328 | 1.5329 | 1.1197 | exploratory signal |
| T/USDT | P12_200 | 52 | 1.3272 | 1.0711 | 1.3272 | 1.0564 | 1.0559 | exploratory signal |
| ROSE/USDT | P55_200 | 112 | 1.3264 | 1.0651 | 1.3264 | 1.6361 | 1.0699 | exploratory signal |
| RUNE/USDT | P50_200 | 89 | 1.3239 | 1.0048 | 1.3239 | 1.4254 | 1.0085 | exploratory signal |
| EGLD/USDT | P55_200 | 99 | 1.3233 | 1.0262 | 1.3233 | 1.4725 | 1.0202 | exploratory signal |
| DAG/USDT | P8_100 | 109 | 1.3177 | 1.0644 | 1.3177 | 1.5113 | 1.0588 | exploratory signal |
| WLD/USDT | P20_200 | 94 | 1.3171 | 1.1761 | 1.2811 | 1.3078 | 1.1347 | credible candidate |
| DEXE/USDT | P12_144 | 88 | 1.3128 | 1.1594 | 1.2833 | 1.3059 | 1.1198 | exploratory signal |
| AVA/USDT | P34_200 | 97 | 1.3090 | 1.0502 | 1.3090 | 1.4280 | 1.0465 | exploratory signal |
| IMX/USDT | P20_200 | 122 | 1.3057 | 1.0826 | 1.3382 | 1.7558 | 1.1116 | exploratory signal |
| IMX/USDT | P8_200 | 93 | 1.3049 | 1.1024 | 1.2911 | 1.3772 | 1.0899 | credible candidate |
| DIA/USDT | P21_200 | 120 | 1.3037 | 1.0515 | 1.3177 | 1.6016 | 1.0516 | exploratory signal |
| BLUR/USDT | P12_144 | 103 | 1.3034 | 1.0910 | 1.3406 | 1.6906 | 1.1106 | exploratory signal |
| COTI/USDT | P50_200 | 99 | 1.3026 | 1.0675 | 1.3026 | 1.4852 | 1.0758 | exploratory signal |
| PENDLE/USDT | P34_144 | 98 | 1.3020 | 1.0650 | 1.3020 | 1.4488 | 1.0713 | exploratory signal |
| ZRO/USDT | P50_55 | 38 | 1.2964 | 0.9794 | 1.2964 | 0.8785 | 0.9728 | exploratory signal |
| RUNE/USDT | P55_200 | 91 | 1.2958 | 0.9705 | 1.2958 | 1.3161 | 0.9697 | exploratory signal |
| WIN/USDT | P8_200 | 104 | 1.2949 | 1.0848 | 1.3047 | 1.4054 | 1.0781 | exploratory signal |
| DIA/USDT | P20_200 | 122 | 1.2927 | 1.0444 | 1.3064 | 1.5725 | 1.0449 | exploratory signal |
| COTI/USDT | P55_144 | 112 | 1.2911 | 1.0220 | 1.2911 | 1.5520 | 1.0354 | exploratory signal |
| AVA/USDT | P26_89 | 161 | 1.2879 | 0.9658 | 1.2879 | 1.7737 | 0.9717 | exploratory signal |
| SUPER/USDT | P8_200 | 64 | 1.2855 | 1.0890 | 1.1483 | 0.6273 | 0.9667 | exploratory signal |
| BLUR/USDT | P8_200 | 83 | 1.2799 | 1.0998 | 1.3389 | 1.4745 | 1.1488 | credible candidate |
| ENA/USDT | P8_12 | 66 | 1.2792 | 0.9252 | 1.2792 | 1.0630 | 0.9228 | exploratory signal |
| NEAR/USDT | P100_144 | 76 | 1.2790 | 0.9474 | 1.2790 | 1.1363 | 0.9421 | exploratory signal |
| WIN/USDT | P12_200 | 96 | 1.2759 | 1.0616 | 1.2655 | 1.1939 | 1.0384 | exploratory signal |
| BLUR/USDT | P12_200 | 86 | 1.2755 | 1.0907 | 1.3084 | 1.4079 | 1.1201 | exploratory signal |
| CETUS/USDT | P12_200 | 68 | 1.2746 | 1.1305 | 1.2746 | 1.1335 | 1.1338 | credible candidate |
| VELO/USDT | P12_200 | 114 | 1.2723 | 1.1009 | 1.2464 | 1.2649 | 1.0736 | exploratory signal |
| ZEC/USDT | P8_12 | 61 | 1.2715 | 0.9755 | 1.2715 | 1.0003 | 0.9712 | exploratory signal |
| PUFFER/USDT | P26_200 | 75 | 1.2674 | 1.1244 | 1.2674 | 1.2929 | 1.1275 | exploratory signal |
| COTI/USDT | P50_144 | 115 | 1.2656 | 1.0100 | 1.2656 | 1.4546 | 1.0217 | exploratory signal |
| SYN/USDT | P20_200 | 99 | 1.2628 | 1.0678 | 1.2314 | 1.1317 | 1.0362 | exploratory signal |
| AVA/USDT | P26_200 | 99 | 1.2616 | 1.0341 | 1.2616 | 1.2779 | 1.0338 | exploratory signal |
| TWT/USDT | P8_200 | 73 | 1.2604 | 1.0174 | 1.2604 | 1.0492 | 1.0098 | exploratory signal |
| JASMY/USDT | P50_144 | 128 | 1.2551 | 0.9350 | 1.2551 | 1.3655 | 0.9305 | exploratory signal |
| AVA/USDT | P26_100 | 153 | 1.2522 | 0.9608 | 1.2522 | 1.5255 | 0.9604 | exploratory signal |
| ENA/USDT | P34_144 | 111 | 1.2519 | 1.0555 | 1.2519 | 1.3176 | 1.0600 | exploratory signal |
| AVA/USDT | P21_144 | 141 | 1.2461 | 0.9860 | 1.2461 | 1.4246 | 0.9836 | exploratory signal |
| AVA/USDT | P20_144 | 141 | 1.2457 | 0.9854 | 1.2457 | 1.4228 | 0.9830 | exploratory signal |
| CFG/USDT | P50_55 | 55 | 1.2457 | 0.8697 | 1.2457 | 0.8515 | 0.8599 | exploratory signal |
| WLD/USDT | P21_200 | 103 | 1.2454 | 1.1119 | 1.2454 | 1.1847 | 1.1074 | exploratory signal |
| NEO/USDT | P8_144 | 90 | 1.2451 | 0.9983 | 1.1382 | 0.6952 | 0.8863 | exploratory signal |
| BRETT/USDT | P8_144 | 78 | 1.2444 | 1.0708 | 1.1688 | 0.8800 | 1.0004 | exploratory signal |
| DIA/USDT | P26_200 | 114 | 1.2413 | 1.0018 | 1.2789 | 1.3786 | 1.0211 | exploratory signal |
| AVA/USDT | P55_200 | 94 | 1.2408 | 0.9881 | 1.2408 | 1.1506 | 0.9884 | exploratory signal |
| BOME/USDT | P26_200 | 112 | 1.2403 | 1.0411 | 1.2403 | 1.2337 | 1.0387 | exploratory signal |
| DEXE/USDT | P26_200 | 63 | 1.2401 | 1.1233 | 1.2250 | 1.0428 | 1.0851 | exploratory signal |
| IMX/USDT | P50_200 | 102 | 1.2397 | 1.0012 | 1.2397 | 1.2209 | 1.0091 | exploratory signal |
| CHZ/USDT | P8_200 | 66 | 1.2395 | 1.0876 | 1.1137 | 0.5232 | 0.9676 | exploratory signal |
| IMX/USDT | P21_200 | 111 | 1.2394 | 1.0252 | 1.2771 | 1.4252 | 1.0591 | exploratory signal |
| MNT/USDT | P144_200 | 66 | 1.2394 | 0.6727 | 1.2394 | 0.8918 | 0.6737 | exploratory signal |
| DEXE/USDT | P20_144 | 90 | 1.2391 | 1.0938 | 1.2489 | 1.1870 | 1.0920 | exploratory signal |
| RLC/USDT | P12_200 | 85 | 1.2384 | 0.9590 | 1.2384 | 1.0364 | 0.9507 | exploratory signal |
| DEXE/USDT | P8_100 | 114 | 1.2379 | 1.0947 | 1.2388 | 1.2518 | 1.0877 | exploratory signal |
| JASMY/USDT | P20_144 | 144 | 1.2376 | 0.9714 | 1.2048 | 1.2165 | 0.9398 | exploratory signal |
| HNT/USDT | P34_144 | 110 | 1.2353 | 0.9969 | 1.2353 | 1.2283 | 0.9989 | exploratory signal |
| VELO/USDT | P20_200 | 107 | 1.2339 | 1.0705 | 1.2073 | 1.0530 | 1.0416 | exploratory signal |
| FET/USDT | P20_200 | 34 | 1.2336 | 1.1324 | 1.2336 | 0.6599 | 1.1306 | exploratory signal |
| AVA/USDT | P20_200 | 105 | 1.2326 | 1.0120 | 1.2326 | 1.2074 | 1.0142 | exploratory signal |
| AVA/USDT | P21_200 | 105 | 1.2324 | 1.0117 | 1.2324 | 1.2067 | 1.0139 | exploratory signal |
| JASMY/USDT | P21_144 | 146 | 1.2316 | 0.9681 | 1.1995 | 1.1954 | 0.9367 | exploratory signal |
| JASMY/USDT | P34_144 | 148 | 1.2295 | 0.9399 | 1.2295 | 1.3374 | 0.9321 | exploratory signal |
| BLUR/USDT | P8_144 | 112 | 1.2248 | 1.0202 | 1.2691 | 1.4448 | 1.0464 | exploratory signal |
| GMT/USDT | P8_144 | 110 | 1.2242 | 1.0183 | 1.1404 | 0.7598 | 0.9364 | exploratory signal |
| APT/USDT | P21_144 | 93 | 1.2226 | 1.0567 | 1.2517 | 1.2323 | 1.0800 | exploratory signal |
| DEXE/USDT | P34_144 | 88 | 1.2222 | 1.0632 | 1.2222 | 1.0586 | 1.0649 | exploratory signal |
| DIA/USDT | P8_200 | 89 | 1.2169 | 1.0141 | 1.2941 | 1.3743 | 1.0808 | exploratory signal |
| DEXE/USDT | P21_144 | 89 | 1.2166 | 1.0751 | 1.2278 | 1.0952 | 1.0745 | exploratory signal |
| MINA/USDT | P12_200 | 75 | 1.2162 | 1.0532 | 1.3342 | 1.2988 | 1.1513 | exploratory signal |
| AVA/USDT | P8_100 | 138 | 1.2145 | 0.9790 | 1.1956 | 1.1992 | 0.9699 | exploratory signal |
| W/USDT | P12_200 | 80 | 1.2138 | 1.0512 | 1.0902 | 0.4972 | 0.9214 | exploratory signal |
| MNT/USDT | P20_100 | 123 | 1.2136 | 0.8347 | 1.2136 | 1.1471 | 0.8332 | exploratory signal |
| APT/USDT | P20_144 | 90 | 1.2129 | 1.0507 | 1.2432 | 1.1762 | 1.0744 | exploratory signal |
| PEOPLE/USDT | P21_144 | 123 | 1.2126 | 0.9945 | 1.2126 | 1.1660 | 0.9931 | exploratory signal |
| FET/USDT | P8_200 | 45 | 1.2115 | 1.1200 | 1.2115 | 0.7046 | 1.1183 | exploratory signal |
| POL/USDT | P20_144 | 73 | 1.2058 | 0.9964 | 1.2058 | 0.9025 | 1.0009 | exploratory signal |
| POL/USDT | P21_144 | 73 | 1.2037 | 0.9916 | 1.2037 | 0.8901 | 0.9951 | exploratory signal |
| APT/USDT | P26_200 | 80 | 1.2029 | 1.0384 | 1.2284 | 1.0173 | 1.0591 | exploratory signal |
| ENA/USDT | P20_200 | 106 | 1.2024 | 1.0479 | 1.2024 | 1.0480 | 1.0475 | exploratory signal |
| ENA/USDT | P8_144 | 123 | 1.2020 | 1.0456 | 1.2020 | 1.1170 | 1.0433 | exploratory signal |
| ZEN/USDT | P12_200 | 37 | 1.2002 | 1.0623 | 1.3991 | 1.1387 | 1.2442 | exploratory signal |

## Leg 3b — The closest survivors: cells that also survive the cost stress

These are the verified cells whose out-of-sample net PF is above 1 both at the registered costs and at 2x costs. The last three columns are the full-sample result, which is what a promotion would have to survive as well.

| Symbol | Cell | OOS trades | Exact OOS PF | Exact OOS Sharpe | Exact stress OOS PF | Full-sample net PF | Full-sample stress PF | Label |
|---|---|---|---|---|---|---|---|---|
| DEXE/USDT | P55_200 | 63 | 1.9333 | 2.6319 | 1.7085 | 0.9677 | 0.7986 | exploratory signal |
| DEXE/USDT | P50_200 | 70 | 1.8239 | 2.5632 | 1.6091 | 1.0694 | 0.8885 | exploratory signal |
| DEXE/USDT | P89_200 | 56 | 1.7448 | 2.1281 | 1.4799 | 0.8904 | 0.7210 | exploratory signal |
| BRETT/USDT | P8_200 | 42 | 1.6888 | 1.9493 | 1.5322 | 1.0449 | 0.9495 | exploratory signal |
| DEXE/USDT | P21_200 | 64 | 1.3506 | 1.4994 | 1.1946 | 0.9970 | 0.8482 | exploratory signal |
| DEXE/USDT | P20_200 | 66 | 1.3381 | 1.4680 | 1.1830 | 0.9864 | 0.8408 | exploratory signal |
| DEXE/USDT | P100_200 | 61 | 1.6140 | 1.8955 | 1.3617 | 0.8062 | 0.6470 | exploratory signal |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.8688 | 1.3924 | 1.1216 | 0.9604 | exploratory signal |
| XPR/USDT | P8_200 | 44 | 1.5261 | 1.5084 | 1.3106 | 0.9178 | 0.7837 | exploratory signal |
| FET/USDT | P12_200 | 36 | 1.5616 | 1.3738 | 1.4404 | 1.0341 | 0.9161 | exploratory signal |
| DEXE/USDT | P8_144 | 83 | 1.6286 | 2.4762 | 1.4581 | 0.9214 | 0.7767 | exploratory signal |
| DEXE/USDT | P55_144 | 76 | 1.4671 | 1.8373 | 1.2660 | 0.8847 | 0.7059 | exploratory signal |
| RUNE/USDT | P50_144 | 120 | 1.5230 | 2.4239 | 1.1018 | 0.9328 | 0.7286 | exploratory signal |
| FLUX/USDT | P8_200 | 93 | 1.2427 | 1.2438 | 1.0272 | 1.2228 | 1.0591 | credible candidate |
| JASMY/USDT | P144_200 | 56 | 1.4928 | 1.5876 | 1.0619 | 1.0245 | 0.7809 | exploratory signal |
| ZEN/USDT | P8_200 | 33 | 1.6713 | 1.7541 | 1.4974 | 1.2569 | 1.1295 | credible candidate |
| IMX/USDT | P26_200 | 114 | 1.4801 | 2.2564 | 1.2246 | 1.1185 | 0.9501 | exploratory signal |
| GMT/USDT | P8_200 | 88 | 1.4743 | 1.9895 | 1.2697 | 0.9866 | 0.8399 | exploratory signal |
| IMX/USDT | P50_55 | 44 | 1.4581 | 1.3460 | 1.0113 | 1.2990 | 0.9259 | exploratory signal |
| CETUS/USDT | P8_200 | 85 | 1.4174 | 1.7508 | 1.2401 | 1.2740 | 1.1315 | credible candidate |
| DEXE/USDT | P50_144 | 89 | 1.4465 | 1.8547 | 1.2581 | 0.8699 | 0.7085 | exploratory signal |
| GRT/USDT | P20_200 | 57 | 1.3953 | 1.4236 | 1.2070 | 1.1087 | 0.9679 | exploratory signal |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.6027 | 1.2175 | 1.0354 | 0.8696 | exploratory signal |
| DIA/USDT | P12_200 | 84 | 1.5029 | 2.0308 | 1.2510 | 1.1315 | 0.9534 | exploratory signal |
| DEXE/USDT | P12_200 | 65 | 1.3235 | 1.4204 | 1.1782 | 1.0165 | 0.8607 | exploratory signal |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.7600 | 1.1220 | 1.0278 | 0.8389 | exploratory signal |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.1879 | 1.0324 | 1.3253 | 1.0289 | credible candidate |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.5210 | 1.1701 | 0.9932 | 0.8286 | exploratory signal |
| IMX/USDT | P12_200 | 94 | 1.4025 | 1.8017 | 1.1843 | 0.9999 | 0.8682 | exploratory signal |
| AVA/USDT | P50_200 | 88 | 1.3796 | 1.6157 | 1.0947 | 0.9483 | 0.7721 | exploratory signal |
| PUFFER/USDT | P20_200 | 81 | 1.4038 | 1.8699 | 1.2514 | 1.1884 | 1.0506 | credible candidate |
| IMX/USDT | P34_200 | 101 | 1.3871 | 1.8507 | 1.1430 | 1.1547 | 0.9774 | exploratory signal |
| GRT/USDT | P8_200 | 57 | 1.2529 | 0.9465 | 1.0880 | 0.9520 | 0.8433 | exploratory signal |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.3904 | 1.1649 | 1.0429 | 0.8651 | exploratory signal |
| DEXE/USDT | P8_200 | 56 | 1.2721 | 1.1854 | 1.1409 | 0.9059 | 0.7682 | exploratory signal |
| PUFFER/USDT | P21_200 | 75 | 1.3789 | 1.7012 | 1.2253 | 1.1333 | 0.9964 | exploratory signal |
| APT/USDT | P12_200 | 36 | 1.4641 | 1.2354 | 1.2962 | 1.0656 | 0.9139 | exploratory signal |
| ROSE/USDT | P34_200 | 88 | 1.3328 | 1.5329 | 1.1197 | 1.0394 | 0.8882 | exploratory signal |
| T/USDT | P12_200 | 52 | 1.3272 | 1.0564 | 1.0559 | 0.9175 | 0.7291 | exploratory signal |
| ROSE/USDT | P55_200 | 112 | 1.3264 | 1.6361 | 1.0699 | 1.0227 | 0.8555 | exploratory signal |
| RUNE/USDT | P50_200 | 89 | 1.3239 | 1.4254 | 1.0085 | 1.0682 | 0.8698 | exploratory signal |
| EGLD/USDT | P55_200 | 99 | 1.3233 | 1.4725 | 1.0202 | 0.8953 | 0.7049 | exploratory signal |
| DAG/USDT | P8_100 | 109 | 1.3177 | 1.5113 | 1.0588 | 0.7768 | 0.6673 | exploratory signal |
| WLD/USDT | P20_200 | 94 | 1.2811 | 1.3078 | 1.1347 | 1.1725 | 1.0544 | credible candidate |
| DEXE/USDT | P12_144 | 88 | 1.2833 | 1.3059 | 1.1198 | 0.9756 | 0.8190 | exploratory signal |
| AVA/USDT | P34_200 | 97 | 1.3090 | 1.4280 | 1.0465 | 0.8734 | 0.7152 | exploratory signal |
| IMX/USDT | P20_200 | 122 | 1.3382 | 1.7558 | 1.1116 | 1.1008 | 0.9382 | exploratory signal |
| IMX/USDT | P8_200 | 93 | 1.2911 | 1.3772 | 1.0899 | 1.2102 | 1.0487 | credible candidate |
| DIA/USDT | P21_200 | 120 | 1.3177 | 1.6016 | 1.0516 | 0.9699 | 0.7985 | exploratory signal |
| BLUR/USDT | P12_144 | 103 | 1.3406 | 1.6906 | 1.1106 | 1.0281 | 0.8659 | exploratory signal |
| COTI/USDT | P50_200 | 99 | 1.3026 | 1.4852 | 1.0758 | 1.0597 | 0.8962 | exploratory signal |
| PENDLE/USDT | P34_144 | 98 | 1.3020 | 1.4488 | 1.0713 | 0.8413 | 0.7069 | exploratory signal |
| WIN/USDT | P8_200 | 104 | 1.3047 | 1.4054 | 1.0781 | 1.0109 | 0.8218 | exploratory signal |
| DIA/USDT | P20_200 | 122 | 1.3064 | 1.5725 | 1.0449 | 0.9440 | 0.7763 | exploratory signal |
| COTI/USDT | P55_144 | 112 | 1.2911 | 1.5520 | 1.0354 | 0.8966 | 0.7256 | exploratory signal |
| BLUR/USDT | P8_200 | 83 | 1.3389 | 1.4745 | 1.1488 | 1.1877 | 1.0230 | credible candidate |
| WIN/USDT | P12_200 | 96 | 1.2655 | 1.1939 | 1.0384 | 0.8747 | 0.7033 | exploratory signal |
| BLUR/USDT | P12_200 | 86 | 1.3084 | 1.4079 | 1.1201 | 1.0764 | 0.9105 | exploratory signal |
| CETUS/USDT | P12_200 | 68 | 1.2746 | 1.1335 | 1.1338 | 1.2391 | 1.1033 | credible candidate |
| VELO/USDT | P12_200 | 114 | 1.2464 | 1.2649 | 1.0736 | 0.9932 | 0.8813 | exploratory signal |
| PUFFER/USDT | P26_200 | 75 | 1.2674 | 1.2929 | 1.1275 | 1.0037 | 0.8831 | exploratory signal |
| COTI/USDT | P50_144 | 115 | 1.2656 | 1.4546 | 1.0217 | 0.8727 | 0.7127 | exploratory signal |
| SYN/USDT | P20_200 | 99 | 1.2314 | 1.1317 | 1.0362 | 0.9918 | 0.8525 | exploratory signal |
| AVA/USDT | P26_200 | 99 | 1.2616 | 1.2779 | 1.0338 | 0.8463 | 0.7039 | exploratory signal |
| TWT/USDT | P8_200 | 73 | 1.2604 | 1.0492 | 1.0098 | 0.8890 | 0.7168 | exploratory signal |
| ENA/USDT | P34_144 | 111 | 1.2519 | 1.3176 | 1.0600 | 0.9014 | 0.7862 | exploratory signal |
| WLD/USDT | P21_200 | 103 | 1.2454 | 1.1847 | 1.1074 | 1.0863 | 0.9732 | exploratory signal |
| BRETT/USDT | P8_144 | 78 | 1.1688 | 0.8800 | 1.0004 | 0.8902 | 0.7915 | exploratory signal |
| DIA/USDT | P26_200 | 114 | 1.2789 | 1.3786 | 1.0211 | 0.9740 | 0.7945 | exploratory signal |
| BOME/USDT | P26_200 | 112 | 1.2403 | 1.2337 | 1.0387 | 0.9895 | 0.8568 | exploratory signal |
| DEXE/USDT | P26_200 | 63 | 1.2250 | 1.0428 | 1.0851 | 0.9471 | 0.8032 | exploratory signal |
| IMX/USDT | P50_200 | 102 | 1.2397 | 1.2209 | 1.0091 | 1.0175 | 0.8471 | exploratory signal |
| IMX/USDT | P21_200 | 111 | 1.2771 | 1.4252 | 1.0591 | 1.0431 | 0.8926 | exploratory signal |
| DEXE/USDT | P20_144 | 90 | 1.2489 | 1.1870 | 1.0920 | 0.9166 | 0.7706 | exploratory signal |
| DEXE/USDT | P8_100 | 114 | 1.2388 | 1.2518 | 1.0877 | 0.9076 | 0.7501 | exploratory signal |
| VELO/USDT | P20_200 | 107 | 1.2073 | 1.0530 | 1.0416 | 0.9855 | 0.8674 | exploratory signal |
| FET/USDT | P20_200 | 34 | 1.2336 | 0.6599 | 1.1306 | 1.0236 | 0.9042 | exploratory signal |
| AVA/USDT | P20_200 | 105 | 1.2326 | 1.2074 | 1.0142 | 0.8490 | 0.7083 | exploratory signal |
| AVA/USDT | P21_200 | 105 | 1.2324 | 1.2067 | 1.0139 | 0.8316 | 0.6937 | exploratory signal |
| BLUR/USDT | P8_144 | 112 | 1.2691 | 1.4448 | 1.0464 | 1.0347 | 0.8783 | exploratory signal |
| APT/USDT | P21_144 | 93 | 1.2517 | 1.2323 | 1.0800 | 1.0362 | 0.8804 | exploratory signal |
| DEXE/USDT | P34_144 | 88 | 1.2222 | 1.0586 | 1.0649 | 0.9170 | 0.7513 | exploratory signal |
| DIA/USDT | P8_200 | 89 | 1.2941 | 1.3743 | 1.0808 | 1.0236 | 0.8644 | exploratory signal |
| DEXE/USDT | P21_144 | 89 | 1.2278 | 1.0952 | 1.0745 | 0.9016 | 0.7595 | exploratory signal |
| MINA/USDT | P12_200 | 75 | 1.3342 | 1.2988 | 1.1513 | 0.9442 | 0.8021 | exploratory signal |
| APT/USDT | P20_144 | 90 | 1.2432 | 1.1762 | 1.0744 | 0.9912 | 0.8406 | exploratory signal |
| FET/USDT | P8_200 | 45 | 1.2115 | 0.7046 | 1.1183 | 1.0215 | 0.9132 | exploratory signal |
| POL/USDT | P20_144 | 73 | 1.2058 | 0.9025 | 1.0009 | 0.9890 | 0.8035 | exploratory signal |
| APT/USDT | P26_200 | 80 | 1.2284 | 1.0173 | 1.0591 | 1.0097 | 0.8649 | exploratory signal |
| ENA/USDT | P20_200 | 106 | 1.2024 | 1.0480 | 1.0475 | 0.9190 | 0.8215 | exploratory signal |
| ENA/USDT | P8_144 | 123 | 1.2020 | 1.1170 | 1.0433 | 1.0576 | 0.9441 | exploratory signal |
| ZEN/USDT | P12_200 | 37 | 1.3991 | 1.1387 | 1.2442 | 1.0183 | 0.8795 | exploratory signal |

## Leg 3c — Why the exploratory signals did not promote

| Blocking gate | Cells |
|---|---|
| out-of-sample net PF still > 1 under 2x costs | 28 |
| full-sample net PF still > 1 under 2x costs | 108 |
| out-of-sample Sharpe > 0 | 0 |

## Leg 3d — Does the verdict depend on the out-of-sample window?

The closest survivors were re-verified at every window length. A cell that only looks good at one window length is an artifact of that choice.

| Symbol | Cell | OOS 20% PF / stress PF | OOS 35% PF / stress PF | OOS 50% PF / stress PF |
|---|---|---|---|---|
| DEXE/USDT | P55_200 | 2.0835 / 1.9031 | 1.9333 / 1.7085 | 1.5723 / 1.3263 |
| DEXE/USDT | P50_200 | 1.7249 / 1.5516 | 1.8239 / 1.6091 | 1.5032 / 1.2616 |
| DEXE/USDT | P89_200 | 1.7758 / 1.6233 | 1.7448 / 1.4799 | 1.2664 / 1.0176 |
| BRETT/USDT | P8_200 | 1.5857 / 1.4148 | 1.6888 / 1.5322 | 1.2354 / 1.1185 |
| DEXE/USDT | P21_200 | 1.3913 / 1.2679 | 1.3506 / 1.1946 | 1.5040 / 1.2870 |
| DEXE/USDT | P20_200 | 1.3915 / 1.2683 | 1.3381 / 1.1830 | 1.5091 / 1.2913 |
| DEXE/USDT | P100_200 | 1.8662 / 1.6677 | 1.6140 / 1.3617 | 1.1435 / 0.9129 |
| POL/USDT | P8_200 | 0.8469 / 0.7028 | 1.6086 / 1.3924 | 1.1234 / 0.9519 |
| XPR/USDT | P8_200 | 1.4808 / 1.2439 | 1.5261 / 1.3106 | 1.2379 / 1.0497 |
| FET/USDT | P12_200 | 1.4800 / 1.3441 | 1.5616 / 1.4404 | 1.3907 / 1.2499 |
| DEXE/USDT | P8_144 | 1.3602 / 1.2663 | 1.6286 / 1.4581 | 1.1530 / 0.9637 |
| DEXE/USDT | P55_144 | 1.1736 / 1.0371 | 1.4671 / 1.2660 | 1.1938 / 0.9510 |
| RUNE/USDT | P50_144 | 1.4362 / 1.0530 | 1.5230 / 1.1018 | 1.2827 / 0.9269 |
| FLUX/USDT | P8_200 | 1.9026 / 1.6374 | 1.2427 / 1.0272 | 1.1846 / 1.0013 |
| JASMY/USDT | P144_200 | 1.1520 / 0.8349 | 1.4928 / 1.0619 | 1.2866 / 0.9289 |
| ZEN/USDT | P8_200 | 1.1896 / 1.0147 | 1.6713 / 1.4974 | 1.1247 / 0.9986 |
| IMX/USDT | P26_200 | 1.3068 / 1.0439 | 1.4801 / 1.2246 | 1.3019 / 1.0879 |
| GMT/USDT | P8_200 | 1.0768 / 0.9140 | 1.4743 / 1.2697 | 1.1887 / 0.9993 |
| IMX/USDT | P50_55 | 0.7177 / 0.4594 | 1.4581 / 1.0113 | 1.6521 / 1.1875 |
| CETUS/USDT | P8_200 | 1.3014 / 1.1343 | 1.4174 / 1.2401 | 1.3585 / 1.1894 |
| DEXE/USDT | P50_144 | 1.2055 / 1.0648 | 1.4465 / 1.2581 | 1.1259 / 0.9329 |
| GRT/USDT | P20_200 | 1.2513 / 1.0435 | 1.3953 / 1.2070 | 1.1981 / 1.0263 |
| POL/USDT | P21_200 | 1.2883 / 1.0852 | 1.4246 / 1.2175 | 1.2338 / 1.0422 |
| DIA/USDT | P12_200 | 1.6330 / 1.3731 | 1.5029 / 1.2510 | 1.5013 / 1.2691 |
| DEXE/USDT | P12_200 | 1.1245 / 1.0255 | 1.3235 / 1.1782 | 1.3809 / 1.1540 |
| POL/USDT | P34_200 | 1.2127 / 0.9489 | 1.3951 / 1.1220 | 1.0744 / 0.8470 |
| ENA/USDT | P20_21 | 1.4238 / 1.0529 | 1.3902 / 1.0324 | 1.5055 / 1.1359 |
| POL/USDT | P26_200 | 1.0844 / 0.9066 | 1.3900 / 1.1701 | 1.0721 / 0.8920 |
| IMX/USDT | P12_200 | 1.4783 / 1.2163 | 1.4025 / 1.1843 | 1.2024 / 1.0210 |
| AVA/USDT | P50_200 | 1.4690 / 1.2293 | 1.3796 / 1.0947 | 1.1542 / 0.9191 |
| PUFFER/USDT | P20_200 | 1.2249 / 1.1155 | 1.4038 / 1.2514 | 1.4214 / 1.2723 |
| IMX/USDT | P34_200 | 1.2938 / 1.0318 | 1.3871 / 1.1430 | 1.2097 / 1.0073 |
| GRT/USDT | P8_200 | 0.9770 / 0.8147 | 1.2529 / 1.0880 | 1.0564 / 0.9188 |
| POL/USDT | P20_200 | 1.1598 / 0.9799 | 1.3597 / 1.1649 | 1.2471 / 1.0631 |
| DEXE/USDT | P8_200 | 1.1502 / 1.0704 | 1.2721 / 1.1409 | 1.2100 / 0.9979 |
| PUFFER/USDT | P21_200 | 1.2603 / 1.1470 | 1.3789 / 1.2253 | 1.3067 / 1.1541 |
| APT/USDT | P12_200 | 1.4887 / 1.2292 | 1.4641 / 1.2962 | 1.0507 / 0.9049 |
| ROSE/USDT | P34_200 | 1.0123 / 0.8248 | 1.3328 / 1.1197 | 1.2002 / 1.0180 |
| T/USDT | P12_200 | 1.5942 / 1.3770 | 1.3272 / 1.0559 | 0.7754 / 0.5778 |
| ROSE/USDT | P55_200 | 1.3066 / 1.0179 | 1.3264 / 1.0699 | 1.1950 / 0.9776 |
| RUNE/USDT | P50_200 | 1.3541 / 1.0299 | 1.3239 / 1.0085 | 1.2968 / 1.0120 |
| EGLD/USDT | P55_200 | 1.5506 / 1.2200 | 1.3233 / 1.0202 | 1.1107 / 0.8590 |
| DAG/USDT | P8_100 | 1.6037 / 1.3263 | 1.3177 / 1.0588 | 0.9778 / 0.8056 |
| WLD/USDT | P20_200 | 1.7616 / 1.5989 | 1.2811 / 1.1347 | 1.2516 / 1.1022 |
| DEXE/USDT | P12_144 | 1.4129 / 1.2961 | 1.2833 / 1.1198 | 1.1287 / 0.9344 |
| AVA/USDT | P34_200 | 1.2066 / 1.0171 | 1.3090 / 1.0465 | 1.1004 / 0.8802 |
| IMX/USDT | P20_200 | 1.3114 / 1.0660 | 1.3382 / 1.1116 | 1.2332 / 1.0291 |
| IMX/USDT | P8_200 | 1.3886 / 1.1443 | 1.2911 / 1.0899 | 1.3184 / 1.1300 |
| DIA/USDT | P21_200 | 2.0329 / 1.6635 | 1.3177 / 1.0516 | 1.2327 / 0.9955 |
| BLUR/USDT | P12_144 | 1.2764 / 1.0375 | 1.3406 / 1.1106 | 1.0083 / 0.8147 |
| COTI/USDT | P50_200 | 1.0187 / 0.8432 | 1.3026 / 1.0758 | 1.2881 / 1.0670 |
| PENDLE/USDT | P34_144 | 0.9883 / 0.7877 | 1.3020 / 1.0713 | 1.1006 / 0.9001 |
| WIN/USDT | P8_200 | 1.6909 / 1.4075 | 1.3047 / 1.0781 | 1.0841 / 0.8726 |
| DIA/USDT | P20_200 | 1.9955 / 1.6365 | 1.3064 / 1.0449 | 1.2043 / 0.9736 |
| COTI/USDT | P55_144 | 1.0722 / 0.8663 | 1.2911 / 1.0354 | 1.1690 / 0.9235 |
| BLUR/USDT | P8_200 | 1.3212 / 1.1147 | 1.3389 / 1.1488 | 1.2613 / 1.0849 |
| WIN/USDT | P12_200 | 1.9330 / 1.6034 | 1.2655 / 1.0384 | 1.0517 / 0.8379 |
| BLUR/USDT | P12_200 | 1.2160 / 1.0174 | 1.3084 / 1.1201 | 1.1416 / 0.9457 |
| CETUS/USDT | P12_200 | 1.0107 / 0.8909 | 1.2746 / 1.1338 | 1.1118 / 0.9812 |
| VELO/USDT | P12_200 | 1.2611 / 1.0920 | 1.2464 / 1.0736 | 1.1749 / 1.0201 |
| PUFFER/USDT | P26_200 | 1.0173 / 0.9208 | 1.2674 / 1.1275 | 1.2201 / 1.0799 |
| COTI/USDT | P50_144 | 1.1056 / 0.9033 | 1.2656 / 1.0217 | 1.1659 / 0.9293 |
| SYN/USDT | P20_200 | 1.4122 / 1.1998 | 1.2314 / 1.0362 | 0.9575 / 0.7946 |
| AVA/USDT | P26_200 | 1.1201 / 0.9702 | 1.2616 / 1.0338 | 1.0784 / 0.8763 |
| TWT/USDT | P8_200 | 1.3218 / 1.0752 | 1.2604 / 1.0098 | 1.0641 / 0.8334 |
| ENA/USDT | P34_144 | 1.1313 / 0.9452 | 1.2519 / 1.0600 | 1.1404 / 0.9701 |
| WLD/USDT | P21_200 | 1.6085 / 1.4621 | 1.2454 / 1.1074 | 1.1216 / 0.9841 |
| BRETT/USDT | P8_144 | 1.1722 / 1.0061 | 1.1688 / 1.0004 | 1.0560 / 0.9214 |
| DIA/USDT | P26_200 | 2.1903 / 1.8058 | 1.2789 / 1.0211 | 1.2825 / 1.0352 |
| BOME/USDT | P26_200 | 1.2228 / 1.0143 | 1.2403 / 1.0387 | 1.2579 / 1.0659 |
| DEXE/USDT | P26_200 | 0.9922 / 0.8948 | 1.2250 / 1.0851 | 1.2634 / 1.0802 |
| IMX/USDT | P50_200 | 1.1890 / 0.9455 | 1.2397 / 1.0091 | 1.0919 / 0.8936 |
| IMX/USDT | P21_200 | 1.2901 / 1.0457 | 1.2771 / 1.0591 | 1.1494 / 0.9607 |
| DEXE/USDT | P20_144 | 1.2817 / 1.1723 | 1.2489 / 1.0920 | 1.0647 / 0.8881 |
| DEXE/USDT | P8_100 | 1.2223 / 1.1237 | 1.2388 / 1.0877 | 0.9821 / 0.8018 |
| VELO/USDT | P20_200 | 1.3372 / 1.1556 | 1.2073 / 1.0416 | 1.0636 / 0.9191 |
| FET/USDT | P20_200 | 1.2493 / 1.1382 | 1.2336 / 1.1306 | 1.3515 / 1.1961 |
| AVA/USDT | P20_200 | 0.9722 / 0.8464 | 1.2326 / 1.0142 | 1.0428 / 0.8518 |
| AVA/USDT | P21_200 | 0.9719 / 0.8458 | 1.2324 / 1.0139 | 1.0660 / 0.8721 |
| BLUR/USDT | P8_144 | 1.2038 / 0.9817 | 1.2691 / 1.0464 | 1.0433 / 0.8547 |
| APT/USDT | P21_144 | 1.3262 / 1.1114 | 1.2517 / 1.0800 | 1.1400 / 0.9619 |
| DEXE/USDT | P34_144 | 0.9045 / 0.8122 | 1.2222 / 1.0649 | 1.0525 / 0.8688 |
| DIA/USDT | P8_200 | 1.3533 / 1.1377 | 1.2941 / 1.0808 | 1.2390 / 1.0472 |
| DEXE/USDT | P21_144 | 1.2828 / 1.1741 | 1.2278 / 1.0745 | 1.0224 / 0.8558 |
| MINA/USDT | P12_200 | 1.6691 / 1.4458 | 1.3342 / 1.1513 | 0.8882 / 0.7392 |
| APT/USDT | P20_144 | 1.3283 / 1.1143 | 1.2432 / 1.0744 | 1.0926 / 0.9172 |
| FET/USDT | P8_200 | 1.3388 / 1.2324 | 1.2115 / 1.1183 | 1.1842 / 1.0667 |
| POL/USDT | P20_144 | 0.8915 / 0.7141 | 1.2058 / 1.0009 | 1.0309 / 0.8552 |
| APT/USDT | P26_200 | 1.3231 / 1.1007 | 1.2284 / 1.0591 | 1.0484 / 0.8893 |
| ENA/USDT | P20_200 | 1.1742 / 1.0049 | 1.2024 / 1.0475 | 1.0171 / 0.8891 |
| ENA/USDT | P8_144 | 1.0318 / 0.8860 | 1.2020 / 1.0433 | 1.1452 / 1.0022 |
| ZEN/USDT | P12_200 | 0.9404 / 0.7905 | 1.3991 / 1.2442 | 1.0349 / 0.8920 |

| Symbol | Cell | OOS 20% trades | OOS 35% trades | OOS 50% trades |
|---|---|---|---|---|
| DEXE/USDT | P55_200 | 27 | 64 | 91 |
| DEXE/USDT | P50_200 | 30 | 71 | 100 |
| DEXE/USDT | P89_200 | 24 | 58 | 87 |
| BRETT/USDT | P8_200 | 38 | 45 | 77 |
| DEXE/USDT | P21_200 | 39 | 87 | 100 |
| DEXE/USDT | P20_200 | 39 | 89 | 103 |
| DEXE/USDT | P100_200 | 25 | 61 | 92 |
| POL/USDT | P8_200 | 18 | 52 | 95 |
| XPR/USDT | P8_200 | 29 | 46 | 97 |
| FET/USDT | P12_200 | 30 | 36 | 70 |
| DEXE/USDT | P8_144 | 38 | 92 | 126 |
| DEXE/USDT | P55_144 | 38 | 82 | 112 |
| RUNE/USDT | P50_144 | 76 | 120 | 171 |
| FLUX/USDT | P8_200 | 59 | 125 | 132 |
| JASMY/USDT | P144_200 | 31 | 56 | 72 |
| ZEN/USDT | P8_200 | 35 | 42 | 83 |
| IMX/USDT | P26_200 | 70 | 114 | 172 |
| GMT/USDT | P8_200 | 53 | 91 | 128 |
| IMX/USDT | P50_55 | 25 | 44 | 67 |
| CETUS/USDT | P8_200 | 37 | 86 | 119 |
| DEXE/USDT | P50_144 | 41 | 89 | 118 |
| GRT/USDT | P20_200 | 51 | 64 | 97 |
| POL/USDT | P21_200 | 34 | 71 | 102 |
| DIA/USDT | P12_200 | 65 | 90 | 103 |
| DEXE/USDT | P12_200 | 39 | 86 | 110 |
| POL/USDT | P34_200 | 52 | 95 | 140 |
| ENA/USDT | P20_21 | 29 | 46 | 63 |
| POL/USDT | P26_200 | 31 | 71 | 102 |
| IMX/USDT | P12_200 | 66 | 100 | 141 |
| AVA/USDT | P50_200 | 42 | 88 | 139 |
| PUFFER/USDT | P20_200 | 46 | 82 | 111 |
| IMX/USDT | P34_200 | 62 | 107 | 158 |
| GRT/USDT | P8_200 | 51 | 62 | 85 |
| POL/USDT | P20_200 | 32 | 69 | 95 |
| DEXE/USDT | P8_200 | 37 | 79 | 102 |
| PUFFER/USDT | P21_200 | 42 | 76 | 111 |
| APT/USDT | P12_200 | 40 | 38 | 83 |
| ROSE/USDT | P34_200 | 46 | 88 | 125 |
| T/USDT | P12_200 | 30 | 52 | 110 |
| ROSE/USDT | P55_200 | 73 | 112 | 150 |
| RUNE/USDT | P50_200 | 63 | 89 | 124 |
| EGLD/USDT | P55_200 | 55 | 99 | 144 |
| DAG/USDT | P8_100 | 67 | 109 | 197 |
| WLD/USDT | P20_200 | 56 | 100 | 128 |
| DEXE/USDT | P12_144 | 39 | 97 | 130 |
| AVA/USDT | P34_200 | 41 | 97 | 158 |
| IMX/USDT | P20_200 | 72 | 129 | 169 |
| IMX/USDT | P8_200 | 66 | 100 | 136 |
| DIA/USDT | P21_200 | 63 | 126 | 145 |
| BLUR/USDT | P12_144 | 75 | 116 | 144 |
| COTI/USDT | P50_200 | 60 | 99 | 144 |
| PENDLE/USDT | P34_144 | 80 | 98 | 154 |
| WIN/USDT | P8_200 | 69 | 107 | 137 |
| DIA/USDT | P20_200 | 62 | 128 | 148 |
| COTI/USDT | P55_144 | 68 | 112 | 167 |
| BLUR/USDT | P8_200 | 65 | 88 | 97 |
| WIN/USDT | P12_200 | 63 | 98 | 138 |
| BLUR/USDT | P12_200 | 60 | 90 | 120 |
| CETUS/USDT | P12_200 | 36 | 68 | 108 |
| VELO/USDT | P12_200 | 66 | 115 | 160 |
| PUFFER/USDT | P26_200 | 44 | 75 | 114 |
| COTI/USDT | P50_144 | 71 | 115 | 173 |
| SYN/USDT | P20_200 | 66 | 100 | 169 |
| AVA/USDT | P26_200 | 41 | 99 | 162 |
| TWT/USDT | P8_200 | 38 | 73 | 109 |
| ENA/USDT | P34_144 | 72 | 111 | 165 |
| WLD/USDT | P21_200 | 61 | 103 | 141 |
| BRETT/USDT | P8_144 | 66 | 92 | 119 |
| DIA/USDT | P26_200 | 59 | 116 | 144 |
| BOME/USDT | P26_200 | 67 | 112 | 152 |
| DEXE/USDT | P26_200 | 41 | 85 | 93 |
| IMX/USDT | P50_200 | 63 | 102 | 159 |
| IMX/USDT | P21_200 | 74 | 118 | 160 |
| DEXE/USDT | P20_144 | 37 | 98 | 130 |
| DEXE/USDT | P8_100 | 43 | 119 | 202 |
| VELO/USDT | P20_200 | 66 | 108 | 163 |
| FET/USDT | P20_200 | 32 | 34 | 80 |
| AVA/USDT | P20_200 | 44 | 105 | 163 |
| AVA/USDT | P21_200 | 44 | 105 | 165 |
| BLUR/USDT | P8_144 | 85 | 123 | 146 |
| APT/USDT | P21_144 | 50 | 97 | 149 |
| DEXE/USDT | P34_144 | 39 | 88 | 137 |
| DIA/USDT | P8_200 | 71 | 95 | 109 |
| DEXE/USDT | P21_144 | 37 | 97 | 127 |
| MINA/USDT | P12_200 | 53 | 74 | 137 |
| APT/USDT | P20_144 | 50 | 94 | 148 |
| FET/USDT | P8_200 | 33 | 45 | 80 |
| POL/USDT | P20_144 | 35 | 73 | 109 |
| APT/USDT | P26_200 | 50 | 81 | 126 |
| ENA/USDT | P20_200 | 65 | 106 | 146 |
| ENA/USDT | P8_144 | 76 | 123 | 172 |
| ZEN/USDT | P12_200 | 29 | 38 | 94 |

## Leg 4 — Selection-bias check against the in-sample winners

| Population | Cells | Out-of-sample PF > 1 | With enough OOS trades | Survive the full §3.4 gate |
|---|---|---|---|---|
| in-sample net PF > 1 (checked by the pipeline) | 287 | 132 | 128 | 9 |
| all cells | 17556 | 608 | 591 | 9 |

## Gates (PROMPT.md §3.3, §3.4)

- Grid cells evaluated out of sample: **17556** (the pipeline had only checked 287).
- Credible candidates found anywhere in the grid: **9**.
- Exploratory signals found anywhere in the grid: **111**.
- Screen survivors verified with a real backtest: **120**.

# Survivor Selection Audit — EMA Hourly Continuation

**Source run:** `results/20261021_172619_grid`
**Out-of-sample audit:** `results/20261022_013800_child_oos_grid_scan`
**Generated:** 2026-10-22T02:24:26.382717+00:00
**Universe:** 266 symbols, 17556 grid cells
**Cost model:** 10.0 bps taker + 2.0 bps slippage per side (stress leg: 2x)

## Why this leg exists

Ten cells out of 17 556 clear the out-of-sample gate. The program decision rests on them, and two questions about that set were still open: is the family a property of the rule or of the one or two symbols it sits on, and does the *selection* survive a walk-forward that never shows the selection the data it is scored on.

## Leg 1 — the family

| Symbol | Cell | OOS trades | OOS net PF | OOS PF (2x costs) | Full-sample net PF | Exact OOS PF | Exact OOS PF (2x) |
|---|---|---|---|---|---|---|---|
| DEXE/USDT | P55_200 | 63 | 1.8907 | 1.6783 | 0.9677 | 1.9333 | 1.7085 |
| DEXE/USDT | P50_200 | 70 | 1.7875 | 1.5833 | 1.0694 | 1.8239 | 1.6091 |
| DEXE/USDT | P89_200 | 56 | 1.7875 | 1.5267 | 0.8904 | 1.7448 | 1.4799 |
| BRETT/USDT | P8_200 | 42 | 1.6802 | 1.5168 | 1.0449 | 1.6888 | 1.5322 |
| DEXE/USDT | P21_200 | 64 | 1.6713 | 1.5219 | 0.9970 | 1.3506 | 1.1946 |
| DEXE/USDT | P20_200 | 66 | 1.6404 | 1.4926 | 0.9864 | 1.3381 | 1.1830 |
| DEXE/USDT | P100_200 | 61 | 1.6140 | 1.3740 | 0.8062 | 1.6140 | 1.3617 |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.3857 | 1.1216 | 1.6086 | 1.3924 |
| XPR/USDT | P8_200 | 44 | 1.5710 | 1.3538 | 0.9178 | 1.5261 | 1.3106 |
| FET/USDT | P12_200 | 36 | 1.5616 | 1.4435 | 1.0341 | 1.5616 | 1.4404 |
| DEXE/USDT | P8_144 | 83 | 1.5518 | 1.4012 | 0.9214 | 1.6286 | 1.4581 |
| DEXE/USDT | P55_144 | 76 | 1.5373 | 1.3363 | 0.8847 | 1.4671 | 1.2660 |
| RUNE/USDT | P50_144 | 120 | 1.5230 | 1.0963 | 0.9328 | 1.5230 | 1.1018 |
| FLUX/USDT | P8_200 | 93 | 1.5170 | 1.2910 | 1.2228 | 1.2427 | 1.0272 |
| JASMY/USDT | P144_200 | 56 | 1.4928 | 1.0550 | 1.0245 | 1.4928 | 1.0619 |
| ZEN/USDT | P8_200 | 33 | 1.4808 | 1.3582 | 1.2569 | 1.6713 | 1.4974 |
| IMX/USDT | P26_200 | 114 | 1.4801 | 1.2167 | 1.1185 | 1.4801 | 1.2246 |
| GMT/USDT | P8_200 | 88 | 1.4737 | 1.2727 | 0.9866 | 1.4743 | 1.2697 |
| CETUS/USDT | P8_200 | 85 | 1.4565 | 1.2715 | 1.2740 | 1.4174 | 1.2401 |
| DEXE/USDT | P50_144 | 89 | 1.4465 | 1.2605 | 0.8699 | 1.4465 | 1.2581 |
| GRT/USDT | P20_200 | 57 | 1.4433 | 1.2623 | 1.1087 | 1.3953 | 1.2070 |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.2155 | 1.0354 | 1.4246 | 1.2175 |
| DIA/USDT | P12_200 | 84 | 1.4204 | 1.1836 | 1.1315 | 1.5029 | 1.2510 |
| DEXE/USDT | P12_200 | 65 | 1.3968 | 1.2667 | 1.0165 | 1.3235 | 1.1782 |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.1151 | 1.0278 | 1.3951 | 1.1220 |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.0315 | 1.3253 | 1.3902 | 1.0324 |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.1647 | 0.9932 | 1.3900 | 1.1701 |
| IMX/USDT | P12_200 | 94 | 1.3886 | 1.1734 | 0.9999 | 1.4025 | 1.1843 |
| AVA/USDT | P50_200 | 88 | 1.3796 | 1.0974 | 0.9483 | 1.3796 | 1.0947 |
| PUFFER/USDT | P20_200 | 81 | 1.3768 | 1.2245 | 1.1884 | 1.4038 | 1.2514 |
| IMX/USDT | P34_200 | 101 | 1.3729 | 1.1217 | 1.1547 | 1.3871 | 1.1430 |
| GRT/USDT | P8_200 | 57 | 1.3602 | 1.2002 | 0.9520 | 1.2529 | 1.0880 |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.1617 | 1.0429 | 1.3597 | 1.1649 |
| DEXE/USDT | P8_200 | 56 | 1.3520 | 1.2415 | 0.9059 | 1.2721 | 1.1409 |
| PUFFER/USDT | P21_200 | 75 | 1.3497 | 1.1974 | 1.1333 | 1.3789 | 1.2253 |
| APT/USDT | P12_200 | 36 | 1.3367 | 1.1823 | 1.0656 | 1.4641 | 1.2962 |
| ROSE/USDT | P34_200 | 88 | 1.3328 | 1.1080 | 1.0394 | 1.3328 | 1.1197 |
| T/USDT | P12_200 | 52 | 1.3272 | 1.0711 | 0.9175 | 1.3272 | 1.0559 |
| ROSE/USDT | P55_200 | 112 | 1.3264 | 1.0651 | 1.0227 | 1.3264 | 1.0699 |
| RUNE/USDT | P50_200 | 89 | 1.3239 | 1.0048 | 1.0682 | 1.3239 | 1.0085 |
| EGLD/USDT | P55_200 | 99 | 1.3233 | 1.0262 | 0.8953 | 1.3233 | 1.0202 |
| DAG/USDT | P8_100 | 109 | 1.3177 | 1.0644 | 0.7768 | 1.3177 | 1.0588 |
| WLD/USDT | P20_200 | 94 | 1.3171 | 1.1761 | 1.1725 | 1.2811 | 1.1347 |
| DEXE/USDT | P12_144 | 88 | 1.3128 | 1.1594 | 0.9756 | 1.2833 | 1.1198 |
| AVA/USDT | P34_200 | 97 | 1.3090 | 1.0502 | 0.8734 | 1.3090 | 1.0465 |
| IMX/USDT | P20_200 | 122 | 1.3057 | 1.0826 | 1.1008 | 1.3382 | 1.1116 |
| IMX/USDT | P8_200 | 93 | 1.3049 | 1.1024 | 1.2102 | 1.2911 | 1.0899 |
| DIA/USDT | P21_200 | 120 | 1.3037 | 1.0515 | 0.9699 | 1.3177 | 1.0516 |
| BLUR/USDT | P12_144 | 103 | 1.3034 | 1.0910 | 1.0281 | 1.3406 | 1.1106 |
| COTI/USDT | P50_200 | 99 | 1.3026 | 1.0675 | 1.0597 | 1.3026 | 1.0758 |
| PENDLE/USDT | P34_144 | 98 | 1.3020 | 1.0650 | 0.8413 | 1.3020 | 1.0713 |
| WIN/USDT | P8_200 | 104 | 1.2949 | 1.0848 | 1.0109 | 1.3047 | 1.0781 |
| DIA/USDT | P20_200 | 122 | 1.2927 | 1.0444 | 0.9440 | 1.3064 | 1.0449 |
| COTI/USDT | P55_144 | 112 | 1.2911 | 1.0220 | 0.8966 | 1.2911 | 1.0354 |
| SUPER/USDT | P8_200 | 64 | 1.2855 | 1.0890 | 1.1941 | 1.1483 | 0.9667 |
| BLUR/USDT | P8_200 | 83 | 1.2799 | 1.0998 | 1.1877 | 1.3389 | 1.1488 |
| WIN/USDT | P12_200 | 96 | 1.2759 | 1.0616 | 0.8747 | 1.2655 | 1.0384 |
| BLUR/USDT | P12_200 | 86 | 1.2755 | 1.0907 | 1.0764 | 1.3084 | 1.1201 |
| CETUS/USDT | P12_200 | 68 | 1.2746 | 1.1305 | 1.2391 | 1.2746 | 1.1338 |
| VELO/USDT | P12_200 | 114 | 1.2723 | 1.1009 | 0.9932 | 1.2464 | 1.0736 |
| PUFFER/USDT | P26_200 | 75 | 1.2674 | 1.1244 | 1.0037 | 1.2674 | 1.1275 |
| COTI/USDT | P50_144 | 115 | 1.2656 | 1.0100 | 0.8727 | 1.2656 | 1.0217 |
| SYN/USDT | P20_200 | 99 | 1.2628 | 1.0678 | 0.9918 | 1.2314 | 1.0362 |
| AVA/USDT | P26_200 | 99 | 1.2616 | 1.0341 | 0.8463 | 1.2616 | 1.0338 |
| TWT/USDT | P8_200 | 73 | 1.2604 | 1.0174 | 0.8890 | 1.2604 | 1.0098 |
| ENA/USDT | P34_144 | 111 | 1.2519 | 1.0555 | 0.9014 | 1.2519 | 1.0600 |
| WLD/USDT | P21_200 | 103 | 1.2454 | 1.1119 | 1.0863 | 1.2454 | 1.1074 |
| BRETT/USDT | P8_144 | 78 | 1.2444 | 1.0708 | 0.8902 | 1.1688 | 1.0004 |
| DIA/USDT | P26_200 | 114 | 1.2413 | 1.0018 | 0.9740 | 1.2789 | 1.0211 |
| BOME/USDT | P26_200 | 112 | 1.2403 | 1.0411 | 0.9895 | 1.2403 | 1.0387 |
| DEXE/USDT | P26_200 | 63 | 1.2401 | 1.1233 | 0.9471 | 1.2250 | 1.0851 |
| IMX/USDT | P50_200 | 102 | 1.2397 | 1.0012 | 1.0175 | 1.2397 | 1.0091 |
| CHZ/USDT | P8_200 | 66 | 1.2395 | 1.0876 | 0.9348 | 1.1137 | 0.9676 |
| IMX/USDT | P21_200 | 111 | 1.2394 | 1.0252 | 1.0431 | 1.2771 | 1.0591 |
| DEXE/USDT | P20_144 | 90 | 1.2391 | 1.0938 | 0.9166 | 1.2489 | 1.0920 |
| DEXE/USDT | P8_100 | 114 | 1.2379 | 1.0947 | 0.9076 | 1.2388 | 1.0877 |
| VELO/USDT | P20_200 | 107 | 1.2339 | 1.0705 | 0.9855 | 1.2073 | 1.0416 |
| FET/USDT | P20_200 | 34 | 1.2336 | 1.1324 | 1.0236 | 1.2336 | 1.1306 |
| AVA/USDT | P20_200 | 105 | 1.2326 | 1.0120 | 0.8490 | 1.2326 | 1.0142 |
| AVA/USDT | P21_200 | 105 | 1.2324 | 1.0117 | 0.8316 | 1.2324 | 1.0139 |
| BLUR/USDT | P8_144 | 112 | 1.2248 | 1.0202 | 1.0347 | 1.2691 | 1.0464 |
| GMT/USDT | P8_144 | 110 | 1.2242 | 1.0183 | 0.9924 | 1.1404 | 0.9364 |
| APT/USDT | P21_144 | 93 | 1.2226 | 1.0567 | 1.0362 | 1.2517 | 1.0800 |
| DEXE/USDT | P34_144 | 88 | 1.2222 | 1.0632 | 0.9170 | 1.2222 | 1.0649 |
| DIA/USDT | P8_200 | 89 | 1.2169 | 1.0141 | 1.0236 | 1.2941 | 1.0808 |
| DEXE/USDT | P21_144 | 89 | 1.2166 | 1.0751 | 0.9016 | 1.2278 | 1.0745 |
| MINA/USDT | P12_200 | 75 | 1.2162 | 1.0532 | 0.9442 | 1.3342 | 1.1513 |
| W/USDT | P12_200 | 80 | 1.2138 | 1.0512 | 0.9956 | 1.0902 | 0.9214 |
| APT/USDT | P20_144 | 90 | 1.2129 | 1.0507 | 0.9912 | 1.2432 | 1.0744 |
| FET/USDT | P8_200 | 45 | 1.2115 | 1.1200 | 1.0215 | 1.2115 | 1.1183 |
| APT/USDT | P26_200 | 80 | 1.2029 | 1.0384 | 1.0097 | 1.2284 | 1.0591 |
| ENA/USDT | P20_200 | 106 | 1.2024 | 1.0479 | 0.9190 | 1.2024 | 1.0475 |
| ENA/USDT | P8_144 | 123 | 1.2020 | 1.0456 | 1.0576 | 1.2020 | 1.0433 |
| ZEN/USDT | P12_200 | 37 | 1.2002 | 1.0623 | 1.0183 | 1.3991 | 1.2442 |
| RENDER/USDT | P8_200 | 45 | 1.1898 | 1.0722 | 0.9713 | 1.1898 | 1.0727 |
| BLUR/USDT | P21_200 | 90 | 1.1885 | 1.0111 | 1.0199 | 1.1885 | 1.0125 |
| DEXE/USDT | P12_100 | 112 | 1.1871 | 1.0349 | 0.9157 | 1.1871 | 1.0307 |
| MEW/USDT | P8_200 | 49 | 1.1845 | 1.0103 | 0.9308 | 0.9391 | 0.7965 |
| GMT/USDT | P12_200 | 83 | 1.1827 | 1.0090 | 0.9341 | 1.1693 | 0.9985 |
| PYTH/USDT | P8_200 | 82 | 1.1827 | 1.0553 | 1.0817 | 1.1983 | 1.0603 |
| ROSE/USDT | P12_200 | 55 | 1.1550 | 1.0027 | 0.9313 | 1.3298 | 1.1638 |
| SYN/USDT | P26_200 | 91 | 1.1537 | 1.0032 | 0.9780 | 1.1537 | 1.0030 |
| ENA/USDT | P21_200 | 101 | 1.1506 | 1.0041 | 0.8941 | 1.1506 | 1.0043 |
| APT/USDT | P12_144 | 86 | 1.1429 | 1.0090 | 0.9400 | 1.1795 | 1.0375 |
| AERO/USDT | P12_200 | 79 | 1.1392 | 1.0084 | 1.1454 | 1.1491 | 1.0137 |
| FET/USDT | P21_200 | 39 | 1.1274 | 1.0389 | 1.0077 | 1.1274 | 1.0368 |

Pooled over the family: net PF **1.3110**, under 2x costs **1.1123**, net P&L 108,189. The family sits on 39 symbols: AERO/USDT, APT/USDT, AVA/USDT, BLUR/USDT, BOME/USDT, BRETT/USDT, CETUS/USDT, CHZ/USDT, COTI/USDT, DAG/USDT, DEXE/USDT, DIA/USDT, EGLD/USDT, ENA/USDT, FET/USDT, FLUX/USDT, GMT/USDT, GRT/USDT, IMX/USDT, JASMY/USDT, MEW/USDT, MINA/USDT, PENDLE/USDT, POL/USDT, PUFFER/USDT, PYTH/USDT, RENDER/USDT, ROSE/USDT, RUNE/USDT, SUPER/USDT, SYN/USDT, T/USDT, TWT/USDT, VELO/USDT, W/USDT, WIN/USDT, WLD/USDT, XPR/USDT, ZEN/USDT.

| Symbol | Family cells | Family trades | Share of the family net P&L | Pooled net PF | Pooled net PF (2x) |
|---|---|---|---|---|---|
| AERO/USDT | 1 | 79 | 0.6% | 1.1392 | 1.0084 |
| APT/USDT | 5 | 385 | 3.2% | 1.2099 | 1.0529 |
| AVA/USDT | 5 | 494 | 4.2% | 1.2814 | 1.0404 |
| BLUR/USDT | 5 | 474 | 5.0% | 1.2535 | 1.0609 |
| BOME/USDT | 1 | 112 | 1.0% | 1.2403 | 1.0411 |
| BRETT/USDT | 2 | 120 | 1.6% | 1.3967 | 1.2247 |
| CETUS/USDT | 2 | 153 | 2.7% | 1.3703 | 1.2047 |
| CHZ/USDT | 1 | 66 | 0.5% | 1.2395 | 1.0876 |
| COTI/USDT | 3 | 326 | 3.3% | 1.2871 | 1.0345 |
| DAG/USDT | 1 | 109 | 0.7% | 1.3177 | 1.0644 |
| DEXE/USDT | 18 | 1393 | 18.3% | 1.4161 | 1.2543 |
| DIA/USDT | 5 | 529 | 5.5% | 1.2926 | 1.0559 |
| EGLD/USDT | 1 | 99 | 1.0% | 1.3233 | 1.0262 |
| ENA/USDT | 5 | 487 | 4.0% | 1.2222 | 1.0385 |
| FET/USDT | 4 | 154 | 1.6% | 1.2652 | 1.1669 |
| FLUX/USDT | 1 | 93 | 2.0% | 1.5170 | 1.2910 |
| GMT/USDT | 3 | 281 | 2.9% | 1.2829 | 1.0878 |
| GRT/USDT | 2 | 114 | 1.7% | 1.4045 | 1.2333 |
| IMX/USDT | 7 | 737 | 9.9% | 1.3314 | 1.1012 |
| JASMY/USDT | 1 | 56 | 0.9% | 1.4928 | 1.0550 |
| MEW/USDT | 1 | 49 | 0.3% | 1.1845 | 1.0103 |
| MINA/USDT | 1 | 75 | 0.6% | 1.2162 | 1.0532 |
| PENDLE/USDT | 1 | 98 | 0.8% | 1.3020 | 1.0650 |
| POL/USDT | 5 | 358 | 5.6% | 1.4250 | 1.1938 |
| PUFFER/USDT | 3 | 231 | 3.3% | 1.3343 | 1.1847 |
| PYTH/USDT | 1 | 82 | 0.6% | 1.1827 | 1.0553 |
| RENDER/USDT | 1 | 45 | 0.3% | 1.1898 | 1.0722 |
| ROSE/USDT | 3 | 255 | 2.9% | 1.2913 | 1.0669 |
| RUNE/USDT | 2 | 209 | 2.9% | 1.4221 | 1.0502 |
| SUPER/USDT | 1 | 64 | 0.9% | 1.2855 | 1.0890 |
| SYN/USDT | 2 | 190 | 1.5% | 1.2082 | 1.0356 |
| T/USDT | 1 | 52 | 0.6% | 1.3272 | 1.0711 |
| TWT/USDT | 1 | 73 | 0.6% | 1.2604 | 1.0174 |
| VELO/USDT | 2 | 221 | 2.0% | 1.2536 | 1.0861 |
| W/USDT | 1 | 80 | 0.7% | 1.2138 | 1.0512 |
| WIN/USDT | 2 | 200 | 1.9% | 1.2866 | 1.0746 |
| WLD/USDT | 2 | 197 | 2.3% | 1.2804 | 1.1433 |
| XPR/USDT | 1 | 44 | 0.7% | 1.5710 | 1.3538 |
| ZEN/USDT | 2 | 70 | 0.9% | 1.3296 | 1.1980 |

## Leg 2 — leave-one-symbol-out

Every symbol of the family is dropped in turn. The gate family loses that symbol's cells; the ranked family is re-selected from the remaining cells, so the cells that would replace them are visible.

| Dropped symbol | Cells dropped | Family cells left | Pooled net PF without it | Pooled net PF (2x) without it | Ranked family: original cells kept | Newcomers | Newcomers that clear the gate | Ranked family net PF | Ranked family net PF (2x) | Ranked family clears the gates |
|---|---|---|---|---|---|---|---|---|---|---|
| AERO/USDT | 1 | 105 | 1.3132 | 1.1136 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| APT/USDT | 5 | 101 | 1.3160 | 1.1152 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| AVA/USDT | 5 | 101 | 1.3124 | 1.1158 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| BLUR/USDT | 5 | 101 | 1.3147 | 1.1156 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| BOME/USDT | 1 | 105 | 1.3119 | 1.1132 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| BRETT/USDT | 2 | 104 | 1.3099 | 1.1108 | 10 | 0 | 0 | 1.6689 | 1.4785 | yes |
| CETUS/USDT | 2 | 104 | 1.3096 | 1.1101 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| CHZ/USDT | 1 | 105 | 1.3115 | 1.1124 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| COTI/USDT | 3 | 103 | 1.3119 | 1.1152 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| DAG/USDT | 1 | 105 | 1.3109 | 1.1126 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| DEXE/USDT | 18 | 88 | 1.2944 | 1.0902 | 10 | 0 | 0 | 1.5245 | 1.2618 | yes |
| DIA/USDT | 5 | 101 | 1.3121 | 1.1158 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| EGLD/USDT | 1 | 105 | 1.3109 | 1.1131 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| ENA/USDT | 5 | 101 | 1.3162 | 1.1166 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| FET/USDT | 4 | 102 | 1.3119 | 1.1113 | 10 | 0 | 0 | 1.6770 | 1.4838 | yes |
| FLUX/USDT | 1 | 105 | 1.3085 | 1.1101 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| GMT/USDT | 3 | 103 | 1.3119 | 1.1131 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| GRT/USDT | 2 | 104 | 1.3097 | 1.1107 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| IMX/USDT | 7 | 99 | 1.3089 | 1.1134 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| JASMY/USDT | 1 | 105 | 1.3099 | 1.1126 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| MEW/USDT | 1 | 105 | 1.3117 | 1.1129 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| MINA/USDT | 1 | 105 | 1.3118 | 1.1127 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| PENDLE/USDT | 1 | 105 | 1.3111 | 1.1127 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| POL/USDT | 5 | 101 | 1.3061 | 1.1088 | 10 | 0 | 0 | 1.6768 | 1.4925 | yes |
| PUFFER/USDT | 3 | 103 | 1.3103 | 1.1100 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| PYTH/USDT | 1 | 105 | 1.3123 | 1.1129 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| RENDER/USDT | 1 | 105 | 1.3117 | 1.1125 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| ROSE/USDT | 3 | 103 | 1.3116 | 1.1137 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| RUNE/USDT | 2 | 104 | 1.3086 | 1.1137 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| SUPER/USDT | 1 | 105 | 1.3112 | 1.1125 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| SYN/USDT | 2 | 104 | 1.3134 | 1.1141 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| T/USDT | 1 | 105 | 1.3109 | 1.1125 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| TWT/USDT | 1 | 105 | 1.3113 | 1.1130 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| VELO/USDT | 2 | 104 | 1.3125 | 1.1129 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| W/USDT | 1 | 105 | 1.3119 | 1.1129 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| WIN/USDT | 2 | 104 | 1.3115 | 1.1131 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| WLD/USDT | 2 | 104 | 1.3118 | 1.1115 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |
| XPR/USDT | 1 | 105 | 1.3099 | 1.1113 | 10 | 0 | 0 | 1.6769 | 1.4908 | yes |
| ZEN/USDT | 2 | 104 | 1.3108 | 1.1115 | 10 | 0 | 0 | 1.6862 | 1.4924 | yes |


## Leg 3 — walk-forward re-selection over the whole grid

The full sample of every symbol is cut into 5 sequential folds. At step k the best cell of the symbol is chosen on the history (folds 1..k, at least 20 trades) and scored on fold k+1, which the selection never saw. Every cell of the grid takes part; nothing is selected in advance.

| Step (history -> test fold) | Symbols scored | Steps with a selection | Out-of-fold PF > 1 | Pooled out-of-fold net PF | Pooled out-of-fold net PF (2x) | Median in-fold net PF |
|---|---|---|---|---|---|---|
| 1 -> 2 | 266 | 266 | 67 (25.2%) | 0.8134 | 0.6641 | 1.2832 |
| 2 -> 3 | 266 | 266 | 40 (15.0%) | 0.7358 | 0.5723 | 1.1640 |
| 3 -> 4 | 266 | 266 | 39 (14.7%) | 0.7045 | 0.5316 | 1.0332 |
| 4 -> 5 | 266 | 266 | 29 (11.0%) | 0.6998 | 0.5240 | 0.9671 |

| Pooled over every step | Value |
|---|---|
| Walk-forward steps scored | 1061 |
| Out-of-fold trades | 60853 |
| Pooled out-of-fold net PF | 0.7390 |
| Pooled out-of-fold net PF (2x costs) | 0.5731 |
| Out-of-fold windows with net PF > 1 | 175 (16.5%) |
| Out-of-fold windows with net PF > 1 under 2x costs | 84 (7.9%) |
| Median in-fold net PF of the selected cell | 1.0906 |
| Median out-of-fold net PF of the selected cell | 0.7347 |

### Leg 3b — the selected cells against the grid's own null

The null needs no randomization: the grid itself holds 17 556 draws of what a cell scores on a fold it was not selected on. If the selection carries information, the selected cells have to sit at the top of that distribution; if it does not, they sit where a random cell would.

| Step | Null cells | Null median PF | Null mean PF | Null share above PF 1 | Null p95 | Selected cells above the null p95 |
|---|---|---|---|---|---|---|
| 1 -> 2 | 17556 | 0.7843 | 0.8123 | 17.0% | 1.2155 | 67 / 266 |
| 2 -> 3 | 17518 | 0.7175 | 0.7379 | 10.2% | 1.1190 | 40 / 266 |
| 3 -> 4 | 17487 | 0.6730 | 0.6978 | 8.7% | 1.0953 | 39 / 265 |
| 4 -> 5 | 17428 | 0.6376 | 0.6566 | 6.6% | 1.0497 | 29 / 264 |

| Measure | Value |
|---|---|
| Selected cells scored | 1059 |
| Median percentile of the selected cells in the null distribution | 0.5565 |
| Selected cells above the null 95th percentile | 106 (10.0%) |
| Expected under a null pick | 53.0 |
| One-sided exact binomial p-value, P(X >= observed) | 2.241e-11 |

## Leg 4 — sub-period stability of the closest survivors

The out-of-sample window of the 6 closest survivors is cut into 4 sequential sub-periods. An edge that is real has to show up in more than one of them.

| Symbol | Cell | PF sub 1 | PF sub 2 | PF sub 3 | PF sub 4 | Sub-periods with PF > 1 | Sub-periods with PF > 1 (2x costs) | Sub-periods with trades |
|---|---|---|---|---|---|---|---|---|
| BRETT/USDT | P8_200 | 2.8570 | 3.8129 | 2.8337 | 1.0211 | 4/4 | 3/4 | 4/4 |
| DEXE/USDT | P50_200 | 0.8933 | 4.4048 | 1.7020 | n/a | 2/3 | 2/3 | 3/4 |
| DEXE/USDT | P55_200 | 0.9742 | 4.4942 | 2.1685 | n/a | 2/3 | 2/3 | 3/4 |
| GRT/USDT | P20_200 | 2.0350 | inf | 1.5663 | 1.0537 | 4/4 | 3/4 | 4/4 |
| MERL/USDT | P8_200 | 1.5734 | n/a | n/a | n/a | 1/1 | 1/1 | 1/4 |
| ZEN/USDT | P12_200 | 1.7836 | 0.8267 | 0.7206 | 1.4530 | 2/4 | 2/4 | 4/4 |

A sub-period without a single trade has no profit factor: it is missing evidence, not a loss. The last column therefore shows how many of the sub-periods carry any trades at all.

The sub-periods are thin: the median sub-period of the closest survivors holds 18 trades, so this leg reads the stability of the edge, not its size.

| Symbol | Cell | Trades per sub-period |
|---|---|---|
| BRETT/USDT | P8_200 | 8, 5, 8, 21 |
| DEXE/USDT | P50_200 | 25, 24, 21, 0 |
| DEXE/USDT | P55_200 | 24, 18, 21, 0 |
| GRT/USDT | P20_200 | 13, 1, 20, 23 |
| MERL/USDT | P8_200 | 22, 0, 0, 0 |
| ZEN/USDT | P12_200 | 18, 4, 11, 4 |

## Verdict

- The 106-cell survivor family is concentrated in 39 symbols; dropping the dominant symbol leaves 88 of the 106 cells.
- Re-selecting the family from the remaining cells keeps 10-10 of the original cells, so the family is stable under a leave-one-symbol-out.
- Walk-forward: the procedure picks a cell on the history (median in-fold net PF 1.0906) and the same cell nets a median out-of-fold PF of 0.7347; the pooled out-of-fold net PF is 0.7390 over 60853 trades, and 16.5% of the out-of-fold windows land above PF 1 against the 10.6% the grid's own null produces on the same folds.
- The selected cells rank at a median of the 0.5565 percentile of that null, and 106 of 1059 beat its 95th percentile (one-sided exact binomial p 2.241e-11): the selection does rank the cells, it just never ranks one into a net-profitable window.
- Sub-period stability: 2 of 6 closest survivors keep PF above 1 in every out-of-sample sub-period that carries trades.
- The out-of-sample gate is measuring a window, not a rule: the survivors do not survive their own walk-forward, and the family collapses onto a handful of symbols.

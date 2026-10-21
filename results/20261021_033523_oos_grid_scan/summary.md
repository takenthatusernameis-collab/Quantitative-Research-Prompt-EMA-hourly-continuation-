# Grid-Wide Out-of-Sample Audit — EMA Hourly Continuation

**Source run:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T03:44:37.205152+00:00
**Universe:** 266 symbols, 17556 grid cells
**OOS window:** trailing 35% of each symbol's bars, entries restricted to the window
**Cost stress:** 2x fees and slippage (base 10 bps taker + 2 bps slippage per side)

## Why this leg exists

The pipeline's OOS gate was only ever applied to the 36 cells whose *in-sample* net PF exceeded 1. This leg applies the same out-of-sample window to all 17556 cells, so a cell whose in-sample window was unlucky cannot hide a survivor from the program.

## Leg 1 — Out-of-sample coverage

| Metric | Value |
|---|---|
| Cells screened | 17556 |
| Cells with at least one out-of-sample trade | 17491 |
| Cells with no out-of-sample trade | 65 |
| Cells with at least 30 out-of-sample trades | 17447 |
| Pooled out-of-sample net PF (all cells) | 0.5298 |
| Pooled out-of-sample net PF under 2x costs | 0.3266 |
| Pooled out-of-sample net P&L | -21837844 |
| Cells whose blotter net PF disagrees with the stored summary | 0 |
| Cells read from the legacy uncompressed blotter layout | 330 |

## Leg 2 — Out-of-sample net PF across the whole grid

| Statistic | Out-of-sample net PF | In-sample net PF |
|---|---|---|
| cells with a defined net PF | 17491 | 17556 |
| mean | 0.4319 | 0.4993 |
| median | 0.4342 | 0.5205 |
| p05 | 0.1446 | 0.1881 |
| p25 | 0.3060 | 0.3848 |
| p75 | 0.5463 | 0.6223 |
| p95 | 0.7201 | 0.7451 |
| max | 1.9955 | 2.2274 |

The 65 cells without a single out-of-sample trade are missing evidence, not a loss, and are excluded from the distribution.

- Cells with out-of-sample net PF > 1: **77** of 17556 (0.44%).
- Expected under a no-edge null: ~50% (excess -0.4956).
- Cells with out-of-sample net PF > 1 **and** at least 30 out-of-sample trades: **75**.
- Cells with out-of-sample net PF > 1, at least 30 out-of-sample trades, and out-of-sample net PF still > 1 under 2x costs: **10**.

## Leg 3 — Screen survivors (verified with a real backtest)

Screen: out-of-sample net PF > 0.9 with at least 30 out-of-sample trades. 180 cell(s) kept.

| Symbol | Cell | OOS trades | Screen OOS PF | Screen OOS stress PF | Exact OOS PF | Exact OOS Sharpe | Exact stress OOS PF | Label |
|---|---|---|---|---|---|---|---|---|
| AAVE/USDT | P21_200 | 94 | 0.9328 | 0.6605 | 0.9328 | -0.2732 | 0.6434 | rejected |
| ALGO/USDT | P12_144 | 111 | 0.9155 | 0.6580 | 0.9248 | -0.3675 | 0.6558 | rejected |
| ALGO/USDT | P12_200 | 80 | 0.9881 | 0.7417 | 0.8791 | -0.5561 | 0.6406 | rejected |
| ANYONE/USDT | P55_200 | 96 | 0.9015 | 0.6696 | 0.8575 | -0.8161 | 0.6207 | rejected |
| APE/USDT | P21_200 | 145 | 0.9223 | 0.6878 | 0.9350 | -0.3843 | 0.7100 | rejected |
| APT/USDT | P26_200 | 105 | 0.9138 | 0.6717 | 0.9318 | -0.3122 | 0.6788 | rejected |
| AVA/USDT | P12_200 | 139 | 0.9387 | 0.6655 | 0.9250 | -0.4176 | 0.6528 | rejected |
| AVA/USDT | P20_144 | 164 | 0.9858 | 0.6629 | 0.9858 | -0.0274 | 0.6657 | rejected |
| AVA/USDT | P20_200 | 120 | 0.9979 | 0.7415 | 0.9979 | 0.0469 | 0.7425 | rejected |
| AVA/USDT | P21_144 | 164 | 0.9509 | 0.6379 | 0.9509 | -0.2739 | 0.6425 | rejected |
| AVA/USDT | P21_200 | 120 | 0.9978 | 0.7413 | 0.9978 | 0.0462 | 0.7424 | rejected |
| AVA/USDT | P26_200 | 110 | 1.0230 | 0.7535 | 1.0230 | 0.1853 | 0.7525 | exploratory signal |
| AVA/USDT | P34_144 | 164 | 1.0061 | 0.6834 | 1.0061 | 0.1096 | 0.6838 | exploratory signal |
| AVA/USDT | P34_200 | 110 | 0.9578 | 0.6739 | 0.9578 | -0.1706 | 0.6561 | rejected |
| AVA/USDT | P50_144 | 153 | 0.9654 | 0.6048 | 0.9654 | -0.1509 | 0.5912 | rejected |
| AVA/USDT | P50_200 | 104 | 0.9906 | 0.7074 | 0.9906 | 0.0065 | 0.6919 | rejected |
| AVA/USDT | P55_144 | 158 | 0.9948 | 0.6450 | 0.9948 | 0.0335 | 0.6369 | rejected |
| AVA/USDT | P55_200 | 114 | 1.0014 | 0.6992 | 1.0014 | 0.0644 | 0.6907 | exploratory signal |
| BAND/USDT | P34_200 | 134 | 0.9755 | 0.6492 | 0.9755 | -0.0822 | 0.6404 | rejected |
| BAT/USDT | P8_200 | 75 | 0.9594 | 0.7460 | 0.8888 | -0.5251 | 0.6494 | rejected |
| BIGTIME/USDT | P8_200 | 77 | 0.9893 | 0.6909 | 0.9663 | -0.1101 | 0.6811 | rejected |
| BLUR/USDT | P12_144 | 122 | 0.9745 | 0.7267 | 1.0240 | 0.2108 | 0.7676 | exploratory signal |
| BLUR/USDT | P8_144 | 129 | 1.0546 | 0.7916 | 1.1004 | 0.6732 | 0.8340 | exploratory signal |
| BOME/USDT | P26_200 | 131 | 0.9334 | 0.7267 | 0.9334 | -0.3509 | 0.7242 | rejected |
| BOME/USDT | P34_200 | 142 | 0.9060 | 0.6798 | 0.9060 | -0.5624 | 0.6830 | rejected |
| BRETT/USDT | P8_200 | 51 | 1.3107 | 1.0111 | 1.3323 | 1.2200 | 1.0489 | exploratory signal |
| CHZ/USDT | P12_200 | 99 | 1.0045 | 0.7929 | 1.0063 | 0.0904 | 0.7999 | exploratory signal |
| CHZ/USDT | P20_200 | 107 | 0.9563 | 0.7271 | 0.9065 | -0.4951 | 0.6878 | rejected |
| CHZ/USDT | P21_200 | 104 | 0.9085 | 0.6905 | 0.8634 | -0.7637 | 0.6557 | rejected |
| CHZ/USDT | P26_200 | 103 | 0.9749 | 0.7253 | 0.9091 | -0.4566 | 0.6728 | rejected |
| CHZ/USDT | P34_200 | 105 | 0.9645 | 0.7494 | 0.9645 | -0.1391 | 0.7463 | rejected |
| CHZ/USDT | P50_200 | 102 | 1.0149 | 0.7979 | 1.0149 | 0.1331 | 0.8012 | exploratory signal |
| CHZ/USDT | P8_200 | 75 | 1.1760 | 0.9416 | 1.0938 | 0.4669 | 0.8685 | exploratory signal |
| COTI/USDT | P26_144 | 222 | 0.9020 | 0.6255 | 0.9020 | -0.7384 | 0.6266 | rejected |
| COTI/USDT | P34_200 | 152 | 0.9165 | 0.6483 | 0.9192 | -0.4853 | 0.6493 | rejected |
| COTI/USDT | P50_200 | 147 | 0.9196 | 0.6158 | 0.9196 | -0.4983 | 0.6286 | rejected |
| DEXE/USDT | P100_200 | 75 | 1.2440 | 0.9975 | 1.2440 | 1.0181 | 0.9883 | exploratory signal |
| DEXE/USDT | P12_144 | 106 | 0.9871 | 0.8035 | 0.9992 | 0.0547 | 0.7850 | rejected |
| DEXE/USDT | P12_200 | 79 | 1.2103 | 1.0325 | 1.1885 | 0.9984 | 0.9892 | exploratory signal |
| DEXE/USDT | P20_144 | 115 | 0.9827 | 0.7906 | 0.9719 | -0.1007 | 0.7617 | rejected |
| DEXE/USDT | P20_200 | 77 | 1.4790 | 1.2967 | 1.1492 | 0.8036 | 0.9157 | exploratory signal |
| DEXE/USDT | P21_144 | 115 | 0.9370 | 0.7493 | 0.9305 | -0.3477 | 0.7240 | rejected |
| DEXE/USDT | P21_200 | 75 | 1.4985 | 1.3136 | 1.1552 | 0.8244 | 0.9027 | exploratory signal |
| DEXE/USDT | P26_200 | 73 | 1.1484 | 1.0066 | 1.0253 | 0.1895 | 0.8405 | exploratory signal |
| DEXE/USDT | P34_144 | 114 | 0.9986 | 0.7486 | 0.9986 | 0.0507 | 0.7415 | rejected |
| DEXE/USDT | P50_144 | 111 | 1.1745 | 0.8964 | 1.1745 | 0.9156 | 0.8817 | exploratory signal |
| DEXE/USDT | P50_200 | 86 | 1.3565 | 1.1165 | 1.3819 | 1.5987 | 1.1322 | exploratory signal |
| DEXE/USDT | P55_144 | 101 | 1.1707 | 0.8868 | 1.1694 | 0.8837 | 0.8636 | exploratory signal |
| DEXE/USDT | P55_200 | 81 | 1.3378 | 1.0789 | 1.3647 | 1.4994 | 1.0975 | exploratory signal |
| DEXE/USDT | P89_200 | 70 | 1.2332 | 0.9859 | 1.2231 | 0.9327 | 0.9736 | exploratory signal |
| DEXE/USDT | P8_144 | 98 | 1.1501 | 0.9456 | 1.1626 | 0.8760 | 0.9405 | exploratory signal |
| DEXE/USDT | P8_200 | 71 | 1.1213 | 0.9596 | 1.0014 | 0.0617 | 0.8333 | exploratory signal |
| DIA/USDT | P12_200 | 102 | 1.1635 | 0.8606 | 1.1966 | 1.0062 | 0.8793 | exploratory signal |
| DIA/USDT | P20_200 | 147 | 1.0774 | 0.7635 | 1.0726 | 0.4994 | 0.7541 | exploratory signal |
| DIA/USDT | P21_200 | 143 | 1.1243 | 0.7923 | 1.1171 | 0.7324 | 0.7790 | exploratory signal |
| DIA/USDT | P26_200 | 133 | 1.0891 | 0.7695 | 1.1200 | 0.7094 | 0.7792 | exploratory signal |
| DIA/USDT | P8_200 | 109 | 1.0168 | 0.7269 | 1.0532 | 0.3455 | 0.7543 | exploratory signal |
| DYDX/USDT | P50_200 | 129 | 0.9643 | 0.7328 | 0.9643 | -0.1686 | 0.7437 | rejected |
| EGLD/USDT | P100_200 | 117 | 0.9628 | 0.5987 | 0.9628 | -0.1522 | 0.5964 | rejected |
| EGLD/USDT | P26_200 | 147 | 0.9621 | 0.6743 | 0.9621 | -0.1793 | 0.6769 | rejected |
| EGLD/USDT | P55_200 | 124 | 1.0321 | 0.6926 | 1.0321 | 0.2432 | 0.6934 | exploratory signal |
| EGLD/USDT | P89_200 | 117 | 0.9476 | 0.6294 | 0.9476 | -0.2340 | 0.6218 | rejected |
| ENA/USDT | P20_200 | 138 | 0.9766 | 0.7289 | 0.9766 | -0.0822 | 0.7266 | rejected |
| ENA/USDT | P21_200 | 132 | 0.9285 | 0.6929 | 0.9285 | -0.3855 | 0.6912 | rejected |
| ENA/USDT | P26_200 | 131 | 0.9385 | 0.6915 | 0.9385 | -0.3065 | 0.6855 | rejected |
| ENA/USDT | P34_144 | 149 | 0.9924 | 0.7180 | 0.9924 | 0.0161 | 0.7193 | rejected |
| ENA/USDT | P8_200 | 119 | 0.9090 | 0.7125 | 0.9090 | -0.4967 | 0.7139 | rejected |
| EUL/USDT | P8_200 | 168 | 0.9400 | 0.7092 | 0.9395 | -0.3642 | 0.7169 | rejected |
| FET/USDT | P12_200 | 43 | 1.0120 | 0.8082 | 1.0120 | 0.0765 | 0.7932 | exploratory signal |
| FET/USDT | P20_200 | 38 | 1.1220 | 0.9713 | 1.1220 | 0.3944 | 0.9658 | exploratory signal |
| FET/USDT | P21_200 | 43 | 1.0457 | 0.9145 | 1.0457 | 0.1838 | 0.9093 | exploratory signal |
| FLUX/USDT | P12_200 | 98 | 0.9372 | 0.6764 | 0.7966 | -1.3009 | 0.5539 | rejected |
| FLUX/USDT | P8_200 | 112 | 1.1427 | 0.8524 | 0.8969 | -0.5921 | 0.6217 | rejected |
| GMT/USDT | P12_200 | 108 | 1.0360 | 0.7389 | 1.0417 | 0.2948 | 0.7532 | exploratory signal |
| GMT/USDT | P20_200 | 126 | 0.9642 | 0.7100 | 0.9642 | -0.1585 | 0.7138 | rejected |
| GMT/USDT | P21_200 | 126 | 0.9644 | 0.7096 | 0.9644 | -0.1588 | 0.7147 | rejected |
| GMT/USDT | P8_200 | 111 | 1.2524 | 0.9129 | 1.2705 | 1.4351 | 0.9326 | exploratory signal |
| GRT/USDT | P20_200 | 61 | 1.4547 | 1.2401 | 1.3413 | 1.3146 | 1.0976 | exploratory signal |
| GRT/USDT | P8_200 | 64 | 1.3136 | 1.0548 | 1.1224 | 0.5284 | 0.8598 | exploratory signal |
| G/USDT | P8_200 | 77 | 0.9258 | 0.7498 | 0.9179 | -0.3440 | 0.7244 | rejected |
| HNT/USDT | P20_200 | 54 | 0.9249 | 0.6896 | 0.9249 | -0.2588 | 0.6885 | rejected |
| HNT/USDT | P34_200 | 96 | 0.9274 | 0.7153 | 0.9274 | -0.3408 | 0.7127 | rejected |
| ILV/USDT | P21_200 | 167 | 0.9022 | 0.6313 | 0.9022 | -0.6372 | 0.6397 | rejected |
| ILV/USDT | P34_200 | 139 | 0.9995 | 0.6840 | 0.9995 | 0.0600 | 0.6881 | rejected |
| IMX/USDT | P12_200 | 106 | 1.0910 | 0.8134 | 1.0741 | 0.4596 | 0.7975 | exploratory signal |
| IMX/USDT | P20_200 | 141 | 1.0637 | 0.7625 | 1.0856 | 0.5740 | 0.7560 | exploratory signal |
| IMX/USDT | P21_200 | 126 | 0.9908 | 0.7130 | 1.0186 | 0.1711 | 0.7126 | exploratory signal |
| IMX/USDT | P26_200 | 130 | 1.2361 | 0.9136 | 1.2361 | 1.3311 | 0.9190 | exploratory signal |
| IMX/USDT | P34_200 | 118 | 1.2027 | 0.9120 | 1.1940 | 1.1155 | 0.9034 | exploratory signal |
| IMX/USDT | P50_200 | 126 | 0.9206 | 0.6458 | 0.9206 | -0.4421 | 0.6511 | rejected |
| IMX/USDT | P55_200 | 121 | 0.9736 | 0.7171 | 0.9736 | -0.0952 | 0.7160 | rejected |
| IMX/USDT | P8_200 | 109 | 1.0832 | 0.8229 | 1.0973 | 0.5817 | 0.8325 | exploratory signal |
| IOTX/USDT | P55_200 | 150 | 0.9349 | 0.6743 | 0.8677 | -0.8452 | 0.6171 | rejected |
| JASMY/USDT | P21_200 | 167 | 0.9003 | 0.5934 | 0.9167 | -0.5194 | 0.6015 | rejected |
| JASMY/USDT | P50_200 | 125 | 0.9602 | 0.6617 | 0.9841 | -0.0363 | 0.6752 | rejected |
| JASMY/USDT | P55_200 | 138 | 0.9065 | 0.6212 | 0.9347 | -0.3641 | 0.6379 | rejected |
| JTO/USDT | P8_200 | 143 | 0.9030 | 0.7173 | 0.9338 | -0.3866 | 0.7352 | rejected |
| LTC/USDT | P12_200 | 52 | 0.9257 | 0.5884 | 0.5708 | -2.5915 | 0.3071 | rejected |
| MERL/USDT | P8_200 | 31 | 1.2518 | 1.0215 | 1.2518 | 0.6633 | 1.0101 | exploratory signal |
| MEW/USDT | P8_200 | 58 | 0.9055 | 0.6279 | 0.7467 | -1.1474 | 0.5193 | rejected |
| MINA/USDT | P12_200 | 87 | 1.1212 | 0.8579 | 1.1931 | 0.8675 | 0.9023 | exploratory signal |
| MINA/USDT | P21_200 | 108 | 0.9667 | 0.6925 | 1.0034 | 0.0739 | 0.7072 | exploratory signal |
| MINA/USDT | P26_200 | 102 | 0.9129 | 0.6519 | 0.9163 | -0.3894 | 0.6397 | rejected |
| MINA/USDT | P8_200 | 95 | 1.0132 | 0.7914 | 1.0549 | 0.3103 | 0.8240 | exploratory signal |
| MNT/USDT | P20_144 | 98 | 0.9403 | 0.6731 | 0.9403 | -0.2679 | 0.6756 | rejected |
| MNT/USDT | P20_200 | 80 | 0.9226 | 0.7140 | 0.9226 | -0.3280 | 0.7130 | rejected |
| MNT/USDT | P21_144 | 103 | 0.9384 | 0.6653 | 0.9384 | -0.2927 | 0.6725 | rejected |
| MNT/USDT | P21_200 | 86 | 1.0499 | 0.7611 | 1.0499 | 0.2771 | 0.7566 | exploratory signal |
| MNT/USDT | P26_144 | 101 | 0.9522 | 0.6624 | 0.9522 | -0.2124 | 0.6699 | rejected |
| MNT/USDT | P26_200 | 84 | 1.0746 | 0.8069 | 1.0746 | 0.3917 | 0.8076 | exploratory signal |
| MNT/USDT | P34_200 | 85 | 0.9497 | 0.7233 | 0.9497 | -0.1986 | 0.7217 | rejected |
| MNT/USDT | P50_200 | 78 | 0.9094 | 0.6948 | 0.9094 | -0.3881 | 0.6931 | rejected |
| MNT/USDT | P55_200 | 80 | 1.0284 | 0.7320 | 1.0284 | 0.1766 | 0.7293 | exploratory signal |
| MNT/USDT | P8_200 | 88 | 0.9848 | 0.7690 | 0.9783 | -0.0608 | 0.7647 | rejected |
| MOG/USDT | P8_200 | 59 | 0.9080 | 0.6695 | 0.9365 | -0.2379 | 0.6964 | rejected |
| NEO/USDT | P8_144 | 104 | 1.0203 | 0.6914 | 0.8509 | -0.7703 | 0.5446 | rejected |
| NEO/USDT | P8_200 | 78 | 1.0395 | 0.7378 | 0.7960 | -0.9988 | 0.5048 | rejected |
| PENDLE/USDT | P34_144 | 132 | 0.9016 | 0.6234 | 0.9016 | -0.5717 | 0.6270 | rejected |
| PENDLE/USDT | P50_200 | 107 | 0.9557 | 0.6896 | 0.9557 | -0.1876 | 0.6885 | rejected |
| PEOPLE/USDT | P20_144 | 137 | 0.9970 | 0.7112 | 0.9970 | 0.0443 | 0.7032 | rejected |
| PEOPLE/USDT | P21_144 | 140 | 1.0165 | 0.7170 | 1.0165 | 0.1619 | 0.7106 | exploratory signal |
| POL/USDT | P21_200 | 91 | 0.9054 | 0.6140 | 0.9054 | -0.4477 | 0.6165 | rejected |
| POL/USDT | P34_200 | 123 | 0.9199 | 0.5674 | 0.9199 | -0.4415 | 0.5860 | rejected |
| POL/USDT | P8_200 | 64 | 1.0564 | 0.7087 | 1.0564 | 0.2848 | 0.7264 | exploratory signal |
| PUFFER/USDT | P12_144 | 125 | 0.9988 | 0.8373 | 1.0141 | 0.1614 | 0.8524 | exploratory signal |
| PUFFER/USDT | P20_144 | 123 | 1.1363 | 0.9458 | 1.1363 | 0.9193 | 0.9484 | exploratory signal |
| PUFFER/USDT | P20_200 | 91 | 1.0860 | 0.9220 | 1.1080 | 0.6375 | 0.9391 | exploratory signal |
| PUFFER/USDT | P21_100 | 141 | 0.9055 | 0.6854 | 0.9055 | -0.6191 | 0.6793 | rejected |
| PUFFER/USDT | P21_144 | 116 | 1.1866 | 0.9929 | 1.1866 | 1.1610 | 0.9934 | exploratory signal |
| PUFFER/USDT | P21_200 | 81 | 1.0560 | 0.8896 | 1.0805 | 0.4664 | 0.9075 | exploratory signal |
| PUFFER/USDT | P26_100 | 160 | 0.9203 | 0.6577 | 0.9203 | -0.5406 | 0.6518 | rejected |
| PUFFER/USDT | P26_144 | 119 | 1.1395 | 0.9079 | 1.1395 | 0.9080 | 0.9067 | exploratory signal |
| PUFFER/USDT | P26_200 | 83 | 0.9871 | 0.7912 | 0.9871 | -0.0127 | 0.7845 | rejected |
| PYTH/USDT | P8_200 | 99 | 0.9560 | 0.7325 | 0.9510 | -0.1970 | 0.7028 | rejected |
| RENDER/USDT | P12_200 | 44 | 1.0001 | 0.8741 | 1.1268 | 0.5348 | 0.9711 | exploratory signal |
| RENDER/USDT | P20_200 | 96 | 1.0042 | 0.7640 | 1.0674 | 0.4387 | 0.8212 | exploratory signal |
| RENDER/USDT | P21_200 | 97 | 0.9380 | 0.7125 | 1.0020 | 0.0704 | 0.7703 | exploratory signal |
| RENDER/USDT | P8_200 | 56 | 1.0150 | 0.8590 | 1.0150 | 0.1086 | 0.8624 | exploratory signal |
| ROSE/USDT | P12_144 | 135 | 0.9650 | 0.7147 | 0.9593 | -0.2040 | 0.7179 | rejected |
| ROSE/USDT | P12_200 | 73 | 0.9993 | 0.7596 | 1.1244 | 0.6159 | 0.8764 | exploratory signal |
| ROSE/USDT | P34_200 | 103 | 1.1654 | 0.8560 | 1.1654 | 0.8969 | 0.8698 | exploratory signal |
| ROSE/USDT | P55_200 | 145 | 0.9839 | 0.6647 | 0.9839 | -0.0397 | 0.6723 | rejected |
| ROSE/USDT | P8_144 | 124 | 0.9314 | 0.7060 | 0.9950 | 0.0311 | 0.7436 | rejected |
| RPL/USDT | P12_144 | 154 | 1.0359 | 0.8223 | 0.9841 | -0.0413 | 0.7757 | rejected |
| RPL/USDT | P8_200 | 148 | 0.9341 | 0.7304 | 0.9212 | -0.4612 | 0.7205 | rejected |
| RUNE/USDT | P34_144 | 144 | 0.9119 | 0.5714 | 0.9119 | -0.5082 | 0.5678 | rejected |
| RUNE/USDT | P50_144 | 149 | 1.1446 | 0.7246 | 1.1446 | 0.9042 | 0.7206 | exploratory signal |
| RUNE/USDT | P50_200 | 103 | 1.1367 | 0.7700 | 1.1367 | 0.7176 | 0.7677 | exploratory signal |
| RUNE/USDT | P55_144 | 150 | 0.9572 | 0.5483 | 0.9572 | -0.2053 | 0.5407 | rejected |
| RUNE/USDT | P55_200 | 107 | 1.0985 | 0.7382 | 1.0985 | 0.5451 | 0.7313 | exploratory signal |
| SATS/USDT | P8_200 | 104 | 0.9343 | 0.7709 | 0.9602 | -0.1678 | 0.7882 | rejected |
| SOL/USDT | P12_200 | 33 | 1.1493 | 0.7949 | 1.1493 | 0.4401 | 0.7792 | exploratory signal |
| SUPER/USDT | P8_200 | 73 | 1.1618 | 0.9104 | 0.9536 | -0.1638 | 0.7176 | rejected |
| SYN/USDT | P12_200 | 120 | 0.9994 | 0.7918 | 0.9812 | -0.0515 | 0.7759 | rejected |
| SYN/USDT | P20_200 | 112 | 1.1832 | 0.9062 | 1.1591 | 0.8931 | 0.8940 | exploratory signal |
| SYN/USDT | P21_200 | 110 | 1.1119 | 0.8567 | 1.0894 | 0.5427 | 0.8467 | exploratory signal |
| SYN/USDT | P26_200 | 103 | 1.1053 | 0.9176 | 1.1053 | 0.6022 | 0.9193 | exploratory signal |
| SYN/USDT | P34_200 | 112 | 1.0080 | 0.8193 | 1.0080 | 0.1013 | 0.8197 | exploratory signal |
| THETA/USDT | P34_200 | 152 | 0.9129 | 0.6064 | 0.9129 | -0.5078 | 0.6018 | rejected |
| T/USDT | P12_200 | 60 | 1.1145 | 0.8176 | 1.1145 | 0.4562 | 0.7967 | exploratory signal |
| VELO/USDT | P12_200 | 143 | 0.9893 | 0.7623 | 0.9741 | -0.0941 | 0.7422 | rejected |
| VELO/USDT | P20_200 | 140 | 0.9092 | 0.6799 | 0.8953 | -0.5981 | 0.6580 | rejected |
| WIN/USDT | P12_200 | 110 | 0.9820 | 0.7195 | 0.9796 | -0.0441 | 0.6880 | rejected |
| WIN/USDT | P8_200 | 132 | 0.9022 | 0.6159 | 0.9160 | -0.4155 | 0.5934 | rejected |
| WLD/USDT | P20_144 | 160 | 0.9622 | 0.7652 | 0.9622 | -0.1811 | 0.7574 | rejected |
| WLD/USDT | P20_200 | 105 | 1.1516 | 0.9619 | 1.1044 | 0.5890 | 0.8974 | exploratory signal |
| WLD/USDT | P21_200 | 123 | 1.0521 | 0.8457 | 1.0521 | 0.3429 | 0.8346 | exploratory signal |
| WLD/USDT | P26_200 | 114 | 0.9983 | 0.8119 | 0.9983 | 0.0480 | 0.7992 | rejected |
| W/USDT | P12_144 | 161 | 0.9473 | 0.6656 | 0.9473 | -0.2853 | 0.6601 | rejected |
| W/USDT | P12_200 | 101 | 1.2628 | 0.9698 | 1.1585 | 0.8588 | 0.8735 | exploratory signal |
| W/USDT | P26_200 | 125 | 0.9140 | 0.6819 | 0.9140 | -0.4366 | 0.6682 | rejected |
| W/USDT | P8_200 | 132 | 1.0954 | 0.8361 | 1.0970 | 0.5938 | 0.8194 | exploratory signal |
| XPR/USDT | P8_200 | 59 | 0.9827 | 0.6799 | 0.9766 | -0.0516 | 0.6699 | rejected |
| ZEC/USDT | P12_144 | 133 | 0.9024 | 0.6819 | 0.9032 | -0.5443 | 0.6859 | rejected |
| ZEC/USDT | P12_200 | 86 | 0.9456 | 0.7605 | 0.9438 | -0.2252 | 0.7568 | rejected |
| ZEC/USDT | P8_144 | 124 | 0.9225 | 0.7163 | 0.8908 | -0.6223 | 0.6955 | rejected |
| ZEC/USDT | P8_200 | 94 | 0.9295 | 0.7489 | 0.8897 | -0.5638 | 0.7234 | rejected |
| ZEN/USDT | P12_200 | 42 | 1.1111 | 0.9022 | 1.2739 | 0.8778 | 1.0388 | exploratory signal |
| ZEN/USDT | P8_200 | 38 | 1.0986 | 0.8670 | 1.1971 | 0.7135 | 0.8871 | exploratory signal |
| ZK/USDT | P21_200 | 115 | 0.9545 | 0.6949 | 0.9264 | -0.3816 | 0.6676 | rejected |

## Leg 3b — The closest survivors: cells that also survive the cost stress

These are the verified cells whose out-of-sample net PF is above 1 both at the registered costs and at 2x costs. The last three columns are the full-sample result, which is what a promotion would have to survive as well.

| Symbol | Cell | OOS trades | Exact OOS PF | Exact OOS Sharpe | Exact stress OOS PF | Full-sample net PF | Full-sample stress PF | Label |
|---|---|---|---|---|---|---|---|---|
| BRETT/USDT | P8_200 | 51 | 1.3323 | 1.2200 | 1.0489 | 0.8337 | 0.6861 | exploratory signal |
| DEXE/USDT | P50_200 | 86 | 1.3819 | 1.5987 | 1.1322 | 0.8058 | 0.5982 | exploratory signal |
| DEXE/USDT | P55_200 | 81 | 1.3647 | 1.4994 | 1.0975 | 0.7535 | 0.5577 | exploratory signal |
| GRT/USDT | P20_200 | 61 | 1.3413 | 1.3146 | 1.0976 | 0.9087 | 0.7066 | exploratory signal |
| MERL/USDT | P8_200 | 31 | 1.2518 | 0.6633 | 1.0101 | 0.8224 | 0.6661 | exploratory signal |
| ZEN/USDT | P12_200 | 42 | 1.2739 | 0.8778 | 1.0388 | 0.7833 | 0.5673 | exploratory signal |

## Leg 3c — Why the exploratory signals did not promote

| Blocking gate | Cells |
|---|---|
| out-of-sample net PF still > 1 under 2x costs | 70 |
| full-sample net PF still > 1 under 2x costs | 76 |
| out-of-sample Sharpe > 0 | 0 |

## Leg 3d — Does the verdict depend on the out-of-sample window?

The closest survivors were re-verified at every window length. A cell that only looks good at one window length is an artifact of that choice.

| Symbol | Cell | OOS 20% PF / stress PF | OOS 35% PF / stress PF | OOS 50% PF / stress PF |
|---|---|---|---|---|
| BRETT/USDT | P8_200 | 1.2320 / 0.9416 | 1.3323 / 1.0489 | 1.0837 / 0.8464 |
| DEXE/USDT | P50_200 | 1.2043 / 1.0345 | 1.3819 / 1.1322 | 0.9681 / 0.6810 |
| DEXE/USDT | P55_200 | 1.1283 / 0.9564 | 1.3647 / 1.0975 | 1.0787 / 0.7813 |
| GRT/USDT | P20_200 | 0.8877 / 0.5715 | 1.3413 / 1.0976 | 0.9737 / 0.7308 |
| MERL/USDT | P8_200 | 0.5627 / 0.4021 | 1.2518 / 1.0101 | 0.8057 / 0.6150 |
| ZEN/USDT | P12_200 | 0.9061 / 0.6012 | 1.2739 / 1.0388 | 0.9331 / 0.7199 |

| Symbol | Cell | OOS 20% trades | OOS 35% trades | OOS 50% trades |
|---|---|---|---|---|
| BRETT/USDT | P8_200 | 47 | 54 | 97 |
| DEXE/USDT | P50_200 | 37 | 87 | 126 |
| DEXE/USDT | P55_200 | 36 | 82 | 117 |
| GRT/USDT | P20_200 | 66 | 70 | 116 |
| MERL/USDT | P8_200 | 92 | 31 | 102 |
| ZEN/USDT | P12_200 | 35 | 43 | 112 |

## Leg 4 — Selection-bias check against the in-sample winners

| Population | Cells | Out-of-sample PF > 1 | With enough OOS trades | Survive the full §3.4 gate |
|---|---|---|---|---|
| in-sample net PF > 1 (checked by the pipeline) | 36 | 1 | 1 | 0 |
| all cells | 17556 | 77 | 75 | 0 |

## Leg 5 — Screen fidelity against the exact backtest

The stage-1 screen was compared with the authoritative numbers of `results/20261021_033219_candidate_check`, which re-ran the same cells through the real backtest.

| Metric | Value |
|---|---|
| Cells compared | 36 |
| Cells with an out-of-sample profit factor in both runs | 4 |
| Cells with no out-of-sample trade in either run (agree by construction) | 32 |
| Mean absolute net PF difference (scored cells) | 0.0603 |
| Max absolute net PF difference (scored cells) | 0.2082 |
| Max absolute trade-count difference | 6 |
| Scored cells where both put the net PF on the same side of 1.0 | 3 of 4 |

The screen can be optimistic: it reuses the full-sample trade blotter, so the out-of-sample window inherits the in-sample equity path and the position state at the boundary. That is why the screen threshold is loose and every verdict is taken from the exact stage-2 numbers.

## Gates (PROMPT.md §3.3, §3.4)

- Grid cells evaluated out of sample: **17556** (the pipeline had only checked 36).
- Credible candidates found anywhere in the grid: **0**.
- Exploratory signals found anywhere in the grid: **76**.
- Screen survivors verified with a real backtest: **180**.

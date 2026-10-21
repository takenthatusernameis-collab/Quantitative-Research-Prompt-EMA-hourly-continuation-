# Grid-Wide Out-of-Sample Audit — EMA Hourly Continuation

**Source run:** `results/20261021_125403_grid`
**Generated:** 2026-10-21T13:53:51.242418+00:00
**Universe:** 266 symbols, 17556 grid cells
**OOS window:** trailing 35% of each symbol's bars, entries restricted to the window
**Cost stress:** 2x fees and slippage (base 10 bps taker + 2 bps slippage per side)
**Exact re-verification engine:** fast

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

Screen: out-of-sample net PF > 0.9 with at least 30 out-of-sample trades. 1426 cell(s) kept.

| Symbol | Cell | OOS trades | Screen OOS PF | Screen OOS stress PF | Exact OOS PF | Exact OOS Sharpe | Exact stress OOS PF | Label |
|---|---|---|---|---|---|---|---|---|
| 1INCH/USDT | P34_200 | 69 | 0.9701 | 0.7455 | 0.9701 | -0.0888 | 0.7470 | rejected |
| 1INCH/USDT | P55_200 | 111 | 0.9002 | 0.6224 | 0.9002 | -0.5387 | 0.6329 | rejected |
| AAVE/USDT | P20_200 | 70 | 1.0504 | 0.8927 | 1.0504 | 0.2492 | 0.8841 | exploratory signal |
| AAVE/USDT | P21_200 | 74 | 1.0964 | 0.9297 | 1.0964 | 0.4412 | 0.9212 | exploratory signal |
| AAVE/USDT | P8_144 | 79 | 1.0035 | 0.8657 | 1.0035 | 0.0630 | 0.8596 | exploratory signal |
| AAVE/USDT | P8_200 | 78 | 0.9736 | 0.8322 | 0.9736 | -0.0718 | 0.8238 | rejected |
| ACE/USDT | P100_200 | 103 | 0.9016 | 0.6802 | 0.9016 | -0.4918 | 0.6796 | rejected |
| ACE/USDT | P21_50 | 176 | 0.9163 | 0.6133 | 0.9163 | -0.5347 | 0.6141 | rejected |
| ACE/USDT | P21_55 | 177 | 0.9065 | 0.6105 | 0.9065 | -0.5956 | 0.6044 | rejected |
| ADA/USDT | P55_144 | 94 | 0.9656 | 0.7311 | 0.9656 | -0.1231 | 0.7255 | rejected |
| ADA/USDT | P8_12 | 54 | 1.0522 | 0.6948 | 1.0522 | 0.2256 | 0.6826 | exploratory signal |
| ADA/USDT | P8_20 | 119 | 1.0191 | 0.6907 | 1.0191 | 0.1595 | 0.6753 | exploratory signal |
| ADA/USDT | P8_21 | 135 | 0.9658 | 0.6533 | 0.9658 | -0.1336 | 0.6329 | rejected |
| AERO/USDT | P12_20 | 115 | 1.0243 | 0.7200 | 1.0243 | 0.1916 | 0.7200 | exploratory signal |
| AERO/USDT | P12_200 | 79 | 1.1392 | 1.0084 | 1.1491 | 0.7642 | 1.0137 | credible candidate |
| AERO/USDT | P12_21 | 133 | 1.0013 | 0.6742 | 1.0013 | 0.0690 | 0.6761 | exploratory signal |
| AERO/USDT | P12_26 | 180 | 0.9399 | 0.6677 | 0.9399 | -0.3659 | 0.6691 | rejected |
| AERO/USDT | P12_50 | 214 | 0.9197 | 0.7180 | 0.9197 | -0.5816 | 0.7218 | rejected |
| AERO/USDT | P12_55 | 213 | 0.9626 | 0.7651 | 0.9626 | -0.2253 | 0.7704 | rejected |
| AERO/USDT | P12_89 | 165 | 0.9298 | 0.7654 | 0.9298 | -0.4236 | 0.7642 | rejected |
| AERO/USDT | P20_21 | 44 | 1.0593 | 0.7133 | 1.0593 | 0.2385 | 0.7169 | exploratory signal |
| AERO/USDT | P20_26 | 62 | 0.9072 | 0.6320 | 0.9072 | -0.3765 | 0.6410 | rejected |
| AERO/USDT | P21_26 | 56 | 1.0008 | 0.6966 | 1.0008 | 0.0433 | 0.7050 | exploratory signal |
| AERO/USDT | P34_55 | 107 | 0.9190 | 0.6604 | 0.9190 | -0.4161 | 0.6655 | rejected |
| AERO/USDT | P8_12 | 112 | 1.0137 | 0.7021 | 1.0137 | 0.1315 | 0.7064 | exploratory signal |
| AERO/USDT | P8_200 | 80 | 1.0259 | 0.9008 | 1.0668 | 0.3869 | 0.9346 | exploratory signal |
| AEVO/USDT | P26_200 | 133 | 0.9056 | 0.7127 | 0.9056 | -0.5465 | 0.7150 | rejected |
| AKT/USDT | P20_21 | 39 | 0.9422 | 0.6906 | 0.9422 | -0.1625 | 0.6898 | rejected |
| AKT/USDT | P20_26 | 61 | 1.0354 | 0.7413 | 1.0354 | 0.1844 | 0.7419 | exploratory signal |
| AKT/USDT | P21_26 | 57 | 0.9169 | 0.6524 | 0.9169 | -0.3068 | 0.6535 | rejected |
| AKT/USDT | P50_144 | 126 | 0.9209 | 0.7747 | 0.9209 | -0.4501 | 0.7793 | rejected |
| AKT/USDT | P55_144 | 123 | 1.0220 | 0.8518 | 1.0220 | 0.1916 | 0.8575 | exploratory signal |
| ALGO/USDT | P12_144 | 90 | 0.9953 | 0.8475 | 1.0031 | 0.0678 | 0.8483 | exploratory signal |
| ALGO/USDT | P12_200 | 67 | 0.9831 | 0.8564 | 0.9146 | -0.3526 | 0.7913 | rejected |
| ALGO/USDT | P12_50 | 222 | 0.9154 | 0.6698 | 0.9154 | -0.6045 | 0.6675 | rejected |
| ALGO/USDT | P89_100 | 30 | 1.0408 | 0.6928 | 1.0408 | 0.1404 | 0.6933 | exploratory signal |
| ALGO/USDT | P8_100 | 106 | 0.9969 | 0.8027 | 1.0068 | 0.0933 | 0.8111 | exploratory signal |
| ALGO/USDT | P8_144 | 60 | 1.1300 | 0.9388 | 1.1364 | 0.5922 | 0.9446 | exploratory signal |
| ALGO/USDT | P8_200 | 40 | 0.9037 | 0.7680 | 0.8427 | -0.5837 | 0.7058 | rejected |
| ALGO/USDT | P8_34 | 243 | 0.9393 | 0.6751 | 0.9393 | -0.4421 | 0.6811 | rejected |
| ALGO/USDT | P8_89 | 142 | 0.9013 | 0.7148 | 0.9115 | -0.5219 | 0.7206 | rejected |
| ANYONE/USDT | P100_200 | 72 | 1.0343 | 0.8132 | 1.0778 | 0.4086 | 0.8470 | exploratory signal |
| ANYONE/USDT | P12_200 | 72 | 0.9205 | 0.7767 | 0.8213 | -0.9184 | 0.6906 | rejected |
| ANYONE/USDT | P144_200 | 75 | 0.9472 | 0.7066 | 0.9472 | -0.2134 | 0.7081 | rejected |
| ANYONE/USDT | P20_144 | 123 | 0.9873 | 0.8280 | 1.0023 | 0.0776 | 0.8458 | exploratory signal |
| ANYONE/USDT | P20_200 | 66 | 1.1205 | 0.9526 | 1.0662 | 0.3445 | 0.9023 | exploratory signal |
| ANYONE/USDT | P21_200 | 71 | 0.9558 | 0.8164 | 0.9215 | -0.3478 | 0.7846 | rejected |
| ANYONE/USDT | P34_200 | 73 | 0.9374 | 0.7965 | 0.9525 | -0.1890 | 0.8045 | rejected |
| ANYONE/USDT | P50_100 | 115 | 0.9860 | 0.7783 | 0.9860 | -0.0247 | 0.7803 | rejected |
| ANYONE/USDT | P50_144 | 106 | 1.0633 | 0.8651 | 1.0809 | 0.5154 | 0.8848 | exploratory signal |
| ANYONE/USDT | P50_200 | 83 | 1.0511 | 0.8819 | 1.0609 | 0.3667 | 0.8924 | exploratory signal |
| ANYONE/USDT | P55_100 | 106 | 0.9024 | 0.7002 | 0.9024 | -0.5420 | 0.7033 | rejected |
| ANYONE/USDT | P55_144 | 102 | 1.0233 | 0.8229 | 1.0233 | 0.1896 | 0.8288 | exploratory signal |
| ANYONE/USDT | P55_200 | 81 | 1.1020 | 0.9173 | 1.0868 | 0.4894 | 0.9084 | exploratory signal |
| ANYONE/USDT | P89_144 | 80 | 1.0516 | 0.8198 | 1.0516 | 0.2951 | 0.8148 | exploratory signal |
| ANYONE/USDT | P89_200 | 78 | 1.0894 | 0.8765 | 1.1287 | 0.6536 | 0.9060 | exploratory signal |
| ANYONE/USDT | P8_144 | 132 | 0.9048 | 0.7601 | 0.8848 | -0.7891 | 0.7476 | rejected |
| ANYONE/USDT | P8_200 | 51 | 0.9636 | 0.8387 | 0.8760 | -0.5286 | 0.7518 | rejected |
| ANYONE/USDT | P8_89 | 195 | 0.9041 | 0.7522 | 0.9133 | -0.6522 | 0.7646 | rejected |
| APE/USDT | P144_200 | 79 | 0.9119 | 0.6524 | 0.9119 | -0.4053 | 0.6643 | rejected |
| APE/USDT | P26_144 | 99 | 1.0245 | 0.8452 | 1.0437 | 0.2848 | 0.8663 | exploratory signal |
| APE/USDT | P55_144 | 118 | 0.9209 | 0.7169 | 0.9361 | -0.3384 | 0.7382 | rejected |
| APE/USDT | P55_200 | 103 | 0.9100 | 0.7545 | 0.9274 | -0.3753 | 0.7773 | rejected |
| APE/USDT | P89_200 | 107 | 0.9323 | 0.7250 | 0.9323 | -0.3303 | 0.7274 | rejected |
| APT/USDT | P12_144 | 86 | 1.1429 | 1.0090 | 1.1795 | 0.8658 | 1.0375 | exploratory signal |
| APT/USDT | P12_200 | 36 | 1.3367 | 1.1823 | 1.4641 | 1.2354 | 1.2962 | exploratory signal |
| APT/USDT | P20_144 | 90 | 1.2129 | 1.0507 | 1.2432 | 1.1762 | 1.0744 | exploratory signal |
| APT/USDT | P20_200 | 61 | 1.0026 | 0.8757 | 1.0665 | 0.3115 | 0.9331 | exploratory signal |
| APT/USDT | P21_144 | 93 | 1.2226 | 1.0567 | 1.2517 | 1.2323 | 1.0800 | exploratory signal |
| APT/USDT | P21_200 | 62 | 1.0299 | 0.8963 | 1.0934 | 0.4192 | 0.9534 | exploratory signal |
| APT/USDT | P26_144 | 133 | 1.0600 | 0.8545 | 1.0600 | 0.4258 | 0.8610 | exploratory signal |
| APT/USDT | P26_200 | 80 | 1.2029 | 1.0384 | 1.2284 | 1.0173 | 1.0591 | exploratory signal |
| APT/USDT | P34_144 | 129 | 0.9409 | 0.7529 | 0.9541 | -0.2260 | 0.7654 | rejected |
| APT/USDT | P34_200 | 72 | 1.1314 | 0.9880 | 1.1590 | 0.7136 | 1.0124 | exploratory signal |
| APT/USDT | P50_144 | 122 | 1.0065 | 0.7787 | 1.0206 | 0.1838 | 0.8006 | exploratory signal |
| APT/USDT | P50_89 | 111 | 0.9536 | 0.6892 | 0.9536 | -0.2175 | 0.6990 | rejected |
| APT/USDT | P55_100 | 114 | 0.9517 | 0.6778 | 0.9517 | -0.2337 | 0.6893 | rejected |
| APT/USDT | P55_144 | 125 | 0.9750 | 0.7408 | 0.9884 | -0.0149 | 0.7684 | rejected |
| APT/USDT | P55_89 | 93 | 0.9833 | 0.6901 | 0.9833 | -0.0358 | 0.6971 | rejected |
| APT/USDT | P8_100 | 120 | 1.0120 | 0.8553 | 1.0251 | 0.2059 | 0.8671 | exploratory signal |
| APT/USDT | P8_144 | 87 | 1.0104 | 0.8899 | 1.0478 | 0.2879 | 0.9213 | exploratory signal |
| APT/USDT | P8_55 | 217 | 0.9005 | 0.7103 | 0.9005 | -0.7305 | 0.7089 | rejected |
| ARB/USDT | P12_100 | 160 | 0.9449 | 0.7556 | 0.9259 | -0.4447 | 0.7344 | rejected |
| ARB/USDT | P12_200 | 31 | 0.9487 | 0.8521 | 0.9805 | -0.0367 | 0.8577 | rejected |
| ARB/USDT | P12_50 | 202 | 0.9314 | 0.7112 | 0.9314 | -0.4487 | 0.7063 | rejected |
| ARB/USDT | P12_55 | 200 | 0.9214 | 0.7119 | 0.9214 | -0.5197 | 0.7051 | rejected |
| ARB/USDT | P20_100 | 163 | 0.9326 | 0.7283 | 0.9326 | -0.3856 | 0.7197 | rejected |
| ARB/USDT | P21_50 | 165 | 0.9790 | 0.7173 | 0.9790 | -0.0726 | 0.7124 | rejected |
| ARB/USDT | P21_55 | 170 | 0.9459 | 0.7050 | 0.9459 | -0.3050 | 0.6995 | rejected |
| ARB/USDT | P26_100 | 160 | 0.9946 | 0.7734 | 0.9946 | 0.0323 | 0.7647 | rejected |
| ARB/USDT | P26_50 | 136 | 0.9698 | 0.6929 | 0.9698 | -0.1229 | 0.6890 | rejected |
| ARB/USDT | P50_100 | 120 | 0.9394 | 0.6965 | 0.9394 | -0.2856 | 0.6864 | rejected |
| ARB/USDT | P50_144 | 119 | 0.9384 | 0.7340 | 0.9384 | -0.3104 | 0.7343 | rejected |
| ARB/USDT | P55_100 | 108 | 0.9203 | 0.6763 | 0.9203 | -0.3794 | 0.6666 | rejected |
| ARB/USDT | P89_100 | 32 | 1.0043 | 0.6805 | 1.0043 | 0.0426 | 0.6778 | exploratory signal |
| ARB/USDT | P8_100 | 131 | 0.9566 | 0.7735 | 0.9175 | -0.4570 | 0.7332 | rejected |
| ARB/USDT | P8_89 | 155 | 0.9776 | 0.7883 | 0.9776 | -0.0777 | 0.7799 | rejected |
| ARKM/USDT | P12_144 | 103 | 0.9176 | 0.7488 | 0.9176 | -0.3975 | 0.7473 | rejected |
| AR/USDT | P34_55 | 126 | 0.9871 | 0.6765 | 0.9871 | -0.0175 | 0.6814 | rejected |
| ATH/USDT | P12_100 | 168 | 1.0204 | 0.8324 | 0.9994 | 0.0679 | 0.8159 | rejected |
| ATH/USDT | P12_200 | 80 | 0.9221 | 0.7920 | 0.9564 | -0.1832 | 0.8228 | rejected |
| ATH/USDT | P12_50 | 207 | 0.9715 | 0.7493 | 0.9715 | -0.1615 | 0.7625 | rejected |
| ATH/USDT | P12_55 | 205 | 1.0210 | 0.7941 | 1.0210 | 0.2481 | 0.8053 | exploratory signal |
| ATH/USDT | P12_89 | 183 | 0.9822 | 0.7934 | 0.9645 | -0.2040 | 0.7833 | rejected |
| ATH/USDT | P21_144 | 147 | 0.9483 | 0.7624 | 0.9329 | -0.4154 | 0.7578 | rejected |
| ATH/USDT | P21_200 | 125 | 0.9508 | 0.7698 | 0.9432 | -0.3097 | 0.7683 | rejected |
| ATH/USDT | P21_89 | 173 | 0.9189 | 0.7322 | 0.9189 | -0.5890 | 0.7463 | rejected |
| ATH/USDT | P26_100 | 161 | 0.9327 | 0.7303 | 0.9327 | -0.4282 | 0.7369 | rejected |
| ATH/USDT | P26_200 | 111 | 0.9491 | 0.7791 | 0.9573 | -0.2023 | 0.7888 | rejected |
| ATH/USDT | P26_34 | 52 | 0.9462 | 0.6508 | 0.9462 | -0.1765 | 0.6524 | rejected |
| ATH/USDT | P26_89 | 161 | 0.9373 | 0.7368 | 0.9373 | -0.3994 | 0.7452 | rejected |
| ATH/USDT | P34_100 | 144 | 0.9930 | 0.7786 | 0.9930 | 0.0205 | 0.7772 | rejected |
| ATH/USDT | P34_200 | 123 | 0.9033 | 0.7406 | 0.8976 | -0.6000 | 0.7332 | rejected |
| ATH/USDT | P8_100 | 179 | 1.0218 | 0.8371 | 1.0125 | 0.1705 | 0.8346 | exploratory signal |
| ATH/USDT | P8_144 | 109 | 0.9538 | 0.7854 | 0.9854 | -0.0260 | 0.8128 | rejected |
| ATH/USDT | P8_200 | 80 | 0.9296 | 0.7966 | 0.9435 | -0.2478 | 0.8086 | rejected |
| ATH/USDT | P8_50 | 234 | 0.9595 | 0.7590 | 0.9595 | -0.2743 | 0.7669 | rejected |
| ATH/USDT | P8_55 | 228 | 0.9669 | 0.7661 | 0.9669 | -0.2025 | 0.7731 | rejected |
| ATH/USDT | P8_89 | 192 | 1.0315 | 0.8400 | 1.0225 | 0.2561 | 0.8402 | exploratory signal |
| ATOM/USDT | P12_200 | 126 | 0.9327 | 0.7685 | 0.9327 | -0.3777 | 0.7762 | rejected |
| ATOM/USDT | P20_100 | 158 | 0.9674 | 0.7421 | 0.9674 | -0.1612 | 0.7504 | rejected |
| ATOM/USDT | P20_144 | 132 | 0.9540 | 0.7582 | 0.9540 | -0.2429 | 0.7688 | rejected |
| ATOM/USDT | P20_200 | 115 | 0.9662 | 0.8027 | 0.9662 | -0.1451 | 0.8076 | rejected |
| ATOM/USDT | P21_100 | 172 | 0.9905 | 0.7563 | 0.9905 | 0.0002 | 0.7667 | rejected |
| ATOM/USDT | P21_144 | 141 | 1.0368 | 0.8261 | 1.0368 | 0.3071 | 0.8395 | exploratory signal |
| ATOM/USDT | P21_200 | 124 | 0.9655 | 0.7987 | 0.9655 | -0.1568 | 0.8047 | rejected |
| ATOM/USDT | P26_100 | 157 | 1.0791 | 0.8249 | 1.0791 | 0.5916 | 0.8365 | exploratory signal |
| ATOM/USDT | P26_144 | 135 | 1.1058 | 0.8768 | 1.1058 | 0.7164 | 0.8896 | exploratory signal |
| ATOM/USDT | P26_200 | 114 | 0.9847 | 0.8186 | 0.9790 | -0.0663 | 0.8167 | rejected |
| ATOM/USDT | P26_89 | 164 | 1.0836 | 0.8126 | 1.0836 | 0.6352 | 0.8259 | exploratory signal |
| ATOM/USDT | P34_100 | 150 | 1.0246 | 0.7579 | 1.0246 | 0.2207 | 0.7578 | exploratory signal |
| ATOM/USDT | P34_144 | 126 | 1.1056 | 0.8662 | 1.1056 | 0.6771 | 0.8750 | exploratory signal |
| ATOM/USDT | P34_200 | 115 | 0.9855 | 0.8066 | 0.9855 | -0.0257 | 0.8070 | rejected |
| ATOM/USDT | P34_89 | 147 | 1.0297 | 0.7502 | 1.0297 | 0.2501 | 0.7513 | exploratory signal |
| ATOM/USDT | P50_100 | 111 | 0.9328 | 0.6582 | 0.9328 | -0.3235 | 0.6562 | rejected |
| ATOM/USDT | P50_144 | 116 | 0.9088 | 0.6957 | 0.9088 | -0.5046 | 0.7012 | rejected |
| ATOM/USDT | P50_200 | 105 | 0.9096 | 0.7282 | 0.9096 | -0.4654 | 0.7298 | rejected |
| ATOM/USDT | P55_100 | 103 | 0.9134 | 0.6403 | 0.9134 | -0.4244 | 0.6398 | rejected |
| ATOM/USDT | P55_144 | 109 | 0.9319 | 0.7120 | 0.9319 | -0.3437 | 0.7164 | rejected |
| ATOM/USDT | P55_200 | 101 | 1.0664 | 0.8486 | 1.0664 | 0.3920 | 0.8470 | exploratory signal |
| ATOM/USDT | P8_100 | 167 | 0.9000 | 0.7205 | 0.9000 | -0.6860 | 0.7282 | rejected |
| AVAX/USDT | P26_200 | 61 | 1.1218 | 0.8621 | 1.1218 | 0.5125 | 0.8636 | exploratory signal |
| AVA/USDT | P100_200 | 101 | 1.1066 | 0.8418 | 1.1066 | 0.5775 | 0.8350 | exploratory signal |
| AVA/USDT | P12_100 | 158 | 1.1492 | 0.9222 | 1.1337 | 0.9115 | 0.9118 | exploratory signal |
| AVA/USDT | P12_144 | 149 | 1.1960 | 0.9624 | 1.1787 | 1.1341 | 0.9498 | exploratory signal |
| AVA/USDT | P12_200 | 120 | 1.1990 | 0.9892 | 1.1772 | 1.0049 | 0.9704 | exploratory signal |
| AVA/USDT | P12_55 | 211 | 0.9172 | 0.6757 | 0.9075 | -0.6480 | 0.6626 | rejected |
| AVA/USDT | P12_89 | 186 | 1.1025 | 0.8575 | 1.0900 | 0.7072 | 0.8517 | exploratory signal |
| AVA/USDT | P144_200 | 66 | 1.1127 | 0.7519 | 1.1127 | 0.5088 | 0.7617 | exploratory signal |
| AVA/USDT | P20_100 | 147 | 1.1206 | 0.8704 | 1.1206 | 0.7897 | 0.8673 | exploratory signal |
| AVA/USDT | P20_144 | 141 | 1.2457 | 0.9854 | 1.2457 | 1.4228 | 0.9830 | exploratory signal |
| AVA/USDT | P20_200 | 105 | 1.2326 | 1.0120 | 1.2326 | 1.2074 | 1.0142 | exploratory signal |
| AVA/USDT | P20_55 | 182 | 0.9182 | 0.6343 | 0.9182 | -0.5403 | 0.6360 | rejected |
| AVA/USDT | P20_89 | 169 | 1.0824 | 0.8080 | 1.0824 | 0.6213 | 0.8122 | exploratory signal |
| AVA/USDT | P21_100 | 146 | 1.1732 | 0.9113 | 1.1732 | 1.0776 | 0.9090 | exploratory signal |
| AVA/USDT | P21_144 | 141 | 1.2461 | 0.9860 | 1.2461 | 1.4246 | 0.9836 | exploratory signal |
| AVA/USDT | P21_200 | 105 | 1.2324 | 1.0117 | 1.2324 | 1.2067 | 1.0139 | exploratory signal |
| AVA/USDT | P21_89 | 160 | 1.0929 | 0.8173 | 1.0929 | 0.6691 | 0.8214 | exploratory signal |
| AVA/USDT | P26_100 | 153 | 1.2522 | 0.9608 | 1.2522 | 1.5255 | 0.9604 | exploratory signal |
| AVA/USDT | P26_144 | 152 | 1.1382 | 0.8893 | 1.1382 | 0.8970 | 0.8859 | exploratory signal |
| AVA/USDT | P26_200 | 99 | 1.2616 | 1.0341 | 1.2616 | 1.2779 | 1.0338 | exploratory signal |
| AVA/USDT | P26_89 | 161 | 1.2879 | 0.9658 | 1.2879 | 1.7737 | 0.9717 | exploratory signal |
| AVA/USDT | P34_100 | 171 | 1.0352 | 0.7572 | 1.0352 | 0.3140 | 0.7614 | exploratory signal |
| AVA/USDT | P34_144 | 142 | 1.1746 | 0.8929 | 1.1746 | 1.0560 | 0.8884 | exploratory signal |
| AVA/USDT | P34_200 | 97 | 1.3090 | 1.0502 | 1.3090 | 1.4280 | 1.0465 | exploratory signal |
| AVA/USDT | P34_50 | 103 | 0.9804 | 0.6073 | 0.9804 | -0.0536 | 0.6156 | rejected |
| AVA/USDT | P34_89 | 176 | 1.0958 | 0.7861 | 1.0958 | 0.7207 | 0.7920 | exploratory signal |
| AVA/USDT | P50_144 | 129 | 1.1000 | 0.8152 | 1.1000 | 0.6164 | 0.8090 | exploratory signal |
| AVA/USDT | P50_200 | 88 | 1.3796 | 1.0974 | 1.3796 | 1.6157 | 1.0947 | exploratory signal |
| AVA/USDT | P55_144 | 132 | 1.0175 | 0.7539 | 1.0175 | 0.1651 | 0.7516 | exploratory signal |
| AVA/USDT | P55_200 | 94 | 1.2408 | 0.9881 | 1.2408 | 1.1506 | 0.9884 | exploratory signal |
| AVA/USDT | P89_200 | 104 | 0.9972 | 0.7648 | 0.9972 | 0.0395 | 0.7611 | rejected |
| AVA/USDT | P8_100 | 138 | 1.2145 | 0.9790 | 1.1956 | 1.1992 | 0.9699 | exploratory signal |
| AVA/USDT | P8_144 | 95 | 1.1780 | 0.9590 | 1.1506 | 0.7728 | 0.9347 | exploratory signal |
| AVA/USDT | P8_50 | 246 | 0.9509 | 0.7076 | 0.9423 | -0.3999 | 0.6948 | rejected |
| AVA/USDT | P8_55 | 221 | 0.9512 | 0.7127 | 0.9415 | -0.3770 | 0.6957 | rejected |
| AVA/USDT | P8_89 | 156 | 1.1377 | 0.9031 | 1.1227 | 0.8698 | 0.9025 | exploratory signal |
| AXS/USDT | P100_200 | 89 | 0.9909 | 0.7316 | 0.9909 | 0.0044 | 0.7372 | rejected |
| AXS/USDT | P21_100 | 154 | 0.9345 | 0.7193 | 0.9345 | -0.4115 | 0.7338 | rejected |
| AXS/USDT | P21_144 | 132 | 0.9015 | 0.7094 | 0.9015 | -0.5924 | 0.7168 | rejected |
| AXS/USDT | P21_89 | 164 | 0.9253 | 0.6963 | 0.9253 | -0.4971 | 0.7120 | rejected |
| AXS/USDT | P26_100 | 146 | 0.9149 | 0.6971 | 0.9149 | -0.5653 | 0.7170 | rejected |
| AXS/USDT | P26_144 | 132 | 0.9902 | 0.7805 | 0.9902 | -0.0021 | 0.7909 | rejected |
| AXS/USDT | P34_100 | 125 | 0.9037 | 0.6711 | 0.9037 | -0.5683 | 0.6827 | rejected |
| AXS/USDT | P34_200 | 114 | 0.9083 | 0.7003 | 0.9083 | -0.4856 | 0.7029 | rejected |
| AXS/USDT | P50_200 | 108 | 0.9471 | 0.7155 | 0.9471 | -0.2430 | 0.7185 | rejected |
| AXS/USDT | P55_144 | 121 | 0.9012 | 0.6460 | 0.9012 | -0.5521 | 0.6512 | rejected |
| AXS/USDT | P55_200 | 104 | 0.9933 | 0.7506 | 0.9933 | 0.0180 | 0.7542 | rejected |
| AXS/USDT | P8_144 | 117 | 1.0257 | 0.8318 | 1.0257 | 0.2062 | 0.8378 | exploratory signal |
| AXS/USDT | P8_200 | 94 | 0.9503 | 0.7797 | 0.9135 | -0.4314 | 0.7458 | rejected |
| BAND/USDT | P34_200 | 114 | 1.0768 | 0.8219 | 1.0768 | 0.4605 | 0.8164 | exploratory signal |
| BAT/USDT | P12_144 | 120 | 0.9193 | 0.7287 | 0.9296 | -0.3768 | 0.7430 | rejected |
| BAT/USDT | P20_200 | 114 | 0.9124 | 0.7436 | 0.9581 | -0.1823 | 0.7773 | rejected |
| BAT/USDT | P21_200 | 113 | 0.9672 | 0.7878 | 1.0119 | 0.1244 | 0.8208 | exploratory signal |
| BAT/USDT | P26_200 | 93 | 0.9795 | 0.8128 | 0.9712 | -0.0983 | 0.8045 | rejected |
| BAT/USDT | P34_200 | 97 | 0.9174 | 0.7507 | 0.9320 | -0.3193 | 0.7618 | rejected |
| BAT/USDT | P55_200 | 111 | 0.9056 | 0.6958 | 0.9391 | -0.2949 | 0.7247 | rejected |
| BAT/USDT | P8_200 | 70 | 1.0088 | 0.8388 | 1.1773 | 0.8246 | 0.9860 | exploratory signal |
| BCH/USDT | P26_200 | 44 | 0.9868 | 0.8229 | 0.9868 | -0.0099 | 0.8171 | rejected |
| BCH/USDT | P34_200 | 39 | 0.9621 | 0.8072 | 0.9621 | -0.0907 | 0.8005 | rejected |
| BICO/USDT | P8_100 | 186 | 0.9522 | 0.8028 | 0.9545 | -0.2881 | 0.8069 | rejected |
| BICO/USDT | P8_144 | 141 | 1.0841 | 0.9177 | 1.1111 | 0.7440 | 0.9425 | exploratory signal |
| BICO/USDT | P8_200 | 120 | 1.0803 | 0.9378 | 1.1122 | 0.6955 | 0.9662 | exploratory signal |
| BIGTIME/USDT | P12_200 | 104 | 0.9441 | 0.7580 | 0.9512 | -0.2212 | 0.7620 | rejected |
| BIGTIME/USDT | P8_144 | 95 | 0.9147 | 0.7437 | 0.9268 | -0.3500 | 0.7539 | rejected |
| BIGTIME/USDT | P8_200 | 62 | 1.1321 | 0.9601 | 1.0801 | 0.3762 | 0.9065 | exploratory signal |
| BLUR/USDT | P12_144 | 103 | 1.3034 | 1.0910 | 1.3406 | 1.6906 | 1.1106 | exploratory signal |
| BLUR/USDT | P12_200 | 86 | 1.2755 | 1.0907 | 1.3084 | 1.4079 | 1.1201 | exploratory signal |
| BLUR/USDT | P20_200 | 88 | 1.1455 | 0.9766 | 1.1455 | 0.7291 | 0.9780 | exploratory signal |
| BLUR/USDT | P21_200 | 90 | 1.1885 | 1.0111 | 1.1885 | 0.9218 | 1.0125 | exploratory signal |
| BLUR/USDT | P26_200 | 84 | 1.0965 | 0.9309 | 1.0965 | 0.5162 | 0.9367 | exploratory signal |
| BLUR/USDT | P34_200 | 89 | 1.1690 | 0.9992 | 1.1690 | 0.8438 | 1.0017 | exploratory signal |
| BLUR/USDT | P50_200 | 85 | 1.1248 | 0.9551 | 1.1248 | 0.6313 | 0.9571 | exploratory signal |
| BLUR/USDT | P55_200 | 88 | 0.9814 | 0.8180 | 0.9814 | -0.0452 | 0.8206 | rejected |
| BLUR/USDT | P8_144 | 112 | 1.2248 | 1.0202 | 1.2691 | 1.4448 | 1.0464 | exploratory signal |
| BLUR/USDT | P8_200 | 83 | 1.2799 | 1.0998 | 1.3389 | 1.4745 | 1.1488 | credible candidate |
| BOME/USDT | P100_144 | 91 | 0.9323 | 0.6737 | 0.9323 | -0.3037 | 0.6769 | rejected |
| BOME/USDT | P100_200 | 88 | 1.1846 | 0.9261 | 1.1846 | 0.8801 | 0.9266 | exploratory signal |
| BOME/USDT | P144_200 | 66 | 0.9903 | 0.7182 | 0.9903 | 0.0013 | 0.7204 | rejected |
| BOME/USDT | P20_144 | 149 | 0.9788 | 0.8203 | 0.9788 | -0.0720 | 0.8187 | rejected |
| BOME/USDT | P21_144 | 145 | 0.9590 | 0.8020 | 0.9590 | -0.1994 | 0.8001 | rejected |
| BOME/USDT | P26_100 | 166 | 0.9721 | 0.7894 | 0.9721 | -0.1174 | 0.7834 | rejected |
| BOME/USDT | P26_144 | 139 | 1.1225 | 0.9371 | 1.1225 | 0.7686 | 0.9342 | exploratory signal |
| BOME/USDT | P26_200 | 112 | 1.2403 | 1.0411 | 1.2403 | 1.2337 | 1.0387 | exploratory signal |
| BOME/USDT | P26_50 | 158 | 0.9346 | 0.6920 | 0.9346 | -0.3837 | 0.6939 | rejected |
| BOME/USDT | P26_89 | 179 | 0.9305 | 0.7392 | 0.9305 | -0.4230 | 0.7347 | rejected |
| BOME/USDT | P34_100 | 164 | 0.9889 | 0.7891 | 0.9889 | -0.0056 | 0.7853 | rejected |
| BOME/USDT | P34_144 | 147 | 1.1072 | 0.9241 | 1.1072 | 0.6996 | 0.9197 | exploratory signal |
| BOME/USDT | P34_200 | 116 | 1.1360 | 0.9495 | 1.1360 | 0.7891 | 0.9518 | exploratory signal |
| BOME/USDT | P34_89 | 182 | 0.9257 | 0.7203 | 0.9257 | -0.4665 | 0.7172 | rejected |
| BOME/USDT | P50_144 | 135 | 0.9263 | 0.7557 | 0.9263 | -0.3981 | 0.7523 | rejected |
| BOME/USDT | P50_200 | 108 | 1.1102 | 0.9199 | 1.1102 | 0.6366 | 0.9227 | exploratory signal |
| BOME/USDT | P55_144 | 139 | 0.9112 | 0.7344 | 0.9112 | -0.5087 | 0.7323 | rejected |
| BOME/USDT | P55_200 | 109 | 0.9415 | 0.7826 | 0.9415 | -0.2858 | 0.7856 | rejected |
| BOME/USDT | P89_200 | 95 | 1.0408 | 0.8253 | 1.0408 | 0.2608 | 0.8286 | exploratory signal |
| BOME/USDT | P8_100 | 198 | 0.9631 | 0.8006 | 0.9631 | -0.1961 | 0.7952 | rejected |
| BOME/USDT | P8_144 | 135 | 0.9144 | 0.7698 | 0.9441 | -0.2978 | 0.7901 | rejected |
| BOME/USDT | P8_200 | 91 | 0.9184 | 0.7754 | 1.0734 | 0.4227 | 0.9183 | exploratory signal |
| BOME/USDT | P8_89 | 206 | 0.9357 | 0.7753 | 0.9357 | -0.4156 | 0.7708 | rejected |
| BONK/USDT | P20_100 | 134 | 0.9032 | 0.7229 | 0.9032 | -0.5213 | 0.7095 | rejected |
| BONK/USDT | P20_144 | 114 | 0.9156 | 0.7513 | 0.9156 | -0.4197 | 0.7426 | rejected |
| BONK/USDT | P20_200 | 107 | 0.9053 | 0.7443 | 0.9053 | -0.4539 | 0.7318 | rejected |
| BONK/USDT | P21_100 | 127 | 0.9580 | 0.7662 | 0.9580 | -0.1796 | 0.7530 | rejected |
| BONK/USDT | P26_100 | 126 | 0.9439 | 0.7529 | 0.9439 | -0.2755 | 0.7485 | rejected |
| BONK/USDT | P26_144 | 104 | 0.9712 | 0.8025 | 0.9712 | -0.0975 | 0.7950 | rejected |
| BONK/USDT | P34_100 | 119 | 0.9241 | 0.7221 | 0.9241 | -0.4086 | 0.7264 | rejected |
| BONK/USDT | P34_144 | 103 | 1.0084 | 0.8078 | 1.0084 | 0.0978 | 0.8035 | exploratory signal |
| BONK/USDT | P34_200 | 85 | 0.9017 | 0.7497 | 0.9017 | -0.4366 | 0.7429 | rejected |
| BONK/USDT | P50_89 | 103 | 0.9032 | 0.6860 | 0.9032 | -0.4805 | 0.6820 | rejected |
| BONK/USDT | P89_100 | 30 | 1.0598 | 0.7467 | 1.0598 | 0.1934 | 0.7436 | exploratory signal |
| BRETT/USDT | P12_144 | 72 | 1.0740 | 0.9195 | 1.0306 | 0.2080 | 0.8803 | exploratory signal |
| BRETT/USDT | P12_200 | 64 | 0.9452 | 0.8263 | 0.9443 | -0.2187 | 0.8309 | rejected |
| BRETT/USDT | P12_34 | 211 | 0.9062 | 0.6961 | 0.9062 | -0.7341 | 0.7053 | rejected |
| BRETT/USDT | P26_144 | 102 | 0.9131 | 0.7652 | 0.9009 | -0.5709 | 0.7557 | rejected |
| BRETT/USDT | P26_200 | 62 | 1.0034 | 0.8731 | 1.0333 | 0.1916 | 0.9048 | exploratory signal |
| BRETT/USDT | P34_200 | 64 | 0.9891 | 0.8512 | 0.9863 | -0.0196 | 0.8564 | rejected |
| BRETT/USDT | P8_144 | 78 | 1.2444 | 1.0708 | 1.1688 | 0.8800 | 1.0004 | exploratory signal |
| BRETT/USDT | P8_200 | 42 | 1.6802 | 1.5168 | 1.6888 | 1.9493 | 1.5322 | exploratory signal |
| CAKE/USDT | P55_200 | 115 | 0.9800 | 0.6683 | 0.9800 | -0.0578 | 0.6745 | rejected |
| CATI/USDT | P12_144 | 77 | 0.9195 | 0.8070 | 0.9195 | -0.3750 | 0.8057 | rejected |
| CATI/USDT | P12_200 | 72 | 0.9587 | 0.8493 | 0.9587 | -0.1613 | 0.8502 | rejected |
| CATI/USDT | P21_100 | 136 | 0.9799 | 0.7684 | 0.9799 | -0.0695 | 0.7676 | rejected |
| CATI/USDT | P21_89 | 130 | 0.9919 | 0.7748 | 0.9919 | 0.0138 | 0.7711 | rejected |
| CATI/USDT | P26_100 | 122 | 0.9442 | 0.7178 | 0.9442 | -0.3044 | 0.7169 | rejected |
| CATI/USDT | P26_144 | 104 | 0.9150 | 0.7305 | 0.9150 | -0.4763 | 0.7333 | rejected |
| CATI/USDT | P26_89 | 119 | 0.9435 | 0.7236 | 0.9435 | -0.2915 | 0.7160 | rejected |
| CATI/USDT | P8_200 | 70 | 0.9004 | 0.7903 | 0.9004 | -0.4774 | 0.7930 | rejected |
| CETUS/USDT | P12_144 | 117 | 1.0814 | 0.9010 | 1.0814 | 0.4844 | 0.8901 | exploratory signal |
| CETUS/USDT | P12_200 | 68 | 1.2746 | 1.1305 | 1.2746 | 1.1335 | 1.1338 | credible candidate |
| CETUS/USDT | P20_144 | 114 | 0.9203 | 0.7654 | 0.9040 | -0.5084 | 0.7497 | rejected |
| CETUS/USDT | P20_200 | 92 | 1.0708 | 0.9231 | 1.0472 | 0.2898 | 0.9045 | exploratory signal |
| CETUS/USDT | P21_200 | 94 | 1.0651 | 0.9180 | 1.0423 | 0.2688 | 0.9004 | exploratory signal |
| CETUS/USDT | P26_200 | 73 | 1.0568 | 0.9201 | 1.0568 | 0.2985 | 0.9203 | exploratory signal |
| CETUS/USDT | P8_144 | 134 | 1.1676 | 0.9753 | 1.1487 | 0.8867 | 0.9535 | exploratory signal |
| CETUS/USDT | P8_200 | 85 | 1.4565 | 1.2715 | 1.4174 | 1.7508 | 1.2401 | credible candidate |
| CFG/USDT | P50_55 | 55 | 1.2457 | 0.8697 | 1.2457 | 0.8515 | 0.8599 | exploratory signal |
| CFG/USDT | P55_100 | 123 | 0.9040 | 0.6933 | 0.9040 | -0.5489 | 0.6980 | rejected |
| CFG/USDT | P55_144 | 137 | 0.9047 | 0.7317 | 0.9047 | -0.5636 | 0.7330 | rejected |
| CGPT/USDT | P12_200 | 78 | 0.9117 | 0.7825 | 0.9117 | -0.3958 | 0.7840 | rejected |
| CGPT/USDT | P8_144 | 152 | 0.9189 | 0.7556 | 0.9189 | -0.4933 | 0.7584 | rejected |
| CGPT/USDT | P8_89 | 214 | 0.9492 | 0.7472 | 0.9492 | -0.3210 | 0.7468 | rejected |
| CHR/USDT | P100_144 | 97 | 1.0238 | 0.7321 | 1.0238 | 0.1792 | 0.7446 | exploratory signal |
| CHR/USDT | P100_200 | 103 | 0.9661 | 0.7568 | 0.9661 | -0.1372 | 0.7632 | rejected |
| CHR/USDT | P12_144 | 108 | 0.9482 | 0.8067 | 0.8853 | -0.6326 | 0.7458 | rejected |
| CHR/USDT | P12_200 | 88 | 1.1033 | 0.9701 | 1.1141 | 0.6155 | 0.9676 | exploratory signal |
| CHR/USDT | P20_144 | 115 | 0.9361 | 0.7799 | 0.9361 | -0.3142 | 0.7777 | rejected |
| CHR/USDT | P20_200 | 74 | 1.0845 | 0.9458 | 1.1313 | 0.6443 | 0.9750 | exploratory signal |
| CHR/USDT | P21_144 | 110 | 0.9606 | 0.8019 | 0.9606 | -0.1642 | 0.7990 | rejected |
| CHR/USDT | P21_200 | 70 | 1.1069 | 0.9715 | 1.1034 | 0.5081 | 0.9615 | exploratory signal |
| CHR/USDT | P26_200 | 96 | 0.9377 | 0.8044 | 0.9377 | -0.2996 | 0.8107 | rejected |
| CHR/USDT | P34_200 | 97 | 1.1662 | 0.9972 | 1.1662 | 0.8772 | 1.0019 | exploratory signal |
| CHR/USDT | P50_200 | 110 | 1.0970 | 0.8978 | 1.0970 | 0.5785 | 0.9014 | exploratory signal |
| CHR/USDT | P55_200 | 108 | 1.1339 | 0.9269 | 1.1339 | 0.7548 | 0.9298 | exploratory signal |
| CHR/USDT | P89_144 | 113 | 1.0337 | 0.7603 | 1.0337 | 0.2560 | 0.7789 | exploratory signal |
| CHR/USDT | P89_200 | 108 | 0.9475 | 0.7485 | 0.9475 | -0.2526 | 0.7549 | rejected |
| CHR/USDT | P8_144 | 119 | 0.9230 | 0.7869 | 0.8626 | -0.8028 | 0.7220 | rejected |
| CHR/USDT | P8_200 | 92 | 0.9876 | 0.8573 | 1.0015 | 0.0615 | 0.8571 | exploratory signal |
| CHZ/USDT | P12_100 | 159 | 0.9485 | 0.7800 | 0.9485 | -0.2875 | 0.7812 | rejected |
| CHZ/USDT | P12_144 | 112 | 1.0939 | 0.9225 | 1.0508 | 0.3457 | 0.8831 | exploratory signal |
| CHZ/USDT | P12_200 | 87 | 1.0371 | 0.8952 | 1.0202 | 0.1549 | 0.8807 | exploratory signal |
| CHZ/USDT | P12_89 | 167 | 1.0372 | 0.8507 | 1.0372 | 0.3143 | 0.8495 | exploratory signal |
| CHZ/USDT | P20_144 | 111 | 0.9590 | 0.8042 | 0.9590 | -0.1747 | 0.8020 | rejected |
| CHZ/USDT | P20_200 | 89 | 0.9540 | 0.7987 | 0.9051 | -0.4606 | 0.7564 | rejected |
| CHZ/USDT | P21_144 | 128 | 0.9140 | 0.7567 | 0.9140 | -0.4721 | 0.7543 | rejected |
| CHZ/USDT | P21_200 | 87 | 0.9141 | 0.7653 | 0.8689 | -0.6671 | 0.7266 | rejected |
| CHZ/USDT | P26_144 | 123 | 1.0197 | 0.8324 | 1.0197 | 0.1709 | 0.8295 | exploratory signal |
| CHZ/USDT | P26_200 | 87 | 1.0428 | 0.8645 | 0.9414 | -0.2511 | 0.7784 | rejected |
| CHZ/USDT | P34_144 | 125 | 0.9345 | 0.7526 | 0.9345 | -0.3329 | 0.7488 | rejected |
| CHZ/USDT | P34_200 | 92 | 1.0672 | 0.8971 | 1.0672 | 0.3800 | 0.8970 | exploratory signal |
| CHZ/USDT | P50_200 | 89 | 0.9963 | 0.8351 | 0.9963 | 0.0313 | 0.8377 | rejected |
| CHZ/USDT | P55_200 | 89 | 0.9379 | 0.7729 | 0.9379 | -0.2742 | 0.7752 | rejected |
| CHZ/USDT | P8_144 | 111 | 1.0702 | 0.8976 | 1.0286 | 0.2225 | 0.8619 | exploratory signal |
| CHZ/USDT | P8_200 | 66 | 1.2395 | 1.0876 | 1.1137 | 0.5232 | 0.9676 | exploratory signal |
| CHZ/USDT | P8_89 | 165 | 0.9201 | 0.7609 | 0.9146 | -0.5336 | 0.7522 | rejected |
| CKB/USDT | P26_144 | 141 | 0.9288 | 0.6755 | 0.9288 | -0.3799 | 0.6670 | rejected |
| COMP/USDT | P12_100 | 171 | 0.9262 | 0.6816 | 0.9262 | -0.4839 | 0.6928 | rejected |
| COMP/USDT | P12_200 | 127 | 0.9247 | 0.7089 | 0.9535 | -0.2307 | 0.7412 | rejected |
| COMP/USDT | P20_55 | 241 | 0.9159 | 0.5642 | 0.9159 | -0.6572 | 0.5789 | rejected |
| COMP/USDT | P21_55 | 237 | 0.9089 | 0.5610 | 0.9089 | -0.7201 | 0.5770 | rejected |
| COMP/USDT | P26_200 | 128 | 0.9230 | 0.6972 | 0.9080 | -0.5107 | 0.6874 | rejected |
| COTI/USDT | P100_144 | 77 | 0.9340 | 0.6452 | 0.9340 | -0.2579 | 0.6388 | rejected |
| COTI/USDT | P12_144 | 162 | 0.9318 | 0.7711 | 0.9428 | -0.3246 | 0.7775 | rejected |
| COTI/USDT | P20_144 | 150 | 0.9090 | 0.7455 | 0.9090 | -0.5595 | 0.7457 | rejected |
| COTI/USDT | P26_100 | 188 | 0.9240 | 0.7192 | 0.9240 | -0.5331 | 0.7282 | rejected |
| COTI/USDT | P26_144 | 152 | 1.1307 | 0.9118 | 1.1307 | 0.8868 | 0.9164 | exploratory signal |
| COTI/USDT | P26_200 | 124 | 1.1006 | 0.9047 | 1.1901 | 1.1385 | 0.9866 | exploratory signal |
| COTI/USDT | P34_144 | 123 | 1.0570 | 0.8483 | 1.0570 | 0.4002 | 0.8569 | exploratory signal |
| COTI/USDT | P34_200 | 105 | 1.1485 | 0.9478 | 1.1786 | 0.9670 | 0.9764 | exploratory signal |
| COTI/USDT | P50_100 | 118 | 0.9713 | 0.7163 | 0.9713 | -0.1155 | 0.7237 | rejected |
| COTI/USDT | P50_144 | 115 | 1.2656 | 1.0100 | 1.2656 | 1.4546 | 1.0217 | exploratory signal |
| COTI/USDT | P50_200 | 99 | 1.3026 | 1.0675 | 1.3026 | 1.4852 | 1.0758 | exploratory signal |
| COTI/USDT | P55_100 | 111 | 0.9242 | 0.6695 | 0.9242 | -0.4040 | 0.6798 | rejected |
| COTI/USDT | P55_144 | 112 | 1.2911 | 1.0220 | 1.2911 | 1.5520 | 1.0354 | exploratory signal |
| COTI/USDT | P55_200 | 97 | 1.1543 | 0.9413 | 1.1543 | 0.8144 | 0.9446 | exploratory signal |
| COTI/USDT | P8_100 | 194 | 1.0153 | 0.8361 | 0.9938 | 0.0307 | 0.8076 | rejected |
| COTI/USDT | P8_144 | 159 | 0.9273 | 0.7691 | 0.9480 | -0.2974 | 0.7877 | rejected |
| COTI/USDT | P8_89 | 210 | 0.9149 | 0.7484 | 0.9149 | -0.5663 | 0.7376 | rejected |
| CRO/USDT | P21_200 | 94 | 0.9164 | 0.6455 | 0.9164 | -0.3692 | 0.6362 | rejected |
| CRO/USDT | P26_200 | 100 | 0.9522 | 0.6869 | 0.9522 | -0.1984 | 0.6818 | rejected |
| CRO/USDT | P34_200 | 101 | 0.9101 | 0.6459 | 0.9101 | -0.4102 | 0.6283 | rejected |
| CRV/USDT | P12_26 | 143 | 0.9727 | 0.6749 | 0.9727 | -0.1034 | 0.6665 | rejected |
| CRV/USDT | P21_34 | 77 | 0.9201 | 0.6227 | 0.9201 | -0.3313 | 0.6213 | rejected |
| CRV/USDT | P89_100 | 31 | 1.0942 | 0.7443 | 1.0942 | 0.2927 | 0.7497 | exploratory signal |
| CTC/USDT | P12_144 | 158 | 0.9271 | 0.7359 | 0.9271 | -0.4039 | 0.7218 | rejected |
| CTC/USDT | P12_200 | 131 | 1.0703 | 0.8691 | 1.0512 | 0.3523 | 0.8438 | exploratory signal |
| CTC/USDT | P20_144 | 132 | 0.9222 | 0.7238 | 0.9054 | -0.5207 | 0.7012 | rejected |
| CTC/USDT | P21_144 | 132 | 0.9231 | 0.7239 | 0.9231 | -0.4026 | 0.7134 | rejected |
| CTC/USDT | P50_200 | 107 | 0.9106 | 0.6783 | 0.9106 | -0.4519 | 0.6759 | rejected |
| CTC/USDT | P8_200 | 123 | 0.9509 | 0.7727 | 0.9327 | -0.3294 | 0.7463 | rejected |
| CTSI/USDT | P8_200 | 95 | 0.9630 | 0.7470 | 1.0115 | 0.1150 | 0.7969 | exploratory signal |
| CVX/USDT | P20_21 | 56 | 0.9601 | 0.6355 | 0.9601 | -0.1174 | 0.6335 | rejected |
| CVX/USDT | P20_26 | 82 | 0.9309 | 0.6022 | 0.9309 | -0.2815 | 0.5972 | rejected |
| CYBER/USDT | P100_144 | 87 | 1.0595 | 0.6429 | 1.0595 | 0.3257 | 0.6528 | exploratory signal |
| CYBER/USDT | P89_144 | 97 | 1.1211 | 0.7122 | 1.1211 | 0.6365 | 0.7217 | exploratory signal |
| DAG/USDT | P100_200 | 49 | 1.1811 | 0.8757 | 1.2611 | 0.8887 | 0.9370 | exploratory signal |
| DAG/USDT | P12_100 | 108 | 1.0618 | 0.8605 | 1.0618 | 0.3786 | 0.8560 | exploratory signal |
| DAG/USDT | P12_200 | 93 | 0.9014 | 0.7565 | 0.9407 | -0.2569 | 0.7853 | rejected |
| DAG/USDT | P12_50 | 132 | 0.9234 | 0.6374 | 0.9234 | -0.3955 | 0.6251 | rejected |
| DAG/USDT | P12_89 | 124 | 0.9257 | 0.7244 | 0.9257 | -0.3795 | 0.7176 | rejected |
| DAG/USDT | P20_100 | 100 | 1.0053 | 0.7812 | 1.0053 | 0.0789 | 0.7682 | exploratory signal |
| DAG/USDT | P20_144 | 93 | 0.9469 | 0.7654 | 0.9818 | -0.0422 | 0.7879 | rejected |
| DAG/USDT | P20_200 | 69 | 1.0787 | 0.9292 | 1.1331 | 0.5947 | 0.9737 | exploratory signal |
| DAG/USDT | P20_89 | 105 | 0.9060 | 0.6803 | 0.9060 | -0.4501 | 0.6705 | rejected |
| DAG/USDT | P21_100 | 100 | 0.9110 | 0.7096 | 0.9110 | -0.4136 | 0.6999 | rejected |
| DAG/USDT | P21_144 | 92 | 0.9271 | 0.7491 | 0.9621 | -0.1460 | 0.7721 | rejected |
| DAG/USDT | P21_200 | 83 | 0.9065 | 0.7567 | 0.9500 | -0.1951 | 0.7879 | rejected |
| DAG/USDT | P26_144 | 77 | 0.9004 | 0.7449 | 0.9625 | -0.1306 | 0.7843 | rejected |
| DAG/USDT | P34_144 | 70 | 1.0421 | 0.8429 | 1.0693 | 0.3349 | 0.8606 | exploratory signal |
| DAG/USDT | P34_200 | 70 | 1.0854 | 0.9138 | 1.1143 | 0.5144 | 0.9348 | exploratory signal |
| DAG/USDT | P50_200 | 62 | 1.0165 | 0.8261 | 1.0471 | 0.2380 | 0.8561 | exploratory signal |
| DAG/USDT | P89_144 | 48 | 0.9443 | 0.6287 | 1.0109 | 0.0773 | 0.6702 | exploratory signal |
| DAG/USDT | P89_200 | 51 | 0.9397 | 0.7259 | 1.0078 | 0.0692 | 0.7843 | exploratory signal |
| DAG/USDT | P8_100 | 109 | 1.3177 | 1.0644 | 1.3177 | 1.5113 | 1.0588 | exploratory signal |
| DAG/USDT | P8_144 | 97 | 1.0180 | 0.8528 | 1.0054 | 0.0816 | 0.8360 | exploratory signal |
| DAG/USDT | P8_200 | 89 | 0.9907 | 0.8278 | 1.0563 | 0.3175 | 0.8768 | exploratory signal |
| DAG/USDT | P8_50 | 156 | 1.0665 | 0.7615 | 1.0665 | 0.4691 | 0.7487 | exploratory signal |
| DAG/USDT | P8_55 | 131 | 1.0328 | 0.7936 | 1.0328 | 0.2451 | 0.7809 | exploratory signal |
| DAG/USDT | P8_89 | 121 | 1.0377 | 0.8296 | 1.0377 | 0.2670 | 0.8252 | exploratory signal |
| DASH/USDT | P12_26 | 136 | 0.9032 | 0.6863 | 0.9032 | -0.6070 | 0.6980 | rejected |
| DCR/USDT | P12_144 | 159 | 0.9473 | 0.7749 | 0.9444 | -0.3109 | 0.7742 | rejected |
| DCR/USDT | P20_144 | 143 | 0.9288 | 0.7514 | 0.9936 | 0.0255 | 0.8040 | rejected |
| DCR/USDT | P21_144 | 151 | 1.0081 | 0.8196 | 1.0081 | 0.1155 | 0.8149 | exploratory signal |
| DCR/USDT | P21_200 | 132 | 0.9299 | 0.7817 | 0.9299 | -0.3453 | 0.7710 | rejected |
| DEEP/USDT | P100_200 | 74 | 1.1016 | 0.8743 | 1.1295 | 0.6617 | 0.8970 | exploratory signal |
| DEEP/USDT | P12_200 | 43 | 0.9873 | 0.8125 | 0.9520 | -0.1730 | 0.7953 | rejected |
| DEEP/USDT | P144_200 | 46 | 1.1846 | 0.9028 | 1.1846 | 0.7148 | 0.9053 | exploratory signal |
| DEEP/USDT | P21_26 | 55 | 0.9194 | 0.5881 | 0.9194 | -0.3123 | 0.5866 | rejected |
| DEEP/USDT | P26_200 | 58 | 1.1063 | 0.9493 | 1.1424 | 0.6351 | 0.9787 | exploratory signal |
| DEEP/USDT | P34_144 | 78 | 1.0242 | 0.8634 | 1.0474 | 0.3066 | 0.8891 | exploratory signal |
| DEEP/USDT | P34_200 | 55 | 1.0983 | 0.9391 | 1.1352 | 0.6027 | 0.9725 | exploratory signal |
| DEEP/USDT | P50_200 | 54 | 1.1245 | 0.9451 | 1.1623 | 0.7019 | 0.9789 | exploratory signal |
| DEEP/USDT | P55_200 | 71 | 1.0660 | 0.8881 | 1.0940 | 0.5010 | 0.9126 | exploratory signal |
| DEEP/USDT | P55_89 | 95 | 0.9012 | 0.6431 | 0.9012 | -0.5500 | 0.6476 | rejected |
| DEEP/USDT | P89_200 | 66 | 1.1564 | 0.9251 | 1.1883 | 0.8648 | 0.9518 | exploratory signal |
| DEEP/USDT | P8_26 | 192 | 0.9057 | 0.6600 | 0.9057 | -0.7165 | 0.6603 | rejected |
| DEEP/USDT | P8_89 | 142 | 0.9519 | 0.7982 | 0.9519 | -0.2880 | 0.8027 | rejected |
| DEGEN/USDT | P100_200 | 95 | 0.9215 | 0.7091 | 0.9215 | -0.3837 | 0.7153 | rejected |
| DEGEN/USDT | P20_34 | 132 | 0.9047 | 0.6121 | 0.9047 | -0.5373 | 0.6136 | rejected |
| DEGEN/USDT | P89_200 | 100 | 1.0252 | 0.8035 | 1.0252 | 0.1907 | 0.8111 | exploratory signal |
| DEXE/USDT | P100_144 | 74 | 1.1330 | 0.8844 | 1.1330 | 0.6194 | 0.8857 | exploratory signal |
| DEXE/USDT | P100_200 | 61 | 1.6140 | 1.3740 | 1.6140 | 1.8955 | 1.3617 | exploratory signal |
| DEXE/USDT | P12_100 | 112 | 1.1871 | 1.0349 | 1.1871 | 1.0012 | 1.0307 | exploratory signal |
| DEXE/USDT | P12_144 | 88 | 1.3128 | 1.1594 | 1.2833 | 1.3059 | 1.1198 | exploratory signal |
| DEXE/USDT | P12_200 | 65 | 1.3968 | 1.2667 | 1.3235 | 1.4204 | 1.1782 | exploratory signal |
| DEXE/USDT | P12_89 | 128 | 1.0152 | 0.8671 | 1.0152 | 0.1500 | 0.8635 | exploratory signal |
| DEXE/USDT | P20_100 | 121 | 1.0042 | 0.8558 | 1.0042 | 0.0828 | 0.8518 | exploratory signal |
| DEXE/USDT | P20_144 | 90 | 1.2391 | 1.0938 | 1.2489 | 1.1870 | 1.0920 | exploratory signal |
| DEXE/USDT | P20_200 | 66 | 1.6404 | 1.4926 | 1.3381 | 1.4680 | 1.1830 | exploratory signal |
| DEXE/USDT | P20_89 | 125 | 0.9566 | 0.8061 | 0.9566 | -0.1949 | 0.7976 | rejected |
| DEXE/USDT | P21_100 | 120 | 0.9883 | 0.8419 | 0.9883 | -0.0090 | 0.8379 | rejected |
| DEXE/USDT | P21_144 | 89 | 1.2166 | 1.0751 | 1.2278 | 1.0952 | 1.0745 | exploratory signal |
| DEXE/USDT | P21_200 | 64 | 1.6713 | 1.5219 | 1.3506 | 1.4994 | 1.1946 | exploratory signal |
| DEXE/USDT | P21_89 | 123 | 0.9920 | 0.8355 | 0.9920 | 0.0132 | 0.8293 | rejected |
| DEXE/USDT | P26_100 | 117 | 1.0430 | 0.8903 | 1.0430 | 0.2958 | 0.8872 | exploratory signal |
| DEXE/USDT | P26_144 | 82 | 1.0999 | 0.9753 | 1.1393 | 0.7059 | 1.0002 | exploratory signal |
| DEXE/USDT | P26_200 | 63 | 1.2401 | 1.1233 | 1.2250 | 1.0428 | 1.0851 | exploratory signal |
| DEXE/USDT | P26_89 | 124 | 0.9004 | 0.7532 | 0.9004 | -0.5443 | 0.7480 | rejected |
| DEXE/USDT | P34_100 | 112 | 1.1391 | 0.9523 | 1.1391 | 0.7865 | 0.9519 | exploratory signal |
| DEXE/USDT | P34_144 | 88 | 1.2222 | 1.0632 | 1.2222 | 1.0586 | 1.0649 | exploratory signal |
| DEXE/USDT | P34_200 | 73 | 1.0315 | 0.9060 | 1.1888 | 0.8662 | 1.0460 | exploratory signal |
| DEXE/USDT | P34_89 | 112 | 1.0136 | 0.8385 | 1.0136 | 0.1317 | 0.8355 | exploratory signal |
| DEXE/USDT | P50_100 | 111 | 1.1013 | 0.9000 | 1.1013 | 0.5725 | 0.8917 | exploratory signal |
| DEXE/USDT | P50_144 | 89 | 1.4465 | 1.2605 | 1.4465 | 1.8547 | 1.2581 | exploratory signal |
| DEXE/USDT | P50_200 | 70 | 1.7875 | 1.5833 | 1.8239 | 2.5632 | 1.6091 | exploratory signal |
| DEXE/USDT | P55_100 | 102 | 1.1891 | 0.9580 | 1.1891 | 0.9369 | 0.9479 | exploratory signal |
| DEXE/USDT | P55_144 | 76 | 1.5373 | 1.3363 | 1.4671 | 1.8373 | 1.2660 | exploratory signal |
| DEXE/USDT | P55_200 | 63 | 1.8907 | 1.6783 | 1.9333 | 2.6319 | 1.7085 | exploratory signal |
| DEXE/USDT | P89_144 | 88 | 1.0885 | 0.8514 | 1.0623 | 0.3613 | 0.8365 | exploratory signal |
| DEXE/USDT | P89_200 | 56 | 1.7875 | 1.5267 | 1.7448 | 2.1281 | 1.4799 | exploratory signal |
| DEXE/USDT | P8_100 | 114 | 1.2379 | 1.0947 | 1.2388 | 1.2518 | 1.0877 | exploratory signal |
| DEXE/USDT | P8_144 | 83 | 1.5518 | 1.4012 | 1.6286 | 2.4762 | 1.4581 | exploratory signal |
| DEXE/USDT | P8_20 | 164 | 0.9040 | 0.6860 | 0.9040 | -0.6092 | 0.6828 | rejected |
| DEXE/USDT | P8_200 | 56 | 1.3520 | 1.2415 | 1.2721 | 1.1854 | 1.1409 | exploratory signal |
| DEXE/USDT | P8_50 | 171 | 0.9082 | 0.7573 | 0.9082 | -0.5841 | 0.7514 | rejected |
| DEXE/USDT | P8_55 | 157 | 0.9460 | 0.7947 | 0.9460 | -0.2950 | 0.7886 | rejected |
| DEXE/USDT | P8_89 | 133 | 1.0608 | 0.9177 | 1.0577 | 0.4112 | 0.9052 | exploratory signal |
| DIA/USDT | P12_200 | 84 | 1.4204 | 1.1836 | 1.5029 | 2.0308 | 1.2510 | exploratory signal |
| DIA/USDT | P20_200 | 122 | 1.2927 | 1.0444 | 1.3064 | 1.5725 | 1.0449 | exploratory signal |
| DIA/USDT | P21_200 | 120 | 1.3037 | 1.0515 | 1.3177 | 1.6016 | 1.0516 | exploratory signal |
| DIA/USDT | P26_200 | 114 | 1.2413 | 1.0018 | 1.2789 | 1.3786 | 1.0211 | exploratory signal |
| DIA/USDT | P34_200 | 145 | 0.9205 | 0.7176 | 0.9205 | -0.4357 | 0.7057 | rejected |
| DIA/USDT | P50_200 | 135 | 0.9631 | 0.7443 | 0.9631 | -0.1599 | 0.7354 | rejected |
| DIA/USDT | P55_200 | 126 | 0.9640 | 0.7457 | 0.9640 | -0.1474 | 0.7349 | rejected |
| DIA/USDT | P8_200 | 89 | 1.2169 | 1.0141 | 1.2941 | 1.3743 | 1.0808 | exploratory signal |
| DOGE/USDT | P34_200 | 95 | 1.0586 | 0.7848 | 1.0586 | 0.3348 | 0.7830 | exploratory signal |
| DOGE/USDT | P50_200 | 103 | 1.0720 | 0.7614 | 1.0720 | 0.4029 | 0.7541 | exploratory signal |
| DOGE/USDT | P55_200 | 103 | 0.9930 | 0.7122 | 0.9930 | 0.0166 | 0.7119 | rejected |
| DOGS/USDT | P12_100 | 170 | 1.0026 | 0.7943 | 1.0026 | 0.0943 | 0.7969 | exploratory signal |
| DOGS/USDT | P12_89 | 179 | 1.0656 | 0.8360 | 1.0656 | 0.5537 | 0.8363 | exploratory signal |
| DOGS/USDT | P20_89 | 160 | 0.9976 | 0.7735 | 0.9976 | 0.0549 | 0.7797 | rejected |
| DOGS/USDT | P21_89 | 151 | 0.9693 | 0.7477 | 0.9693 | -0.1524 | 0.7538 | rejected |
| DOGS/USDT | P26_89 | 142 | 0.9558 | 0.7242 | 0.9558 | -0.2449 | 0.7321 | rejected |
| DOGS/USDT | P89_100 | 30 | 1.1941 | 0.8162 | 1.1941 | 0.5730 | 0.8182 | exploratory signal |
| DOGS/USDT | P8_100 | 194 | 0.9574 | 0.7618 | 0.9574 | -0.2625 | 0.7614 | rejected |
| DOGS/USDT | P8_89 | 195 | 0.9582 | 0.7552 | 0.9582 | -0.2660 | 0.7600 | rejected |
| DOT/USDT | P100_200 | 74 | 0.9495 | 0.6859 | 0.9495 | -0.1914 | 0.6894 | rejected |
| DOT/USDT | P12_100 | 148 | 0.9820 | 0.7840 | 0.9820 | -0.0483 | 0.7775 | rejected |
| DOT/USDT | P12_144 | 112 | 1.0280 | 0.8302 | 1.0280 | 0.2119 | 0.8297 | exploratory signal |
| DOT/USDT | P12_89 | 153 | 0.9603 | 0.7638 | 0.9603 | -0.1894 | 0.7573 | rejected |
| DOT/USDT | P20_200 | 83 | 1.0076 | 0.8258 | 1.0076 | 0.0854 | 0.8246 | exploratory signal |
| DOT/USDT | P21_200 | 82 | 1.0858 | 0.8860 | 1.0858 | 0.4476 | 0.8888 | exploratory signal |
| DOT/USDT | P26_200 | 84 | 0.9198 | 0.7409 | 0.9198 | -0.3667 | 0.7439 | rejected |
| DOT/USDT | P34_55 | 88 | 0.9294 | 0.6132 | 0.9294 | -0.3081 | 0.6153 | rejected |
| DOT/USDT | P55_89 | 87 | 0.9051 | 0.6327 | 0.9051 | -0.4387 | 0.6339 | rejected |
| DOT/USDT | P8_144 | 121 | 0.9675 | 0.7897 | 0.9675 | -0.1305 | 0.7854 | rejected |
| DUSK/USDT | P100_200 | 97 | 1.1915 | 0.9751 | 1.1915 | 0.9675 | 0.9788 | exploratory signal |
| DUSK/USDT | P12_200 | 83 | 1.0135 | 0.8989 | 1.0460 | 0.2827 | 0.9305 | exploratory signal |
| DUSK/USDT | P26_144 | 126 | 0.9317 | 0.8088 | 0.9317 | -0.3676 | 0.8109 | rejected |
| DUSK/USDT | P89_200 | 100 | 0.9568 | 0.7958 | 0.9568 | -0.1834 | 0.7984 | rejected |
| DUSK/USDT | P8_200 | 95 | 0.9070 | 0.7960 | 0.9239 | -0.3718 | 0.8122 | rejected |
| DYDX/USDT | P34_200 | 110 | 0.9795 | 0.8148 | 1.0052 | 0.0866 | 0.8370 | exploratory signal |
| DYDX/USDT | P50_200 | 104 | 1.1053 | 0.9034 | 1.1053 | 0.6203 | 0.9135 | exploratory signal |
| DYDX/USDT | P55_200 | 110 | 0.9632 | 0.7741 | 0.9632 | -0.1647 | 0.7849 | rejected |
| EDU/USDT | P20_144 | 144 | 0.9304 | 0.7624 | 0.9304 | -0.4006 | 0.7617 | rejected |
| EDU/USDT | P21_144 | 142 | 0.9346 | 0.7677 | 0.9346 | -0.3657 | 0.7659 | rejected |
| EDU/USDT | P50_144 | 142 | 1.0115 | 0.7780 | 1.0115 | 0.1383 | 0.7859 | exploratory signal |
| EDU/USDT | P55_144 | 133 | 0.9550 | 0.7320 | 0.9550 | -0.2271 | 0.7373 | rejected |
| EGLD/USDT | P100_200 | 86 | 1.0805 | 0.8151 | 1.0805 | 0.4209 | 0.8136 | exploratory signal |
| EGLD/USDT | P12_144 | 147 | 0.9026 | 0.7279 | 0.9026 | -0.5522 | 0.7152 | rejected |
| EGLD/USDT | P12_200 | 134 | 0.9172 | 0.7514 | 0.9172 | -0.4330 | 0.7386 | rejected |
| EGLD/USDT | P144_200 | 64 | 1.0789 | 0.7368 | 1.0789 | 0.3590 | 0.7380 | exploratory signal |
| EGLD/USDT | P20_144 | 128 | 1.0191 | 0.8035 | 1.0191 | 0.1664 | 0.7908 | exploratory signal |
| EGLD/USDT | P21_144 | 130 | 1.0860 | 0.8571 | 1.0860 | 0.5249 | 0.8428 | exploratory signal |
| EGLD/USDT | P21_200 | 119 | 0.9322 | 0.7454 | 0.9283 | -0.3720 | 0.7396 | rejected |
| EGLD/USDT | P26_144 | 139 | 0.9766 | 0.7665 | 0.9766 | -0.0837 | 0.7642 | rejected |
| EGLD/USDT | P26_200 | 124 | 1.0756 | 0.8599 | 1.0756 | 0.4859 | 0.8588 | exploratory signal |
| EGLD/USDT | P34_144 | 128 | 0.9984 | 0.7729 | 0.9984 | 0.0505 | 0.7720 | rejected |
| EGLD/USDT | P34_200 | 116 | 1.0518 | 0.8327 | 1.0518 | 0.3389 | 0.8281 | exploratory signal |
| EGLD/USDT | P50_200 | 101 | 0.9807 | 0.7659 | 0.9807 | -0.0475 | 0.7604 | rejected |
| EGLD/USDT | P55_144 | 111 | 1.0636 | 0.7922 | 1.0636 | 0.4043 | 0.7970 | exploratory signal |
| EGLD/USDT | P55_200 | 99 | 1.3233 | 1.0262 | 1.3233 | 1.4725 | 1.0202 | exploratory signal |
| EGLD/USDT | P89_100 | 46 | 0.9592 | 0.5654 | 0.9592 | -0.1086 | 0.5624 | rejected |
| EGLD/USDT | P89_200 | 90 | 1.0307 | 0.7921 | 1.0307 | 0.1957 | 0.7854 | exploratory signal |
| EIGEN/USDT | P20_34 | 98 | 0.9586 | 0.7222 | 0.9586 | -0.1758 | 0.7131 | rejected |
| EIGEN/USDT | P21_34 | 91 | 0.9065 | 0.6792 | 0.9065 | -0.4674 | 0.6700 | rejected |
| EIGEN/USDT | P26_34 | 56 | 1.0357 | 0.7486 | 1.0357 | 0.1864 | 0.7306 | exploratory signal |
| ENA/USDT | P100_144 | 64 | 1.1290 | 0.8738 | 1.1290 | 0.5378 | 0.8664 | exploratory signal |
| ENA/USDT | P12_100 | 154 | 1.0818 | 0.9176 | 1.0818 | 0.5761 | 0.9164 | exploratory signal |
| ENA/USDT | P12_144 | 133 | 1.0852 | 0.9313 | 1.0852 | 0.5609 | 0.9316 | exploratory signal |
| ENA/USDT | P12_20 | 91 | 1.1715 | 0.8529 | 1.1715 | 0.8347 | 0.8531 | exploratory signal |
| ENA/USDT | P12_200 | 94 | 1.1355 | 0.9836 | 1.1355 | 0.7026 | 0.9841 | exploratory signal |
| ENA/USDT | P12_21 | 100 | 1.0862 | 0.7800 | 1.0862 | 0.4758 | 0.7755 | exploratory signal |
| ENA/USDT | P12_26 | 138 | 0.9438 | 0.7034 | 0.9438 | -0.2851 | 0.6982 | rejected |
| ENA/USDT | P12_55 | 201 | 0.9735 | 0.7869 | 0.9735 | -0.1234 | 0.7850 | rejected |
| ENA/USDT | P12_89 | 178 | 1.0695 | 0.8859 | 1.0695 | 0.5347 | 0.8824 | exploratory signal |
| ENA/USDT | P20_100 | 159 | 1.0201 | 0.8528 | 1.0201 | 0.1965 | 0.8498 | exploratory signal |
| ENA/USDT | P20_144 | 142 | 1.0093 | 0.8525 | 1.0093 | 0.1237 | 0.8582 | exploratory signal |
| ENA/USDT | P20_200 | 106 | 1.2024 | 1.0479 | 1.2024 | 1.0480 | 1.0475 | exploratory signal |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.0315 | 1.3902 | 1.1879 | 1.0324 | credible candidate |
| ENA/USDT | P20_26 | 64 | 1.0942 | 0.8213 | 1.0942 | 0.4192 | 0.8204 | exploratory signal |
| ENA/USDT | P20_34 | 110 | 0.9305 | 0.6963 | 0.9305 | -0.3342 | 0.6922 | rejected |
| ENA/USDT | P20_50 | 165 | 0.9865 | 0.7739 | 0.9865 | -0.0243 | 0.7756 | rejected |
| ENA/USDT | P20_55 | 167 | 1.1176 | 0.8838 | 1.1176 | 0.8308 | 0.8857 | exploratory signal |
| ENA/USDT | P20_89 | 170 | 1.0226 | 0.8361 | 1.0226 | 0.2163 | 0.8293 | exploratory signal |
| ENA/USDT | P21_100 | 154 | 1.0681 | 0.8932 | 1.0681 | 0.4990 | 0.8947 | exploratory signal |
| ENA/USDT | P21_144 | 136 | 1.0170 | 0.8585 | 1.0170 | 0.1710 | 0.8661 | exploratory signal |
| ENA/USDT | P21_200 | 101 | 1.1506 | 1.0041 | 1.1506 | 0.7956 | 1.0043 | exploratory signal |
| ENA/USDT | P21_26 | 52 | 1.1092 | 0.8328 | 1.1092 | 0.4309 | 0.8342 | exploratory signal |
| ENA/USDT | P21_34 | 96 | 0.9131 | 0.6779 | 0.9131 | -0.4039 | 0.6724 | rejected |
| ENA/USDT | P21_50 | 157 | 0.9433 | 0.7349 | 0.9433 | -0.3323 | 0.7405 | rejected |
| ENA/USDT | P21_55 | 159 | 1.0006 | 0.7911 | 1.0006 | 0.0713 | 0.7959 | exploratory signal |
| ENA/USDT | P21_89 | 168 | 0.9521 | 0.7789 | 0.9521 | -0.2637 | 0.7778 | rejected |
| ENA/USDT | P26_100 | 163 | 0.9760 | 0.8041 | 0.9760 | -0.0987 | 0.8066 | rejected |
| ENA/USDT | P26_144 | 126 | 1.1740 | 0.9882 | 1.1740 | 1.0087 | 0.9892 | exploratory signal |
| ENA/USDT | P26_200 | 98 | 1.0938 | 0.9565 | 1.0938 | 0.5154 | 0.9553 | exploratory signal |
| ENA/USDT | P34_100 | 141 | 1.1458 | 0.9333 | 1.1458 | 0.9247 | 0.9372 | exploratory signal |
| ENA/USDT | P34_144 | 111 | 1.2519 | 1.0555 | 1.2519 | 1.3176 | 1.0600 | exploratory signal |
| ENA/USDT | P34_200 | 99 | 0.9287 | 0.8010 | 0.9287 | -0.3400 | 0.8016 | rejected |
| ENA/USDT | P34_89 | 151 | 0.9037 | 0.7137 | 0.9037 | -0.5994 | 0.7167 | rejected |
| ENA/USDT | P50_144 | 98 | 1.0425 | 0.8685 | 1.0425 | 0.2697 | 0.8682 | exploratory signal |
| ENA/USDT | P55_144 | 98 | 1.1759 | 0.9710 | 1.1759 | 0.8831 | 0.9685 | exploratory signal |
| ENA/USDT | P55_200 | 84 | 0.9423 | 0.7913 | 0.9423 | -0.2345 | 0.7890 | rejected |
| ENA/USDT | P89_144 | 72 | 0.9807 | 0.7720 | 0.9807 | -0.0405 | 0.7682 | rejected |
| ENA/USDT | P8_100 | 167 | 1.0216 | 0.8667 | 1.0216 | 0.2101 | 0.8615 | exploratory signal |
| ENA/USDT | P8_12 | 66 | 1.2792 | 0.9252 | 1.2792 | 1.0630 | 0.9228 | exploratory signal |
| ENA/USDT | P8_144 | 123 | 1.2020 | 1.0456 | 1.2020 | 1.1170 | 1.0433 | exploratory signal |
| ENA/USDT | P8_20 | 165 | 0.9327 | 0.6876 | 0.9327 | -0.4110 | 0.6907 | rejected |
| ENA/USDT | P8_200 | 94 | 1.1431 | 0.9973 | 1.1431 | 0.7381 | 0.9980 | exploratory signal |
| ENA/USDT | P8_21 | 179 | 0.9308 | 0.6839 | 0.9308 | -0.4230 | 0.6791 | rejected |
| ENA/USDT | P8_26 | 210 | 0.9481 | 0.7289 | 0.9481 | -0.3410 | 0.7329 | rejected |
| ENA/USDT | P8_34 | 239 | 0.9627 | 0.7549 | 0.9627 | -0.2198 | 0.7485 | rejected |
| ENA/USDT | P8_55 | 219 | 0.9934 | 0.8182 | 0.9934 | 0.0271 | 0.8167 | rejected |
| ENA/USDT | P8_89 | 192 | 0.9741 | 0.8162 | 0.9741 | -0.1160 | 0.8136 | rejected |
| ENJ/USDT | P12_200 | 124 | 0.9496 | 0.7809 | 0.9496 | -0.2381 | 0.7776 | rejected |
| ENJ/USDT | P20_200 | 116 | 0.9116 | 0.7400 | 0.8600 | -0.8357 | 0.7003 | rejected |
| ENJ/USDT | P21_200 | 116 | 0.9157 | 0.7446 | 0.8483 | -0.9284 | 0.6924 | rejected |
| ENJ/USDT | P34_200 | 125 | 0.9493 | 0.7472 | 0.9493 | -0.2585 | 0.7557 | rejected |
| ENJ/USDT | P55_200 | 112 | 0.9145 | 0.7274 | 0.9145 | -0.4487 | 0.7292 | rejected |
| ENJ/USDT | P8_200 | 93 | 1.1393 | 0.9943 | 0.9967 | 0.0361 | 0.8557 | rejected |
| ENS/USDT | P21_200 | 91 | 0.9386 | 0.7428 | 0.9230 | -0.3548 | 0.7232 | rejected |
| ETHFI/USDT | P50_55 | 36 | 0.9372 | 0.6949 | 0.9372 | -0.1783 | 0.7014 | rejected |
| EUL/USDT | P12_100 | 207 | 0.9143 | 0.7590 | 0.9056 | -0.7549 | 0.7655 | rejected |
| EUL/USDT | P12_89 | 222 | 0.9492 | 0.7749 | 0.9405 | -0.4392 | 0.7796 | rejected |
| EUL/USDT | P20_50 | 199 | 0.9596 | 0.7126 | 0.9596 | -0.2469 | 0.7245 | rejected |
| EUL/USDT | P21_200 | 110 | 0.9379 | 0.8125 | 0.9474 | -0.2634 | 0.8232 | rejected |
| EUL/USDT | P21_50 | 195 | 0.9414 | 0.6966 | 0.9414 | -0.3966 | 0.7107 | rejected |
| EUL/USDT | P26_50 | 167 | 0.9177 | 0.6626 | 0.9177 | -0.5429 | 0.6754 | rejected |
| EUL/USDT | P34_50 | 119 | 0.9833 | 0.6891 | 0.9833 | -0.0431 | 0.7029 | rejected |
| EUL/USDT | P8_100 | 211 | 0.9448 | 0.7863 | 0.9357 | -0.4632 | 0.7872 | rejected |
| EUL/USDT | P8_144 | 156 | 0.9221 | 0.7839 | 0.9097 | -0.5661 | 0.7755 | rejected |
| EUL/USDT | P8_200 | 133 | 0.9805 | 0.8329 | 0.9792 | -0.0711 | 0.8372 | rejected |
| EUL/USDT | P8_89 | 219 | 0.9002 | 0.7429 | 0.8916 | -0.8520 | 0.7412 | rejected |
| FET/USDT | P12_144 | 68 | 0.9078 | 0.8098 | 0.9078 | -0.3699 | 0.8075 | rejected |
| FET/USDT | P12_200 | 36 | 1.5616 | 1.4435 | 1.5616 | 1.3738 | 1.4404 | exploratory signal |
| FET/USDT | P20_144 | 95 | 1.0591 | 0.9118 | 1.0591 | 0.3390 | 0.9083 | exploratory signal |
| FET/USDT | P20_200 | 34 | 1.2336 | 1.1324 | 1.2336 | 0.6599 | 1.1306 | exploratory signal |
| FET/USDT | P21_144 | 93 | 1.0197 | 0.8801 | 1.0197 | 0.1469 | 0.8756 | exploratory signal |
| FET/USDT | P21_200 | 39 | 1.1274 | 1.0389 | 1.1274 | 0.4174 | 1.0368 | exploratory signal |
| FET/USDT | P26_144 | 93 | 1.0151 | 0.8685 | 1.0151 | 0.1250 | 0.8640 | exploratory signal |
| FET/USDT | P26_200 | 64 | 0.9106 | 0.8095 | 0.9106 | -0.3415 | 0.8062 | rejected |
| FET/USDT | P8_144 | 95 | 0.9128 | 0.8030 | 0.9128 | -0.4162 | 0.8020 | rejected |
| FET/USDT | P8_200 | 45 | 1.2115 | 1.1200 | 1.2115 | 0.7046 | 1.1183 | exploratory signal |
| FIL/USDT | P89_200 | 86 | 0.9601 | 0.7336 | 0.9356 | -0.2602 | 0.7057 | rejected |
| FIL/USDT | P8_12 | 71 | 1.0516 | 0.7068 | 1.0516 | 0.2631 | 0.7074 | exploratory signal |
| FLOKI/USDT | P100_144 | 92 | 0.9075 | 0.5885 | 0.9075 | -0.4489 | 0.5988 | rejected |
| FLOKI/USDT | P12_200 | 102 | 1.0054 | 0.8220 | 1.0559 | 0.3686 | 0.8679 | exploratory signal |
| FLOKI/USDT | P8_200 | 132 | 0.9839 | 0.8039 | 0.9839 | -0.0369 | 0.8036 | rejected |
| FLOW/USDT | P12_144 | 147 | 0.9569 | 0.8019 | 0.9621 | -0.2005 | 0.8124 | rejected |
| FLOW/USDT | P12_89 | 196 | 0.9104 | 0.7411 | 0.9104 | -0.6465 | 0.7485 | rejected |
| FLOW/USDT | P8_144 | 115 | 0.9639 | 0.8102 | 0.9408 | -0.3252 | 0.7998 | rejected |
| FLUX/USDT | P100_144 | 82 | 1.1505 | 0.8009 | 1.1505 | 0.7069 | 0.8005 | exploratory signal |
| FLUX/USDT | P12_200 | 79 | 1.0836 | 0.9246 | 1.0006 | 0.0584 | 0.8372 | exploratory signal |
| FLUX/USDT | P12_34 | 217 | 0.9176 | 0.6432 | 0.9258 | -0.4821 | 0.6369 | rejected |
| FLUX/USDT | P12_55 | 222 | 0.9856 | 0.7417 | 0.9940 | 0.0359 | 0.7329 | rejected |
| FLUX/USDT | P34_200 | 101 | 0.9398 | 0.7623 | 0.9398 | -0.2646 | 0.7560 | rejected |
| FLUX/USDT | P50_200 | 103 | 0.9877 | 0.7940 | 0.9877 | -0.0113 | 0.7908 | rejected |
| FLUX/USDT | P55_144 | 123 | 0.9689 | 0.7363 | 0.9689 | -0.1303 | 0.7411 | rejected |
| FLUX/USDT | P55_200 | 95 | 1.1052 | 0.8973 | 1.0789 | 0.4399 | 0.8726 | exploratory signal |
| FLUX/USDT | P89_144 | 100 | 0.9556 | 0.6867 | 0.9556 | -0.1890 | 0.6902 | rejected |
| FLUX/USDT | P8_144 | 140 | 0.9806 | 0.8083 | 0.9144 | -0.4792 | 0.7445 | rejected |
| FLUX/USDT | P8_200 | 93 | 1.5170 | 1.2910 | 1.2427 | 1.2438 | 1.0272 | credible candidate |
| GALA/USDT | P12_200 | 74 | 1.0583 | 0.9301 | 1.0583 | 0.3084 | 0.9313 | exploratory signal |
| GALA/USDT | P20_200 | 76 | 1.0355 | 0.9018 | 1.0192 | 0.1409 | 0.8870 | exploratory signal |
| GALA/USDT | P21_200 | 84 | 1.0533 | 0.9035 | 1.0573 | 0.3381 | 0.9088 | exploratory signal |
| GALA/USDT | P26_144 | 113 | 1.0553 | 0.8745 | 1.0553 | 0.3615 | 0.8766 | exploratory signal |
| GALA/USDT | P26_200 | 91 | 1.1471 | 0.9721 | 1.1440 | 0.7554 | 0.9691 | exploratory signal |
| GALA/USDT | P8_144 | 80 | 1.0899 | 0.9604 | 1.0899 | 0.4601 | 0.9613 | exploratory signal |
| GMT/USDT | P12_144 | 103 | 0.9932 | 0.8181 | 0.9265 | -0.3528 | 0.7568 | rejected |
| GMT/USDT | P12_20 | 103 | 1.0775 | 0.7253 | 1.0775 | 0.4592 | 0.7365 | exploratory signal |
| GMT/USDT | P12_200 | 83 | 1.1827 | 1.0090 | 1.1693 | 0.8336 | 0.9985 | exploratory signal |
| GMT/USDT | P12_21 | 113 | 1.0432 | 0.7111 | 1.0432 | 0.2982 | 0.7218 | exploratory signal |
| GMT/USDT | P20_200 | 103 | 1.0420 | 0.8679 | 1.0420 | 0.2803 | 0.8715 | exploratory signal |
| GMT/USDT | P21_200 | 103 | 1.0424 | 0.8683 | 1.0424 | 0.2841 | 0.8735 | exploratory signal |
| GMT/USDT | P26_200 | 102 | 1.0534 | 0.8629 | 1.0534 | 0.3430 | 0.8719 | exploratory signal |
| GMT/USDT | P34_200 | 102 | 1.0048 | 0.8186 | 1.0004 | 0.0561 | 0.8211 | exploratory signal |
| GMT/USDT | P8_12 | 81 | 1.0031 | 0.6799 | 1.0031 | 0.0626 | 0.6926 | exploratory signal |
| GMT/USDT | P8_144 | 110 | 1.2242 | 1.0183 | 1.1404 | 0.7598 | 0.9364 | exploratory signal |
| GMT/USDT | P8_20 | 173 | 0.9164 | 0.6305 | 0.9039 | -0.6492 | 0.6304 | rejected |
| GMT/USDT | P8_200 | 88 | 1.4737 | 1.2727 | 1.4743 | 1.9895 | 1.2697 | exploratory signal |
| GMT/USDT | P8_21 | 181 | 0.9277 | 0.6410 | 0.9154 | -0.5605 | 0.6373 | rejected |
| GRT/USDT | P20_200 | 57 | 1.4433 | 1.2623 | 1.3953 | 1.4236 | 1.2070 | exploratory signal |
| GRT/USDT | P26_200 | 85 | 0.9493 | 0.7885 | 0.9650 | -0.1263 | 0.7997 | rejected |
| GRT/USDT | P34_200 | 105 | 0.9841 | 0.8033 | 0.9841 | -0.0330 | 0.8040 | rejected |
| GRT/USDT | P50_200 | 92 | 1.1164 | 0.9006 | 1.1164 | 0.6211 | 0.9059 | exploratory signal |
| GRT/USDT | P8_200 | 57 | 1.3602 | 1.2002 | 1.2529 | 0.9465 | 1.0880 | exploratory signal |
| G/USDT | P8_144 | 88 | 0.9124 | 0.7573 | 0.9496 | -0.2085 | 0.7724 | rejected |
| G/USDT | P8_200 | 75 | 1.1125 | 0.9476 | 1.0971 | 0.4790 | 0.9166 | exploratory signal |
| HBAR/USDT | P20_200 | 116 | 0.9934 | 0.7826 | 0.9934 | 0.0207 | 0.7776 | rejected |
| HBAR/USDT | P21_200 | 110 | 0.9295 | 0.7276 | 0.9295 | -0.3410 | 0.7246 | rejected |
| HBAR/USDT | P50_200 | 90 | 0.9165 | 0.6694 | 0.9165 | -0.3809 | 0.6689 | rejected |
| HNT/USDT | P100_144 | 75 | 0.9662 | 0.6972 | 0.9662 | -0.1109 | 0.6968 | rejected |
| HNT/USDT | P12_144 | 114 | 1.0480 | 0.8751 | 1.0480 | 0.3223 | 0.8745 | exploratory signal |
| HNT/USDT | P12_200 | 82 | 1.0640 | 0.8966 | 1.0640 | 0.3576 | 0.9012 | exploratory signal |
| HNT/USDT | P20_100 | 160 | 0.9647 | 0.7723 | 0.9647 | -0.1759 | 0.7734 | rejected |
| HNT/USDT | P20_144 | 114 | 1.1362 | 0.9237 | 1.1362 | 0.7783 | 0.9235 | exploratory signal |
| HNT/USDT | P20_200 | 42 | 1.0326 | 0.8913 | 1.0326 | 0.1482 | 0.8924 | exploratory signal |
| HNT/USDT | P20_89 | 180 | 0.9547 | 0.7503 | 0.9547 | -0.2646 | 0.7540 | rejected |
| HNT/USDT | P21_100 | 158 | 0.9408 | 0.7515 | 0.9408 | -0.3422 | 0.7518 | rejected |
| HNT/USDT | P21_144 | 93 | 1.0530 | 0.8537 | 1.0530 | 0.3127 | 0.8515 | exploratory signal |
| HNT/USDT | P21_200 | 41 | 0.9864 | 0.8494 | 0.9864 | -0.0133 | 0.8500 | rejected |
| HNT/USDT | P21_89 | 178 | 0.9357 | 0.7355 | 0.9357 | -0.4046 | 0.7375 | rejected |
| HNT/USDT | P26_144 | 106 | 0.9292 | 0.7579 | 0.9292 | -0.3401 | 0.7544 | rejected |
| HNT/USDT | P26_200 | 61 | 1.0599 | 0.9035 | 1.0599 | 0.2837 | 0.9011 | exploratory signal |
| HNT/USDT | P26_89 | 169 | 0.9055 | 0.7053 | 0.9055 | -0.6242 | 0.7075 | rejected |
| HNT/USDT | P34_100 | 145 | 0.9516 | 0.7441 | 0.9516 | -0.2516 | 0.7432 | rejected |
| HNT/USDT | P34_144 | 110 | 1.2353 | 0.9969 | 1.2353 | 1.2283 | 0.9989 | exploratory signal |
| HNT/USDT | P34_200 | 81 | 1.1427 | 0.9573 | 1.1427 | 0.7008 | 0.9603 | exploratory signal |
| HNT/USDT | P34_55 | 115 | 0.9715 | 0.6644 | 0.9715 | -0.1057 | 0.6651 | rejected |
| HNT/USDT | P34_89 | 162 | 0.9477 | 0.7196 | 0.9477 | -0.2989 | 0.7227 | rejected |
| HNT/USDT | P50_144 | 122 | 1.0046 | 0.7856 | 1.0046 | 0.0857 | 0.7870 | exploratory signal |
| HNT/USDT | P50_200 | 104 | 0.9764 | 0.8031 | 0.9764 | -0.0824 | 0.8112 | rejected |
| HNT/USDT | P55_144 | 124 | 1.0646 | 0.8298 | 1.0646 | 0.4202 | 0.8245 | exploratory signal |
| HNT/USDT | P55_200 | 111 | 0.9868 | 0.8142 | 0.9868 | -0.0205 | 0.8190 | rejected |
| HNT/USDT | P89_144 | 88 | 1.1786 | 0.8770 | 1.1786 | 0.8592 | 0.8780 | exploratory signal |
| HNT/USDT | P8_144 | 123 | 1.0117 | 0.8448 | 1.0117 | 0.1289 | 0.8461 | exploratory signal |
| HNT/USDT | P8_200 | 63 | 0.9672 | 0.8041 | 0.9672 | -0.1021 | 0.8067 | rejected |
| ICP/USDT | P100_144 | 62 | 1.0791 | 0.7755 | 1.0791 | 0.3568 | 0.7815 | exploratory signal |
| ICP/USDT | P20_144 | 110 | 0.9169 | 0.7422 | 0.9514 | -0.2173 | 0.7682 | rejected |
| ICP/USDT | P89_144 | 82 | 1.0350 | 0.7528 | 1.0580 | 0.3247 | 0.7819 | exploratory signal |
| ICP/USDT | P8_12 | 58 | 0.9076 | 0.5962 | 0.9076 | -0.3338 | 0.5934 | rejected |
| ID/USDT | P12_144 | 120 | 0.9984 | 0.8055 | 0.9900 | -0.0027 | 0.7967 | rejected |
| ID/USDT | P26_200 | 101 | 0.9151 | 0.7683 | 0.9099 | -0.4631 | 0.7647 | rejected |
| ID/USDT | P50_200 | 98 | 1.0309 | 0.8415 | 1.0321 | 0.2255 | 0.8401 | exploratory signal |
| ID/USDT | P55_200 | 95 | 0.9671 | 0.7822 | 0.9704 | -0.1098 | 0.7834 | rejected |
| ID/USDT | P8_144 | 124 | 0.9041 | 0.7570 | 0.9015 | -0.5784 | 0.7357 | rejected |
| ILV/USDT | P100_200 | 104 | 0.9605 | 0.6942 | 0.9605 | -0.1609 | 0.6945 | rejected |
| ILV/USDT | P12_200 | 103 | 0.9057 | 0.7264 | 0.9057 | -0.4871 | 0.7310 | rejected |
| ILV/USDT | P144_200 | 82 | 0.9345 | 0.6295 | 0.9345 | -0.2613 | 0.6221 | rejected |
| ILV/USDT | P21_200 | 146 | 0.9376 | 0.7393 | 0.9376 | -0.3593 | 0.7456 | rejected |
| ILV/USDT | P26_200 | 127 | 1.0133 | 0.7945 | 1.0133 | 0.1376 | 0.7960 | exploratory signal |
| ILV/USDT | P34_144 | 159 | 0.9404 | 0.7034 | 0.9404 | -0.3494 | 0.7085 | rejected |
| ILV/USDT | P34_200 | 120 | 1.1186 | 0.8754 | 1.1186 | 0.6996 | 0.8761 | exploratory signal |
| ILV/USDT | P50_200 | 115 | 0.9059 | 0.6969 | 0.9059 | -0.5003 | 0.6961 | rejected |
| ILV/USDT | P55_200 | 110 | 1.0022 | 0.7722 | 1.0022 | 0.0682 | 0.7722 | exploratory signal |
| ILV/USDT | P8_200 | 108 | 1.0056 | 0.8247 | 1.0056 | 0.0855 | 0.8247 | exploratory signal |
| IMX/USDT | P12_100 | 183 | 1.0658 | 0.8541 | 1.0658 | 0.5009 | 0.8447 | exploratory signal |
| IMX/USDT | P12_144 | 133 | 0.9464 | 0.7771 | 0.9464 | -0.2674 | 0.7742 | rejected |
| IMX/USDT | P12_200 | 94 | 1.3886 | 1.1734 | 1.4025 | 1.8017 | 1.1843 | exploratory signal |
| IMX/USDT | P12_89 | 194 | 0.9054 | 0.7224 | 0.9054 | -0.6452 | 0.7201 | rejected |
| IMX/USDT | P20_100 | 179 | 0.9697 | 0.7725 | 0.9697 | -0.1443 | 0.7721 | rejected |
| IMX/USDT | P20_144 | 143 | 1.0420 | 0.8488 | 1.0436 | 0.3383 | 0.8488 | exploratory signal |
| IMX/USDT | P20_200 | 122 | 1.3057 | 1.0826 | 1.3382 | 1.7558 | 1.1116 | exploratory signal |
| IMX/USDT | P20_89 | 183 | 0.9198 | 0.7311 | 0.9198 | -0.5292 | 0.7322 | rejected |
| IMX/USDT | P21_144 | 143 | 0.9568 | 0.7805 | 0.9622 | -0.1802 | 0.7819 | rejected |
| IMX/USDT | P21_200 | 111 | 1.2394 | 1.0252 | 1.2771 | 1.4252 | 1.0591 | exploratory signal |
| IMX/USDT | P26_100 | 181 | 0.9714 | 0.7569 | 0.9714 | -0.1257 | 0.7498 | rejected |
| IMX/USDT | P26_144 | 134 | 1.1163 | 0.9104 | 1.1163 | 0.7168 | 0.9068 | exploratory signal |
| IMX/USDT | P26_200 | 114 | 1.4801 | 1.2167 | 1.4801 | 2.2564 | 1.2246 | exploratory signal |
| IMX/USDT | P34_100 | 175 | 0.9267 | 0.6982 | 0.9267 | -0.4454 | 0.6950 | rejected |
| IMX/USDT | P34_144 | 134 | 1.0718 | 0.8669 | 1.0718 | 0.4869 | 0.8687 | exploratory signal |
| IMX/USDT | P34_200 | 101 | 1.3729 | 1.1217 | 1.3871 | 1.8507 | 1.1430 | exploratory signal |
| IMX/USDT | P34_50 | 109 | 1.0669 | 0.6937 | 1.0669 | 0.4104 | 0.7057 | exploratory signal |
| IMX/USDT | P34_55 | 125 | 0.9689 | 0.6598 | 0.9689 | -0.1272 | 0.6663 | rejected |
| IMX/USDT | P50_144 | 130 | 1.1208 | 0.8701 | 1.1208 | 0.7655 | 0.8790 | exploratory signal |
| IMX/USDT | P50_200 | 102 | 1.2397 | 1.0012 | 1.2397 | 1.2209 | 1.0091 | exploratory signal |
| IMX/USDT | P50_55 | 44 | 1.4581 | 0.9954 | 1.4581 | 1.3460 | 1.0113 | exploratory signal |
| IMX/USDT | P55_100 | 147 | 0.9437 | 0.6794 | 0.9437 | -0.3135 | 0.6869 | rejected |
| IMX/USDT | P55_144 | 130 | 1.1112 | 0.8505 | 1.1112 | 0.6959 | 0.8548 | exploratory signal |
| IMX/USDT | P55_200 | 101 | 1.1258 | 0.9078 | 1.1258 | 0.6932 | 0.9132 | exploratory signal |
| IMX/USDT | P8_100 | 185 | 0.9986 | 0.8060 | 0.9592 | -0.2327 | 0.7768 | rejected |
| IMX/USDT | P8_144 | 149 | 1.0150 | 0.8318 | 1.0053 | 0.1005 | 0.8204 | exploratory signal |
| IMX/USDT | P8_200 | 93 | 1.3049 | 1.1024 | 1.2911 | 1.3772 | 1.0899 | credible candidate |
| INJ/USDT | P8_12 | 58 | 0.9568 | 0.6267 | 0.9568 | -0.1356 | 0.6301 | rejected |
| IOST/USDT | P12_200 | 109 | 0.9268 | 0.7312 | 0.9268 | -0.3640 | 0.7310 | rejected |
| IOST/USDT | P20_200 | 126 | 0.9495 | 0.7273 | 0.9495 | -0.2369 | 0.7190 | rejected |
| IOST/USDT | P21_200 | 128 | 0.9503 | 0.7318 | 0.9503 | -0.2334 | 0.7226 | rejected |
| IOST/USDT | P26_144 | 136 | 0.9231 | 0.6789 | 0.9231 | -0.4233 | 0.6752 | rejected |
| IOST/USDT | P26_200 | 131 | 0.9458 | 0.7168 | 0.9458 | -0.2623 | 0.7076 | rejected |
| IOST/USDT | P34_200 | 127 | 0.9136 | 0.6839 | 0.9136 | -0.4603 | 0.6771 | rejected |
| IOST/USDT | P8_200 | 129 | 0.9068 | 0.6941 | 0.9068 | -0.5178 | 0.6915 | rejected |
| IOTA/USDT | P12_144 | 124 | 0.9579 | 0.7787 | 0.9676 | -0.1456 | 0.7936 | rejected |
| IOTA/USDT | P21_200 | 103 | 0.9006 | 0.7297 | 0.9006 | -0.5083 | 0.7298 | rejected |
| IOTA/USDT | P26_200 | 109 | 0.9168 | 0.7329 | 0.9168 | -0.4247 | 0.7333 | rejected |
| IOTX/USDT | P21_200 | 129 | 0.9440 | 0.7418 | 0.9165 | -0.4589 | 0.7132 | rejected |
| IOTX/USDT | P34_200 | 116 | 0.9409 | 0.7342 | 0.9579 | -0.1808 | 0.7445 | rejected |
| IOTX/USDT | P55_200 | 124 | 1.0327 | 0.8111 | 0.9823 | -0.0459 | 0.7690 | rejected |
| IOTX/USDT | P8_144 | 87 | 0.9043 | 0.7100 | 0.8954 | -0.5618 | 0.6969 | rejected |
| JASMY/USDT | P100_144 | 80 | 1.0033 | 0.6887 | 1.0033 | 0.0626 | 0.6952 | exploratory signal |
| JASMY/USDT | P100_200 | 98 | 1.1344 | 0.8462 | 1.1230 | 0.6529 | 0.8331 | exploratory signal |
| JASMY/USDT | P12_100 | 186 | 0.9261 | 0.7242 | 0.9261 | -0.4665 | 0.7193 | rejected |
| JASMY/USDT | P12_144 | 156 | 0.9724 | 0.7720 | 0.9668 | -0.1614 | 0.7708 | rejected |
| JASMY/USDT | P144_200 | 56 | 1.4928 | 1.0550 | 1.4928 | 1.5876 | 1.0619 | exploratory signal |
| JASMY/USDT | P20_100 | 165 | 1.0677 | 0.8169 | 1.0677 | 0.4907 | 0.8066 | exploratory signal |
| JASMY/USDT | P20_144 | 144 | 1.2376 | 0.9714 | 1.2048 | 1.2165 | 0.9398 | exploratory signal |
| JASMY/USDT | P20_200 | 135 | 1.1237 | 0.8935 | 1.1057 | 0.6744 | 0.8723 | exploratory signal |
| JASMY/USDT | P21_100 | 167 | 1.0660 | 0.8183 | 1.0660 | 0.4865 | 0.8101 | exploratory signal |
| JASMY/USDT | P21_144 | 146 | 1.2316 | 0.9681 | 1.1995 | 1.1954 | 0.9367 | exploratory signal |
| JASMY/USDT | P21_200 | 135 | 1.1228 | 0.8918 | 1.1048 | 0.6683 | 0.8702 | exploratory signal |
| JASMY/USDT | P26_100 | 161 | 0.9362 | 0.7070 | 0.9362 | -0.3628 | 0.7032 | rejected |
| JASMY/USDT | P26_144 | 148 | 1.1415 | 0.8829 | 1.1415 | 0.8891 | 0.8789 | exploratory signal |
| JASMY/USDT | P26_200 | 130 | 1.0813 | 0.8562 | 1.0194 | 0.1755 | 0.7985 | exploratory signal |
| JASMY/USDT | P34_144 | 148 | 1.2295 | 0.9399 | 1.2295 | 1.3374 | 0.9321 | exploratory signal |
| JASMY/USDT | P34_200 | 120 | 0.9656 | 0.7636 | 0.9934 | 0.0213 | 0.7804 | rejected |
| JASMY/USDT | P50_144 | 128 | 1.2551 | 0.9350 | 1.2551 | 1.3655 | 0.9305 | exploratory signal |
| JASMY/USDT | P50_200 | 103 | 1.1875 | 0.9344 | 1.1698 | 0.9010 | 0.9190 | exploratory signal |
| JASMY/USDT | P55_144 | 132 | 1.1905 | 0.8861 | 1.1905 | 1.0953 | 0.8852 | exploratory signal |
| JASMY/USDT | P55_200 | 114 | 1.1133 | 0.8703 | 1.1212 | 0.7074 | 0.8752 | exploratory signal |
| JASMY/USDT | P89_100 | 33 | 0.9027 | 0.5768 | 0.9027 | -0.2764 | 0.5795 | rejected |
| JASMY/USDT | P89_144 | 94 | 0.9227 | 0.6451 | 0.9227 | -0.3688 | 0.6540 | rejected |
| JASMY/USDT | P89_200 | 101 | 1.0624 | 0.8012 | 1.0535 | 0.3352 | 0.7961 | exploratory signal |
| JASMY/USDT | P8_200 | 149 | 0.9616 | 0.7727 | 0.9917 | 0.0117 | 0.7971 | rejected |
| JST/USDT | P20_200 | 110 | 0.9292 | 0.7247 | 0.9108 | -0.4249 | 0.6987 | rejected |
| JST/USDT | P21_200 | 110 | 0.9210 | 0.7136 | 0.9031 | -0.4742 | 0.6890 | rejected |
| JST/USDT | P26_200 | 110 | 0.9048 | 0.6879 | 0.8880 | -0.5880 | 0.6720 | rejected |
| JTO/USDT | P12_200 | 113 | 1.0239 | 0.8870 | 1.0320 | 0.2399 | 0.8938 | exploratory signal |
| JTO/USDT | P26_200 | 128 | 0.9018 | 0.7733 | 0.9018 | -0.5772 | 0.7767 | rejected |
| JTO/USDT | P34_200 | 116 | 0.9364 | 0.8104 | 0.9706 | -0.1266 | 0.8423 | rejected |
| JTO/USDT | P8_200 | 117 | 0.9241 | 0.8056 | 0.9501 | -0.2459 | 0.8278 | rejected |
| JUP/USDT | P144_200 | 74 | 0.9661 | 0.7091 | 0.9661 | -0.1016 | 0.6959 | rejected |
| JUP/USDT | P55_100 | 104 | 0.9089 | 0.6873 | 0.9089 | -0.4323 | 0.6795 | rejected |
| JUP/USDT | P8_12 | 70 | 0.9436 | 0.6596 | 0.9436 | -0.2109 | 0.6611 | rejected |
| KAS/USDT | P12_50 | 198 | 0.9277 | 0.6732 | 0.9277 | -0.4700 | 0.6720 | rejected |
| KAS/USDT | P12_55 | 199 | 0.9232 | 0.6775 | 0.9232 | -0.4842 | 0.6672 | rejected |
| KMNO/USDT | P55_89 | 112 | 0.9193 | 0.6326 | 0.9193 | -0.4404 | 0.6472 | rejected |
| KNC/USDT | P20_200 | 96 | 1.0278 | 0.7821 | 1.0027 | 0.0663 | 0.7630 | exploratory signal |
| KNC/USDT | P26_200 | 114 | 0.9424 | 0.6887 | 0.9424 | -0.2673 | 0.6837 | rejected |
| LDO/USDT | P21_26 | 64 | 0.9159 | 0.6000 | 0.9159 | -0.3202 | 0.5989 | rejected |
| LDO/USDT | P26_34 | 62 | 1.0133 | 0.6857 | 1.0133 | 0.0952 | 0.6822 | exploratory signal |
| LINK/USDT | P100_200 | 86 | 0.9309 | 0.6183 | 0.9309 | -0.2772 | 0.6048 | rejected |
| LINK/USDT | P12_200 | 107 | 0.9288 | 0.7169 | 0.9288 | -0.3417 | 0.7136 | rejected |
| LINK/USDT | P20_200 | 108 | 0.9009 | 0.6860 | 0.9009 | -0.5027 | 0.6818 | rejected |
| LINK/USDT | P55_200 | 101 | 0.9543 | 0.6764 | 0.9543 | -0.1777 | 0.6641 | rejected |
| LINK/USDT | P8_200 | 114 | 0.9002 | 0.6978 | 0.9002 | -0.5160 | 0.6916 | rejected |
| LQTY/USDT | P12_200 | 96 | 1.0126 | 0.7645 | 0.9094 | -0.4684 | 0.6953 | rejected |
| LQTY/USDT | P20_200 | 120 | 0.9259 | 0.6968 | 0.7817 | -1.3577 | 0.5919 | rejected |
| LQTY/USDT | P21_200 | 118 | 0.9627 | 0.7263 | 0.8257 | -1.0369 | 0.6279 | rejected |
| LQTY/USDT | P26_200 | 118 | 0.9732 | 0.7425 | 0.8343 | -0.9755 | 0.6393 | rejected |
| LQTY/USDT | P34_200 | 119 | 0.9789 | 0.7666 | 0.9789 | -0.0662 | 0.7702 | rejected |
| LQTY/USDT | P8_200 | 75 | 1.0732 | 0.8609 | 0.8736 | -0.6091 | 0.7006 | rejected |
| LTC/USDT | P12_200 | 43 | 1.1151 | 0.8627 | 0.9687 | -0.0928 | 0.7464 | rejected |
| LTC/USDT | P50_55 | 33 | 1.0143 | 0.5546 | 1.0143 | 0.0719 | 0.5573 | exploratory signal |
| MANA/USDT | P20_21 | 49 | 0.9422 | 0.5875 | 0.9422 | -0.1833 | 0.5965 | rejected |
| MANA/USDT | P20_26 | 69 | 1.1093 | 0.6678 | 1.1093 | 0.4886 | 0.6759 | exploratory signal |
| MANA/USDT | P20_34 | 117 | 0.9017 | 0.5673 | 0.9017 | -0.5416 | 0.5768 | rejected |
| MANA/USDT | P21_26 | 63 | 1.1085 | 0.6784 | 1.1085 | 0.4699 | 0.6897 | exploratory signal |
| MANA/USDT | P8_144 | 63 | 0.9557 | 0.7494 | 0.9613 | -0.1311 | 0.7571 | rejected |
| MEME/USDT | P100_144 | 117 | 0.9674 | 0.6459 | 0.9674 | -0.1339 | 0.6519 | rejected |
| MEME/USDT | P100_200 | 120 | 0.9324 | 0.6860 | 0.9468 | -0.2717 | 0.7068 | rejected |
| MEME/USDT | P34_200 | 114 | 0.9219 | 0.7260 | 0.9219 | -0.4173 | 0.7329 | rejected |
| MEME/USDT | P89_144 | 120 | 0.9835 | 0.6716 | 0.9982 | 0.0477 | 0.6871 | rejected |
| MEME/USDT | P89_200 | 120 | 0.9552 | 0.7043 | 0.9706 | -0.1160 | 0.7204 | rejected |
| MERL/USDT | P8_144 | 142 | 0.9387 | 0.8059 | 0.9387 | -0.3490 | 0.8101 | rejected |
| MERL/USDT | P8_50 | 264 | 0.9394 | 0.7715 | 0.9394 | -0.4868 | 0.7821 | rejected |
| MERL/USDT | P8_89 | 235 | 0.9028 | 0.7532 | 0.9028 | -0.7869 | 0.7606 | rejected |
| MEW/USDT | P8_200 | 49 | 1.1845 | 1.0103 | 0.9391 | -0.2020 | 0.7965 | rejected |
| MINA/USDT | P12_200 | 75 | 1.2162 | 1.0532 | 1.3342 | 1.2988 | 1.1513 | exploratory signal |
| MINA/USDT | P20_100 | 145 | 1.1707 | 0.9193 | 1.1707 | 0.9950 | 0.9022 | exploratory signal |
| MINA/USDT | P20_144 | 119 | 0.9992 | 0.7867 | 1.0180 | 0.1573 | 0.7957 | exploratory signal |
| MINA/USDT | P20_200 | 100 | 1.1087 | 0.9031 | 1.1504 | 0.7663 | 0.9304 | exploratory signal |
| MINA/USDT | P20_89 | 157 | 1.0878 | 0.8409 | 1.0878 | 0.5750 | 0.8195 | exploratory signal |
| MINA/USDT | P21_100 | 152 | 1.1539 | 0.8979 | 1.1539 | 0.9330 | 0.8814 | exploratory signal |
| MINA/USDT | P21_144 | 124 | 1.0044 | 0.7898 | 1.0292 | 0.2279 | 0.8039 | exploratory signal |
| MINA/USDT | P21_200 | 92 | 1.1527 | 0.9497 | 1.1987 | 0.9311 | 0.9787 | exploratory signal |
| MINA/USDT | P21_89 | 164 | 1.1029 | 0.8435 | 1.1029 | 0.6797 | 0.8248 | exploratory signal |
| MINA/USDT | P26_100 | 150 | 1.1210 | 0.8607 | 1.1210 | 0.7629 | 0.8481 | exploratory signal |
| MINA/USDT | P26_144 | 123 | 1.0906 | 0.8487 | 1.0906 | 0.5574 | 0.8445 | exploratory signal |
| MINA/USDT | P26_200 | 88 | 1.1223 | 0.9307 | 1.1321 | 0.6396 | 0.9336 | exploratory signal |
| MINA/USDT | P26_89 | 163 | 1.0537 | 0.7943 | 1.0537 | 0.4020 | 0.7818 | exploratory signal |
| MINA/USDT | P34_100 | 147 | 1.1810 | 0.8871 | 1.1810 | 1.0972 | 0.8809 | exploratory signal |
| MINA/USDT | P34_144 | 121 | 0.9867 | 0.7704 | 0.9969 | 0.0416 | 0.7748 | rejected |
| MINA/USDT | P34_200 | 87 | 0.9595 | 0.8031 | 1.0114 | 0.1045 | 0.8446 | exploratory signal |
| MINA/USDT | P34_89 | 165 | 1.1827 | 0.8581 | 1.1827 | 1.1469 | 0.8460 | exploratory signal |
| MINA/USDT | P8_200 | 84 | 1.0690 | 0.9159 | 1.1571 | 0.7252 | 0.9854 | exploratory signal |
| MINA/USDT | P8_89 | 172 | 1.0104 | 0.7963 | 1.0104 | 0.1375 | 0.7857 | exploratory signal |
| MNT/USDT | P100_200 | 77 | 0.9271 | 0.6048 | 0.8986 | -0.4414 | 0.5882 | rejected |
| MNT/USDT | P12_144 | 99 | 0.9121 | 0.7170 | 0.9121 | -0.4470 | 0.7228 | rejected |
| MNT/USDT | P144_200 | 66 | 1.2394 | 0.6727 | 1.2394 | 0.8918 | 0.6737 | exploratory signal |
| MNT/USDT | P20_100 | 123 | 1.2136 | 0.8347 | 1.2136 | 1.1471 | 0.8332 | exploratory signal |
| MNT/USDT | P20_144 | 93 | 1.0883 | 0.8225 | 1.0883 | 0.4844 | 0.8296 | exploratory signal |
| MNT/USDT | P20_200 | 76 | 0.9732 | 0.7836 | 0.9732 | -0.0791 | 0.7841 | rejected |
| MNT/USDT | P20_89 | 134 | 0.9990 | 0.6918 | 0.9990 | 0.0558 | 0.6987 | rejected |
| MNT/USDT | P21_100 | 128 | 1.0816 | 0.7408 | 1.0816 | 0.5190 | 0.7418 | exploratory signal |
| MNT/USDT | P21_144 | 95 | 1.1175 | 0.8382 | 1.1175 | 0.6269 | 0.8454 | exploratory signal |
| MNT/USDT | P21_200 | 79 | 1.0756 | 0.8429 | 1.0756 | 0.3835 | 0.8420 | exploratory signal |
| MNT/USDT | P21_89 | 139 | 0.9131 | 0.6298 | 0.9131 | -0.5101 | 0.6365 | rejected |
| MNT/USDT | P26_144 | 91 | 1.1369 | 0.8902 | 1.1369 | 0.6990 | 0.8922 | exploratory signal |
| MNT/USDT | P26_200 | 77 | 1.1569 | 0.9298 | 1.1569 | 0.7251 | 0.9338 | exploratory signal |
| MNT/USDT | P34_144 | 106 | 0.9904 | 0.7566 | 0.9904 | 0.0038 | 0.7512 | rejected |
| MNT/USDT | P34_200 | 81 | 0.9959 | 0.7848 | 0.9959 | 0.0285 | 0.7869 | rejected |
| MNT/USDT | P55_200 | 75 | 1.1266 | 0.8744 | 1.1266 | 0.5795 | 0.8718 | exploratory signal |
| MNT/USDT | P8_144 | 97 | 1.0306 | 0.8468 | 1.0306 | 0.2176 | 0.8536 | exploratory signal |
| MNT/USDT | P8_200 | 84 | 0.9911 | 0.8054 | 0.9842 | -0.0301 | 0.8009 | rejected |
| MOCA/USDT | P50_200 | 76 | 1.0452 | 0.7895 | 1.0452 | 0.2534 | 0.7815 | exploratory signal |
| MOCA/USDT | P55_200 | 75 | 1.0657 | 0.7933 | 1.0657 | 0.3398 | 0.7845 | exploratory signal |
| MOG/USDT | P8_200 | 52 | 0.9847 | 0.8003 | 1.0177 | 0.1111 | 0.8309 | exploratory signal |
| MOODENG/USDT | P100_144 | 82 | 1.0081 | 0.6783 | 1.0081 | 0.0988 | 0.7013 | exploratory signal |
| MOODENG/USDT | P100_200 | 94 | 0.9968 | 0.7318 | 0.9968 | 0.0376 | 0.7496 | rejected |
| MOODENG/USDT | P12_144 | 119 | 0.9360 | 0.7672 | 0.9360 | -0.3722 | 0.7737 | rejected |
| MOODENG/USDT | P89_144 | 102 | 0.9484 | 0.6665 | 0.9484 | -0.2758 | 0.6859 | rejected |
| MOODENG/USDT | P8_200 | 99 | 0.9434 | 0.7941 | 0.9434 | -0.2846 | 0.7965 | rejected |
| MOVR/USDT | P12_200 | 110 | 0.9504 | 0.8072 | 0.9621 | -0.1559 | 0.8100 | rejected |
| NEAR/USDT | P100_144 | 76 | 1.2790 | 0.9474 | 1.2790 | 1.1363 | 0.9421 | exploratory signal |
| NEAR/USDT | P12_200 | 71 | 0.9091 | 0.8125 | 0.8808 | -0.5497 | 0.7841 | rejected |
| NEAR/USDT | P20_21 | 39 | 0.9276 | 0.6583 | 0.9276 | -0.2083 | 0.6543 | rejected |
| NEAR/USDT | P20_26 | 48 | 0.9527 | 0.7015 | 0.9527 | -0.1379 | 0.7001 | rejected |
| NEAR/USDT | P20_34 | 84 | 0.9518 | 0.6766 | 0.9518 | -0.1882 | 0.6757 | rejected |
| NEAR/USDT | P21_34 | 77 | 0.9678 | 0.6957 | 0.9678 | -0.1018 | 0.6925 | rejected |
| NEAR/USDT | P26_200 | 86 | 1.0738 | 0.9069 | 1.1128 | 0.5961 | 0.9457 | exploratory signal |
| NEAR/USDT | P26_34 | 48 | 1.0398 | 0.7675 | 1.0398 | 0.1769 | 0.7657 | exploratory signal |
| NEAR/USDT | P34_200 | 93 | 1.0441 | 0.8942 | 1.0441 | 0.2732 | 0.8946 | exploratory signal |
| NEAR/USDT | P50_144 | 113 | 0.9876 | 0.7762 | 0.9876 | -0.0124 | 0.7747 | rejected |
| NEAR/USDT | P50_200 | 109 | 1.0278 | 0.8274 | 1.0278 | 0.2076 | 0.8285 | exploratory signal |
| NEAR/USDT | P55_200 | 109 | 0.9231 | 0.7459 | 0.9231 | -0.3923 | 0.7474 | rejected |
| NEAR/USDT | P89_144 | 85 | 1.0923 | 0.8334 | 1.0923 | 0.4663 | 0.8286 | exploratory signal |
| NEAR/USDT | P8_100 | 156 | 0.9149 | 0.7598 | 0.9149 | -0.5255 | 0.7597 | rejected |
| NEO/USDT | P12_144 | 89 | 0.9696 | 0.7520 | 0.9594 | -0.1608 | 0.7352 | rejected |
| NEO/USDT | P12_200 | 72 | 0.9622 | 0.7666 | 0.9911 | 0.0056 | 0.7875 | rejected |
| NEO/USDT | P20_144 | 104 | 1.0440 | 0.7809 | 1.0440 | 0.2771 | 0.7740 | exploratory signal |
| NEO/USDT | P20_200 | 73 | 0.9589 | 0.7455 | 1.0988 | 0.4663 | 0.8482 | exploratory signal |
| NEO/USDT | P21_144 | 104 | 1.1331 | 0.8458 | 1.1331 | 0.6967 | 0.8378 | exploratory signal |
| NEO/USDT | P21_200 | 70 | 0.9923 | 0.7637 | 1.1065 | 0.4904 | 0.8491 | exploratory signal |
| NEO/USDT | P26_144 | 119 | 0.9958 | 0.7268 | 0.9958 | 0.0346 | 0.7138 | rejected |
| NEO/USDT | P26_200 | 96 | 0.9971 | 0.7594 | 1.0463 | 0.2910 | 0.7961 | exploratory signal |
| NEO/USDT | P34_144 | 131 | 0.9961 | 0.7240 | 0.9961 | 0.0379 | 0.7168 | rejected |
| NEO/USDT | P34_200 | 91 | 1.0736 | 0.8124 | 1.0736 | 0.4070 | 0.8130 | exploratory signal |
| NEO/USDT | P8_144 | 90 | 1.2451 | 0.9983 | 1.1382 | 0.6952 | 0.8863 | exploratory signal |
| NEO/USDT | P8_200 | 71 | 1.0720 | 0.8652 | 1.0458 | 0.2496 | 0.8232 | exploratory signal |
| NMR/USDT | P12_200 | 121 | 0.9904 | 0.8078 | 0.9904 | 0.0040 | 0.8024 | rejected |
| NMR/USDT | P20_200 | 114 | 0.9266 | 0.7372 | 0.9266 | -0.3650 | 0.7340 | rejected |
| NMR/USDT | P21_200 | 112 | 0.9922 | 0.7820 | 0.9922 | 0.0132 | 0.7792 | rejected |
| NMR/USDT | P26_200 | 112 | 0.9723 | 0.7507 | 0.9723 | -0.0954 | 0.7446 | rejected |
| NMR/USDT | P50_200 | 112 | 0.9455 | 0.6717 | 0.9455 | -0.2524 | 0.6717 | rejected |
| NMR/USDT | P55_144 | 133 | 0.9905 | 0.6563 | 0.9905 | 0.0046 | 0.6578 | rejected |
| NMR/USDT | P55_200 | 110 | 0.9356 | 0.6533 | 0.9356 | -0.3110 | 0.6555 | rejected |
| NMR/USDT | P8_200 | 116 | 0.9675 | 0.7775 | 0.9675 | -0.1224 | 0.7690 | rejected |
| NOT/USDT | P100_200 | 109 | 0.9154 | 0.6936 | 0.9154 | -0.4518 | 0.7000 | rejected |
| NOT/USDT | P12_100 | 181 | 0.9239 | 0.7399 | 0.9239 | -0.5134 | 0.7447 | rejected |
| NOT/USDT | P12_20 | 77 | 1.0629 | 0.7564 | 1.0629 | 0.3270 | 0.7519 | exploratory signal |
| NOT/USDT | P12_21 | 79 | 1.0094 | 0.7280 | 1.0094 | 0.0916 | 0.7240 | exploratory signal |
| NOT/USDT | P12_89 | 188 | 0.9087 | 0.7277 | 0.9087 | -0.6529 | 0.7330 | rejected |
| NOT/USDT | P20_100 | 166 | 0.9326 | 0.7337 | 0.9326 | -0.4294 | 0.7401 | rejected |
| NOT/USDT | P20_200 | 134 | 0.9091 | 0.7497 | 0.9091 | -0.5460 | 0.7538 | rejected |
| NOT/USDT | P20_21 | 35 | 1.0511 | 0.7216 | 1.0511 | 0.1842 | 0.7171 | exploratory signal |
| NOT/USDT | P20_34 | 95 | 0.9742 | 0.6790 | 0.9742 | -0.0813 | 0.6771 | rejected |
| NOT/USDT | P20_55 | 182 | 0.9124 | 0.6604 | 0.9124 | -0.5925 | 0.6654 | rejected |
| NOT/USDT | P20_89 | 162 | 0.9064 | 0.7068 | 0.9064 | -0.6334 | 0.7148 | rejected |
| NOT/USDT | P21_100 | 163 | 0.9250 | 0.7286 | 0.9250 | -0.4824 | 0.7347 | rejected |
| NOT/USDT | P21_200 | 136 | 0.9312 | 0.7645 | 0.9312 | -0.3931 | 0.7681 | rejected |
| NOT/USDT | P26_200 | 124 | 0.9006 | 0.7275 | 0.9006 | -0.5689 | 0.7294 | rejected |
| NOT/USDT | P26_34 | 56 | 1.1848 | 0.8234 | 1.1848 | 0.6892 | 0.8176 | exploratory signal |
| NOT/USDT | P34_50 | 73 | 0.9714 | 0.6882 | 0.9714 | -0.0854 | 0.6897 | rejected |
| NOT/USDT | P55_100 | 117 | 0.9423 | 0.6799 | 0.9423 | -0.2966 | 0.6893 | rejected |
| NOT/USDT | P89_100 | 32 | 1.1767 | 0.7998 | 1.1767 | 0.4919 | 0.7916 | exploratory signal |
| NOT/USDT | P89_200 | 111 | 0.9239 | 0.7088 | 0.9239 | -0.3938 | 0.7121 | rejected |
| NOT/USDT | P8_100 | 189 | 0.9876 | 0.7996 | 0.9876 | -0.0156 | 0.7965 | rejected |
| NOT/USDT | P8_89 | 201 | 0.9714 | 0.7844 | 0.9601 | -0.2240 | 0.7705 | rejected |
| ONDO/USDT | P20_144 | 130 | 0.9159 | 0.7588 | 0.9159 | -0.4653 | 0.7578 | rejected |
| ONDO/USDT | P8_100 | 173 | 0.9206 | 0.7604 | 0.9206 | -0.4849 | 0.7545 | rejected |
| ONDO/USDT | P8_144 | 149 | 0.9484 | 0.7915 | 0.9484 | -0.2732 | 0.7895 | rejected |
| ONDO/USDT | P8_21 | 169 | 0.9119 | 0.6455 | 0.9119 | -0.5478 | 0.6397 | rejected |
| ONDO/USDT | P8_26 | 204 | 0.9432 | 0.6856 | 0.9432 | -0.3606 | 0.6843 | rejected |
| ONT/USDT | P26_200 | 93 | 0.9143 | 0.7513 | 0.9143 | -0.3929 | 0.7473 | rejected |
| OP/USDT | P34_50 | 89 | 1.0269 | 0.7066 | 1.0269 | 0.1793 | 0.7085 | exploratory signal |
| OP/USDT | P34_55 | 118 | 0.9416 | 0.6468 | 0.9416 | -0.2721 | 0.6402 | rejected |
| PENDLE/USDT | P12_200 | 58 | 1.0112 | 0.9220 | 1.0112 | 0.0844 | 0.9200 | exploratory signal |
| PENDLE/USDT | P20_100 | 153 | 0.9036 | 0.7253 | 0.9036 | -0.6184 | 0.7311 | rejected |
| PENDLE/USDT | P20_144 | 105 | 0.9270 | 0.7766 | 0.9270 | -0.3562 | 0.7761 | rejected |
| PENDLE/USDT | P20_89 | 183 | 0.9327 | 0.7374 | 0.9327 | -0.4409 | 0.7434 | rejected |
| PENDLE/USDT | P26_100 | 140 | 0.9445 | 0.7516 | 0.9445 | -0.3031 | 0.7571 | rejected |
| PENDLE/USDT | P26_144 | 103 | 1.0727 | 0.8852 | 1.0727 | 0.4360 | 0.8884 | exploratory signal |
| PENDLE/USDT | P26_89 | 174 | 0.9168 | 0.7146 | 0.9168 | -0.5500 | 0.7202 | rejected |
| PENDLE/USDT | P34_100 | 138 | 0.9937 | 0.7853 | 0.9937 | 0.0227 | 0.7901 | rejected |
| PENDLE/USDT | P34_144 | 98 | 1.3020 | 1.0650 | 1.3020 | 1.4488 | 1.0713 | exploratory signal |
| PENDLE/USDT | P50_100 | 132 | 0.9481 | 0.7290 | 0.9481 | -0.2661 | 0.7321 | rejected |
| PENDLE/USDT | P50_144 | 122 | 1.0105 | 0.8077 | 1.0105 | 0.1184 | 0.8033 | exploratory signal |
| PENDLE/USDT | P50_200 | 87 | 0.9951 | 0.8328 | 0.9951 | 0.0254 | 0.8304 | rejected |
| PENDLE/USDT | P50_89 | 125 | 0.9265 | 0.6970 | 0.9265 | -0.3850 | 0.6954 | rejected |
| PENDLE/USDT | P55_100 | 123 | 1.0153 | 0.7830 | 1.0153 | 0.1473 | 0.7821 | exploratory signal |
| PENDLE/USDT | P55_144 | 116 | 0.9187 | 0.7348 | 0.9187 | -0.4167 | 0.7312 | rejected |
| PENDLE/USDT | P55_89 | 109 | 1.0264 | 0.7684 | 1.0264 | 0.1957 | 0.7645 | exploratory signal |
| PENDLE/USDT | P8_100 | 128 | 0.9787 | 0.8251 | 0.9787 | -0.0701 | 0.8263 | rejected |
| PENDLE/USDT | P8_144 | 107 | 1.0379 | 0.8844 | 1.0379 | 0.2605 | 0.8856 | exploratory signal |
| PENDLE/USDT | P8_200 | 72 | 0.9374 | 0.8236 | 0.9374 | -0.2456 | 0.8232 | rejected |
| PENDLE/USDT | P8_89 | 144 | 0.9038 | 0.7562 | 0.9038 | -0.5862 | 0.7574 | rejected |
| PEOPLE/USDT | P100_200 | 117 | 0.9390 | 0.6948 | 0.9390 | -0.2882 | 0.6870 | rejected |
| PEOPLE/USDT | P12_200 | 101 | 0.9392 | 0.7903 | 0.9392 | -0.2743 | 0.7871 | rejected |
| PEOPLE/USDT | P20_100 | 155 | 0.9205 | 0.7200 | 0.9205 | -0.4845 | 0.7240 | rejected |
| PEOPLE/USDT | P20_144 | 120 | 1.1659 | 0.9611 | 1.1659 | 0.9412 | 0.9620 | exploratory signal |
| PEOPLE/USDT | P20_200 | 115 | 1.0785 | 0.8862 | 1.0785 | 0.4809 | 0.8846 | exploratory signal |
| PEOPLE/USDT | P21_100 | 157 | 0.9373 | 0.7282 | 0.9373 | -0.3660 | 0.7324 | rejected |
| PEOPLE/USDT | P21_144 | 123 | 1.2126 | 0.9945 | 1.2126 | 1.1660 | 0.9931 | exploratory signal |
| PEOPLE/USDT | P21_200 | 119 | 1.0633 | 0.8697 | 1.0633 | 0.4078 | 0.8679 | exploratory signal |
| PEOPLE/USDT | P26_100 | 158 | 0.9052 | 0.6908 | 0.9052 | -0.5876 | 0.6914 | rejected |
| PEOPLE/USDT | P26_144 | 128 | 0.9056 | 0.7181 | 0.9056 | -0.5234 | 0.7164 | rejected |
| PEOPLE/USDT | P34_144 | 130 | 0.9374 | 0.7429 | 0.9374 | -0.3317 | 0.7458 | rejected |
| PEOPLE/USDT | P50_200 | 119 | 0.9376 | 0.7483 | 0.9376 | -0.3013 | 0.7421 | rejected |
| PEOPLE/USDT | P55_200 | 121 | 0.9252 | 0.7307 | 0.9252 | -0.3765 | 0.7240 | rejected |
| PEOPLE/USDT | P89_200 | 128 | 0.9102 | 0.6823 | 0.9102 | -0.4738 | 0.6718 | rejected |
| PHA/USDT | P21_89 | 173 | 0.9271 | 0.7566 | 0.9271 | -0.4792 | 0.7623 | rejected |
| POL/USDT | P12_144 | 76 | 1.0865 | 0.8876 | 1.1676 | 0.8080 | 0.9561 | exploratory signal |
| POL/USDT | P12_200 | 57 | 0.9935 | 0.8246 | 1.1355 | 0.5977 | 0.9475 | exploratory signal |
| POL/USDT | P20_100 | 126 | 0.9261 | 0.7007 | 0.9261 | -0.3863 | 0.6987 | rejected |
| POL/USDT | P20_144 | 73 | 1.2058 | 0.9964 | 1.2058 | 0.9025 | 1.0009 | exploratory signal |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.1617 | 1.3597 | 1.3904 | 1.1649 | exploratory signal |
| POL/USDT | P21_100 | 122 | 0.9975 | 0.7530 | 0.9975 | 0.0440 | 0.7545 | rejected |
| POL/USDT | P21_144 | 73 | 1.2037 | 0.9916 | 1.2037 | 0.8901 | 0.9951 | exploratory signal |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.2155 | 1.4246 | 1.6027 | 1.2175 | exploratory signal |
| POL/USDT | P21_89 | 138 | 0.9410 | 0.6857 | 0.9410 | -0.3189 | 0.6916 | rejected |
| POL/USDT | P26_100 | 118 | 1.0603 | 0.7840 | 1.0603 | 0.4012 | 0.7941 | exploratory signal |
| POL/USDT | P26_144 | 81 | 1.1914 | 0.9632 | 1.1914 | 0.9124 | 0.9728 | exploratory signal |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.1647 | 1.3900 | 1.5210 | 1.1701 | exploratory signal |
| POL/USDT | P26_89 | 140 | 0.9108 | 0.6351 | 0.9108 | -0.5414 | 0.6480 | rejected |
| POL/USDT | P34_100 | 126 | 1.1289 | 0.8274 | 1.1289 | 0.7705 | 0.8272 | exploratory signal |
| POL/USDT | P34_144 | 119 | 1.1288 | 0.8492 | 1.1288 | 0.7807 | 0.8632 | exploratory signal |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.1151 | 1.3951 | 1.7600 | 1.1220 | exploratory signal |
| POL/USDT | P34_89 | 139 | 0.9768 | 0.6857 | 0.9768 | -0.0892 | 0.6979 | rejected |
| POL/USDT | P50_100 | 110 | 0.9856 | 0.6782 | 0.9856 | -0.0227 | 0.6753 | rejected |
| POL/USDT | P50_144 | 117 | 0.9446 | 0.6971 | 0.9446 | -0.2690 | 0.6998 | rejected |
| POL/USDT | P50_200 | 107 | 1.0734 | 0.8265 | 1.0734 | 0.4590 | 0.8377 | exploratory signal |
| POL/USDT | P55_100 | 110 | 0.9075 | 0.6112 | 0.9075 | -0.4775 | 0.6129 | rejected |
| POL/USDT | P55_144 | 111 | 0.9230 | 0.6767 | 0.9230 | -0.3916 | 0.6806 | rejected |
| POL/USDT | P55_200 | 99 | 0.9353 | 0.7154 | 0.9353 | -0.3190 | 0.7271 | rejected |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.3857 | 1.6086 | 1.8688 | 1.3924 | exploratory signal |
| POPCAT/USDT | P89_200 | 100 | 0.9222 | 0.6969 | 0.9222 | -0.4260 | 0.7053 | rejected |
| POPCAT/USDT | P8_100 | 151 | 0.9269 | 0.7412 | 0.9521 | -0.2703 | 0.7604 | rejected |
| PUFFER/USDT | P12_144 | 125 | 1.0180 | 0.8705 | 1.0334 | 0.2892 | 0.8857 | exploratory signal |
| PUFFER/USDT | P12_200 | 86 | 1.0253 | 0.9111 | 1.0483 | 0.3168 | 0.9320 | exploratory signal |
| PUFFER/USDT | P20_100 | 127 | 0.9987 | 0.8128 | 0.9987 | 0.0576 | 0.8189 | rejected |
| PUFFER/USDT | P20_144 | 118 | 1.1089 | 0.9362 | 1.1089 | 0.7429 | 0.9387 | exploratory signal |
| PUFFER/USDT | P20_200 | 81 | 1.3768 | 1.2245 | 1.4038 | 1.8699 | 1.2514 | credible candidate |
| PUFFER/USDT | P20_50 | 155 | 0.9023 | 0.6848 | 0.9023 | -0.7081 | 0.6900 | rejected |
| PUFFER/USDT | P20_55 | 160 | 0.9214 | 0.7100 | 0.9214 | -0.5587 | 0.7157 | rejected |
| PUFFER/USDT | P20_89 | 142 | 1.0335 | 0.8298 | 1.0335 | 0.3146 | 0.8384 | exploratory signal |
| PUFFER/USDT | P21_100 | 124 | 1.0165 | 0.8247 | 1.0165 | 0.1770 | 0.8292 | exploratory signal |
| PUFFER/USDT | P21_144 | 117 | 1.1255 | 0.9456 | 1.1255 | 0.8333 | 0.9476 | exploratory signal |
| PUFFER/USDT | P21_200 | 75 | 1.3497 | 1.1974 | 1.3789 | 1.7012 | 1.2253 | exploratory signal |
| PUFFER/USDT | P21_50 | 152 | 0.9302 | 0.6988 | 0.9302 | -0.4729 | 0.7050 | rejected |
| PUFFER/USDT | P21_55 | 158 | 0.9857 | 0.7545 | 0.9857 | -0.0345 | 0.7580 | rejected |
| PUFFER/USDT | P21_89 | 142 | 1.0043 | 0.8057 | 1.0043 | 0.1028 | 0.8150 | exploratory signal |
| PUFFER/USDT | P26_100 | 125 | 1.0562 | 0.8516 | 1.0562 | 0.4363 | 0.8536 | exploratory signal |
| PUFFER/USDT | P26_144 | 109 | 1.1473 | 0.9629 | 1.1473 | 0.9379 | 0.9675 | exploratory signal |
| PUFFER/USDT | P26_200 | 75 | 1.2674 | 1.1244 | 1.2674 | 1.2929 | 1.1275 | exploratory signal |
| PUFFER/USDT | P26_89 | 148 | 0.9311 | 0.7353 | 0.9311 | -0.4512 | 0.7371 | rejected |
| PUFFER/USDT | P34_100 | 126 | 0.9898 | 0.7849 | 0.9898 | -0.0012 | 0.7828 | rejected |
| PUFFER/USDT | P34_144 | 111 | 0.9011 | 0.7449 | 0.9011 | -0.6032 | 0.7458 | rejected |
| PUFFER/USDT | P34_200 | 84 | 1.0033 | 0.8654 | 1.0033 | 0.0729 | 0.8663 | exploratory signal |
| PUFFER/USDT | P34_89 | 134 | 0.9084 | 0.7087 | 0.9084 | -0.5925 | 0.7081 | rejected |
| PUFFER/USDT | P8_50 | 192 | 0.9280 | 0.7443 | 0.9376 | -0.4620 | 0.7554 | rejected |
| PUFFER/USDT | P8_55 | 194 | 0.9206 | 0.7494 | 0.9298 | -0.5497 | 0.7630 | rejected |
| PUFFER/USDT | P8_89 | 154 | 0.9604 | 0.7910 | 0.9727 | -0.1352 | 0.8051 | rejected |
| PUNDIX/USDT | P8_200 | 65 | 1.0990 | 0.8182 | 1.0990 | 0.4198 | 0.8066 | exploratory signal |
| PYTH/USDT | P100_200 | 92 | 0.9926 | 0.7968 | 0.9926 | 0.0135 | 0.7949 | rejected |
| PYTH/USDT | P12_200 | 86 | 1.0996 | 0.9736 | 1.1151 | 0.5664 | 0.9786 | exploratory signal |
| PYTH/USDT | P20_200 | 83 | 0.9210 | 0.7979 | 0.9398 | -0.2524 | 0.8104 | rejected |
| PYTH/USDT | P21_200 | 82 | 0.9457 | 0.8190 | 0.9863 | -0.0182 | 0.8523 | rejected |
| PYTH/USDT | P89_100 | 34 | 1.0014 | 0.6970 | 1.0014 | 0.0353 | 0.6962 | exploratory signal |
| PYTH/USDT | P89_144 | 103 | 0.9634 | 0.7192 | 0.9634 | -0.1416 | 0.7158 | rejected |
| PYTH/USDT | P89_200 | 92 | 1.0428 | 0.8401 | 1.0428 | 0.2635 | 0.8402 | exploratory signal |
| PYTH/USDT | P8_200 | 82 | 1.1827 | 1.0553 | 1.1983 | 0.8804 | 1.0603 | exploratory signal |
| QI/USDT | P34_100 | 140 | 0.9046 | 0.6384 | 0.9046 | -0.5697 | 0.6452 | rejected |
| QNT/USDT | P8_89 | 241 | 0.9048 | 0.6645 | 0.9048 | -0.7340 | 0.6674 | rejected |
| RENDER/USDT | P100_200 | 80 | 1.0132 | 0.7607 | 1.0132 | 0.1181 | 0.7627 | exploratory signal |
| RENDER/USDT | P12_200 | 38 | 0.9376 | 0.8374 | 1.0182 | 0.1059 | 0.9069 | exploratory signal |
| RENDER/USDT | P144_200 | 52 | 1.1981 | 0.8153 | 1.1981 | 0.7722 | 0.8216 | exploratory signal |
| RENDER/USDT | P20_200 | 77 | 1.1067 | 0.9454 | 1.1739 | 0.8885 | 1.0086 | exploratory signal |
| RENDER/USDT | P21_200 | 77 | 1.0495 | 0.8963 | 1.1167 | 0.6311 | 0.9599 | exploratory signal |
| RENDER/USDT | P26_200 | 77 | 0.9359 | 0.7899 | 1.0050 | 0.0767 | 0.8480 | exploratory signal |
| RENDER/USDT | P50_200 | 99 | 0.9508 | 0.7613 | 0.9693 | -0.1305 | 0.7882 | rejected |
| RENDER/USDT | P55_200 | 102 | 0.9327 | 0.7413 | 0.9327 | -0.3738 | 0.7545 | rejected |
| RENDER/USDT | P8_100 | 134 | 0.9351 | 0.7703 | 0.9901 | 0.0030 | 0.8092 | rejected |
| RENDER/USDT | P8_144 | 85 | 1.0762 | 0.9168 | 1.0879 | 0.5248 | 0.9251 | exploratory signal |
| RENDER/USDT | P8_200 | 45 | 1.1898 | 1.0722 | 1.1898 | 0.7068 | 1.0727 | exploratory signal |
| RENDER/USDT | P8_55 | 192 | 0.9033 | 0.7002 | 0.9033 | -0.7206 | 0.7005 | rejected |
| RENDER/USDT | P8_89 | 140 | 0.9705 | 0.7835 | 1.0104 | 0.1370 | 0.8124 | exploratory signal |
| REZ/USDT | P12_100 | 187 | 0.9874 | 0.8005 | 0.9955 | 0.0388 | 0.8185 | rejected |
| REZ/USDT | P12_89 | 198 | 1.0033 | 0.8112 | 1.0033 | 0.1014 | 0.8189 | exploratory signal |
| REZ/USDT | P20_100 | 191 | 0.9459 | 0.7514 | 0.9545 | -0.2917 | 0.7699 | rejected |
| REZ/USDT | P20_144 | 153 | 0.9630 | 0.7880 | 0.9741 | -0.1208 | 0.8094 | rejected |
| REZ/USDT | P20_200 | 143 | 0.9135 | 0.7392 | 0.9384 | -0.3670 | 0.7695 | rejected |
| REZ/USDT | P21_100 | 190 | 0.9750 | 0.7739 | 0.9837 | -0.0547 | 0.7928 | rejected |
| REZ/USDT | P21_144 | 153 | 0.9859 | 0.8057 | 0.9969 | 0.0446 | 0.8289 | rejected |
| REZ/USDT | P21_200 | 143 | 0.9396 | 0.7612 | 0.9645 | -0.1820 | 0.7924 | rejected |
| REZ/USDT | P26_100 | 186 | 0.9314 | 0.7301 | 0.9401 | -0.4134 | 0.7520 | rejected |
| REZ/USDT | P26_144 | 152 | 0.9388 | 0.7555 | 0.9496 | -0.3124 | 0.7821 | rejected |
| REZ/USDT | P26_200 | 140 | 0.9514 | 0.7684 | 0.9761 | -0.1046 | 0.8049 | rejected |
| REZ/USDT | P34_100 | 170 | 1.0699 | 0.8288 | 1.0795 | 0.6484 | 0.8556 | exploratory signal |
| REZ/USDT | P34_144 | 139 | 0.9114 | 0.7295 | 0.9355 | -0.4035 | 0.7665 | rejected |
| REZ/USDT | P34_200 | 130 | 0.9116 | 0.7374 | 0.9377 | -0.3732 | 0.7753 | rejected |
| REZ/USDT | P34_89 | 185 | 0.9496 | 0.7172 | 0.9582 | -0.2558 | 0.7376 | rejected |
| REZ/USDT | P50_100 | 148 | 1.1978 | 0.8830 | 1.2097 | 1.3350 | 0.9037 | exploratory signal |
| REZ/USDT | P50_144 | 124 | 1.0666 | 0.8348 | 1.0807 | 0.5542 | 0.8601 | exploratory signal |
| REZ/USDT | P50_200 | 121 | 1.0316 | 0.8121 | 1.0467 | 0.3391 | 0.8336 | exploratory signal |
| REZ/USDT | P50_89 | 149 | 1.0164 | 0.7419 | 1.0277 | 0.2465 | 0.7542 | exploratory signal |
| REZ/USDT | P55_100 | 140 | 1.0907 | 0.7977 | 1.0907 | 0.6145 | 0.8018 | exploratory signal |
| REZ/USDT | P55_200 | 117 | 0.9239 | 0.7127 | 0.9239 | -0.4045 | 0.7170 | rejected |
| REZ/USDT | P55_89 | 146 | 0.9658 | 0.6919 | 0.9658 | -0.1597 | 0.6934 | rejected |
| REZ/USDT | P8_100 | 199 | 0.9933 | 0.8213 | 0.9933 | 0.0232 | 0.8274 | rejected |
| REZ/USDT | P8_200 | 156 | 0.9129 | 0.7580 | 0.9251 | -0.4601 | 0.7708 | rejected |
| REZ/USDT | P8_89 | 210 | 1.0247 | 0.8414 | 1.0247 | 0.2703 | 0.8449 | exploratory signal |
| RIO/USDT | P12_144 | 152 | 0.9022 | 0.8102 | 0.9261 | -0.4661 | 0.8351 | rejected |
| RLC/USDT | P12_100 | 168 | 0.9881 | 0.7423 | 0.9881 | -0.0115 | 0.7397 | rejected |
| RLC/USDT | P12_200 | 85 | 1.2384 | 0.9590 | 1.2384 | 1.0364 | 0.9507 | exploratory signal |
| RLC/USDT | P12_89 | 172 | 0.9291 | 0.6960 | 0.9291 | -0.4296 | 0.6921 | rejected |
| RLC/USDT | P8_100 | 168 | 0.9097 | 0.6943 | 0.8967 | -0.6407 | 0.6738 | rejected |
| RLC/USDT | P8_200 | 65 | 1.0824 | 0.8806 | 1.0313 | 0.1685 | 0.8204 | exploratory signal |
| ROSE/USDT | P100_144 | 87 | 0.9125 | 0.6428 | 0.9125 | -0.4061 | 0.6468 | rejected |
| ROSE/USDT | P100_200 | 101 | 0.9886 | 0.7548 | 1.0075 | 0.0928 | 0.7681 | exploratory signal |
| ROSE/USDT | P12_144 | 112 | 1.1053 | 0.9046 | 1.1243 | 0.7585 | 0.9296 | exploratory signal |
| ROSE/USDT | P12_200 | 55 | 1.1550 | 1.0027 | 1.3298 | 1.2553 | 1.1638 | exploratory signal |
| ROSE/USDT | P20_144 | 132 | 0.9588 | 0.7775 | 0.9753 | -0.1040 | 0.8020 | rejected |
| ROSE/USDT | P20_200 | 110 | 0.9944 | 0.8114 | 1.0445 | 0.3114 | 0.8630 | exploratory signal |
| ROSE/USDT | P21_144 | 131 | 0.9459 | 0.7673 | 0.9788 | -0.0791 | 0.8056 | rejected |
| ROSE/USDT | P21_200 | 102 | 1.0126 | 0.8310 | 1.0661 | 0.4178 | 0.8853 | exploratory signal |
| ROSE/USDT | P26_144 | 146 | 1.0084 | 0.8048 | 1.0084 | 0.1205 | 0.8164 | exploratory signal |
| ROSE/USDT | P26_200 | 108 | 0.9941 | 0.8066 | 0.9941 | 0.0205 | 0.8187 | rejected |
| ROSE/USDT | P34_144 | 137 | 0.9440 | 0.7443 | 0.9440 | -0.3114 | 0.7541 | rejected |
| ROSE/USDT | P34_200 | 88 | 1.3328 | 1.1080 | 1.3328 | 1.5329 | 1.1197 | exploratory signal |
| ROSE/USDT | P50_144 | 146 | 0.9461 | 0.7388 | 0.9461 | -0.3046 | 0.7477 | rejected |
| ROSE/USDT | P50_200 | 109 | 1.1723 | 0.9428 | 1.1723 | 0.9704 | 0.9541 | exploratory signal |
| ROSE/USDT | P55_144 | 140 | 0.9555 | 0.7495 | 0.9555 | -0.2286 | 0.7558 | rejected |
| ROSE/USDT | P55_200 | 112 | 1.3264 | 1.0651 | 1.3264 | 1.6361 | 1.0699 | exploratory signal |
| ROSE/USDT | P89_200 | 110 | 0.9298 | 0.7239 | 0.9470 | -0.2399 | 0.7351 | rejected |
| ROSE/USDT | P8_144 | 104 | 1.1021 | 0.9062 | 1.1673 | 0.9102 | 0.9632 | exploratory signal |
| RPL/USDT | P12_144 | 143 | 1.0708 | 0.9015 | 1.0035 | 0.0888 | 0.8366 | exploratory signal |
| RPL/USDT | P12_200 | 140 | 0.9506 | 0.8016 | 0.9506 | -0.2697 | 0.8068 | rejected |
| RPL/USDT | P20_200 | 117 | 0.9476 | 0.7864 | 0.9721 | -0.1177 | 0.8158 | rejected |
| RPL/USDT | P21_200 | 129 | 0.9318 | 0.7690 | 0.9318 | -0.3950 | 0.7793 | rejected |
| RPL/USDT | P26_200 | 121 | 0.9126 | 0.7530 | 0.9099 | -0.5458 | 0.7629 | rejected |
| RPL/USDT | P8_200 | 133 | 0.9132 | 0.7637 | 0.8996 | -0.5925 | 0.7532 | rejected |
| RSR/USDT | P100_144 | 73 | 0.9423 | 0.6896 | 0.9423 | -0.2316 | 0.6977 | rejected |
| RSR/USDT | P100_200 | 83 | 1.0705 | 0.8426 | 1.0705 | 0.3785 | 0.8440 | exploratory signal |
| RSR/USDT | P12_200 | 90 | 0.9845 | 0.8112 | 0.9473 | -0.2323 | 0.7813 | rejected |
| RSR/USDT | P26_200 | 107 | 0.9154 | 0.7650 | 0.8812 | -0.6779 | 0.7427 | rejected |
| RSR/USDT | P50_144 | 130 | 0.9495 | 0.7521 | 0.9495 | -0.2592 | 0.7573 | rejected |
| RSR/USDT | P50_200 | 101 | 0.9020 | 0.7377 | 0.9020 | -0.5031 | 0.7403 | rejected |
| RUNE/USDT | P20_144 | 109 | 0.9411 | 0.7199 | 0.9411 | -0.2818 | 0.7212 | rejected |
| RUNE/USDT | P20_200 | 85 | 1.0483 | 0.8348 | 1.0483 | 0.2863 | 0.8419 | exploratory signal |
| RUNE/USDT | P20_89 | 155 | 0.9006 | 0.6464 | 0.9006 | -0.6335 | 0.6499 | rejected |
| RUNE/USDT | P21_144 | 113 | 1.0021 | 0.7644 | 1.0021 | 0.0685 | 0.7678 | exploratory signal |
| RUNE/USDT | P21_200 | 85 | 1.0483 | 0.8348 | 1.0483 | 0.2864 | 0.8419 | exploratory signal |
| RUNE/USDT | P21_89 | 151 | 0.9044 | 0.6475 | 0.9044 | -0.6000 | 0.6523 | rejected |
| RUNE/USDT | P26_144 | 113 | 0.9245 | 0.6954 | 0.9245 | -0.3794 | 0.6938 | rejected |
| RUNE/USDT | P26_200 | 75 | 0.9751 | 0.7703 | 0.9751 | -0.0732 | 0.7772 | rejected |
| RUNE/USDT | P34_100 | 134 | 1.0358 | 0.7107 | 1.0358 | 0.2739 | 0.7125 | exploratory signal |
| RUNE/USDT | P34_144 | 116 | 1.1851 | 0.8774 | 1.1851 | 1.0186 | 0.8801 | exploratory signal |
| RUNE/USDT | P34_200 | 92 | 0.9764 | 0.7556 | 0.9764 | -0.0712 | 0.7569 | rejected |
| RUNE/USDT | P34_89 | 137 | 0.9841 | 0.6552 | 0.9841 | -0.0359 | 0.6575 | rejected |
| RUNE/USDT | P50_100 | 124 | 1.1003 | 0.7169 | 1.1003 | 0.6052 | 0.7170 | exploratory signal |
| RUNE/USDT | P50_144 | 120 | 1.5230 | 1.0963 | 1.5230 | 2.4239 | 1.1018 | exploratory signal |
| RUNE/USDT | P50_200 | 89 | 1.3239 | 1.0048 | 1.3239 | 1.4254 | 1.0085 | exploratory signal |
| RUNE/USDT | P50_89 | 129 | 0.9216 | 0.5749 | 0.9216 | -0.4074 | 0.5696 | rejected |
| RUNE/USDT | P55_100 | 113 | 1.0783 | 0.6967 | 1.0783 | 0.4854 | 0.7098 | exploratory signal |
| RUNE/USDT | P55_144 | 112 | 1.3458 | 0.9527 | 1.3458 | 1.6928 | 0.9594 | exploratory signal |
| RUNE/USDT | P55_200 | 91 | 1.2958 | 0.9705 | 1.2958 | 1.3161 | 0.9697 | exploratory signal |
| RUNE/USDT | P89_144 | 85 | 0.9565 | 0.6079 | 0.9565 | -0.1637 | 0.6096 | rejected |
| RUNE/USDT | P89_200 | 77 | 1.0496 | 0.7498 | 1.0496 | 0.2587 | 0.7426 | exploratory signal |
| RUNE/USDT | P8_144 | 109 | 0.9930 | 0.8034 | 0.9899 | -0.0010 | 0.8029 | rejected |
| RUNE/USDT | P8_200 | 94 | 0.9560 | 0.7585 | 0.9406 | -0.2651 | 0.7526 | rejected |
| SAFE/USDT | P12_100 | 189 | 0.9264 | 0.7565 | 0.9264 | -0.5293 | 0.7676 | rejected |
| SAFE/USDT | P12_144 | 161 | 0.9527 | 0.8041 | 0.9527 | -0.2808 | 0.8126 | rejected |
| SAFE/USDT | P21_144 | 143 | 0.9110 | 0.7439 | 0.9110 | -0.5412 | 0.7472 | rejected |
| SAFE/USDT | P21_200 | 126 | 0.9264 | 0.7729 | 0.9264 | -0.3979 | 0.7734 | rejected |
| SAFE/USDT | P26_144 | 147 | 0.9550 | 0.7758 | 0.9550 | -0.2433 | 0.7814 | rejected |
| SAFE/USDT | P26_200 | 125 | 0.9719 | 0.8060 | 0.9719 | -0.1152 | 0.8102 | rejected |
| SAFE/USDT | P34_100 | 170 | 0.9359 | 0.7324 | 0.9359 | -0.4169 | 0.7419 | rejected |
| SAFE/USDT | P34_200 | 125 | 0.9647 | 0.7927 | 0.9647 | -0.1635 | 0.7991 | rejected |
| SAFE/USDT | P8_200 | 159 | 0.9145 | 0.7744 | 0.9145 | -0.5611 | 0.7802 | rejected |
| SAND/USDT | P12_200 | 53 | 0.9562 | 0.7462 | 0.9562 | -0.1369 | 0.7524 | rejected |
| SAND/USDT | P89_100 | 34 | 0.9059 | 0.5466 | 0.9059 | -0.2607 | 0.5454 | rejected |
| SAND/USDT | P8_200 | 48 | 1.0183 | 0.7866 | 1.0906 | 0.3676 | 0.8588 | exploratory signal |
| SATS/USDT | P12_200 | 117 | 0.9411 | 0.7815 | 0.9375 | -0.3103 | 0.7762 | rejected |
| SATS/USDT | P8_200 | 97 | 0.9425 | 0.7952 | 0.9706 | -0.1061 | 0.8149 | rejected |
| SEI/USDT | P20_200 | 92 | 0.9671 | 0.8005 | 0.9160 | -0.3973 | 0.7541 | rejected |
| SEI/USDT | P21_200 | 93 | 0.9043 | 0.7480 | 0.8606 | -0.7263 | 0.7093 | rejected |
| SEI/USDT | P89_144 | 83 | 0.9147 | 0.6312 | 0.9147 | -0.3568 | 0.6221 | rejected |
| SHIB/USDT | P100_200 | 86 | 0.9685 | 0.6615 | 0.9685 | -0.1050 | 0.6629 | rejected |
| SHIB/USDT | P89_200 | 86 | 0.9629 | 0.6624 | 0.9629 | -0.1369 | 0.6706 | rejected |
| SKL/USDT | P100_200 | 96 | 1.0966 | 0.8177 | 1.1170 | 0.5966 | 0.8224 | exploratory signal |
| SKL/USDT | P21_200 | 134 | 0.9013 | 0.7353 | 0.9289 | -0.3853 | 0.7553 | rejected |
| SKL/USDT | P50_200 | 106 | 0.9288 | 0.7273 | 0.9456 | -0.2509 | 0.7418 | rejected |
| SKL/USDT | P89_144 | 93 | 0.9012 | 0.6329 | 0.9012 | -0.4652 | 0.6305 | rejected |
| SKL/USDT | P89_200 | 92 | 1.0809 | 0.8229 | 1.1018 | 0.5174 | 0.8261 | exploratory signal |
| SKL/USDT | P8_144 | 168 | 0.9058 | 0.7216 | 0.9445 | -0.3287 | 0.7531 | rejected |
| SKY/USDT | P12_100 | 122 | 0.9032 | 0.6701 | 0.9032 | -0.5538 | 0.6581 | rejected |
| SKY/USDT | P12_144 | 99 | 0.9564 | 0.7450 | 0.9564 | -0.1858 | 0.7332 | rejected |
| SKY/USDT | P12_200 | 82 | 1.0150 | 0.8204 | 1.0150 | 0.1313 | 0.8193 | exploratory signal |
| SKY/USDT | P20_200 | 84 | 0.9697 | 0.7907 | 0.9697 | -0.1098 | 0.7893 | rejected |
| SKY/USDT | P21_144 | 86 | 0.9375 | 0.7449 | 0.9375 | -0.2832 | 0.7397 | rejected |
| SKY/USDT | P21_200 | 85 | 0.9435 | 0.7687 | 0.9435 | -0.2589 | 0.7679 | rejected |
| SKY/USDT | P55_200 | 103 | 0.9087 | 0.7052 | 0.9087 | -0.5157 | 0.7075 | rejected |
| SKY/USDT | P8_200 | 83 | 0.9454 | 0.7768 | 0.9660 | -0.1277 | 0.7890 | rejected |
| SNX/USDT | P8_200 | 117 | 0.9630 | 0.7876 | 0.9456 | -0.2651 | 0.7745 | rejected |
| SOL/USDT | P12_144 | 95 | 0.9956 | 0.7535 | 0.9956 | 0.0288 | 0.7571 | rejected |
| SOL/USDT | P20_200 | 59 | 1.0622 | 0.8417 | 1.0622 | 0.2898 | 0.8424 | exploratory signal |
| SOL/USDT | P21_200 | 61 | 1.0525 | 0.8280 | 1.0525 | 0.2566 | 0.8324 | exploratory signal |
| SOL/USDT | P26_34 | 46 | 0.9049 | 0.5583 | 0.9049 | -0.3227 | 0.5641 | rejected |
| SOL/USDT | P8_12 | 75 | 1.0103 | 0.5686 | 1.0103 | 0.0908 | 0.5751 | exploratory signal |
| SQD/USDT | P12_144 | 132 | 0.9426 | 0.7871 | 0.9573 | -0.1994 | 0.7943 | rejected |
| SQD/USDT | P20_144 | 136 | 0.9321 | 0.7705 | 0.9457 | -0.2901 | 0.7833 | rejected |
| SQD/USDT | P20_200 | 114 | 0.9798 | 0.8288 | 0.9787 | -0.0634 | 0.8261 | rejected |
| SQD/USDT | P21_144 | 136 | 0.9033 | 0.7453 | 0.9030 | -0.5786 | 0.7455 | rejected |
| SQD/USDT | P21_200 | 115 | 0.9272 | 0.7859 | 0.9441 | -0.2683 | 0.7979 | rejected |
| SQD/USDT | P26_200 | 106 | 0.9214 | 0.7822 | 0.9390 | -0.2988 | 0.7995 | rejected |
| SSV/USDT | P100_144 | 104 | 0.9542 | 0.6518 | 0.9542 | -0.1895 | 0.6500 | rejected |
| SSV/USDT | P8_200 | 43 | 1.1153 | 0.9729 | 0.6742 | -1.6093 | 0.5765 | rejected |
| STRK/USDT | P12_26 | 140 | 0.9571 | 0.6878 | 0.9571 | -0.1954 | 0.6742 | rejected |
| STRK/USDT | P12_89 | 183 | 0.9121 | 0.7231 | 0.9008 | -0.6953 | 0.7184 | rejected |
| STRK/USDT | P20_200 | 90 | 1.0054 | 0.8525 | 1.0262 | 0.1873 | 0.8774 | exploratory signal |
| STRK/USDT | P21_200 | 89 | 1.0272 | 0.8690 | 1.0486 | 0.2976 | 0.8937 | exploratory signal |
| STRK/USDT | P26_200 | 103 | 0.9659 | 0.7895 | 0.9659 | -0.1378 | 0.7939 | rejected |
| STRK/USDT | P34_144 | 114 | 1.0274 | 0.8291 | 1.0274 | 0.2103 | 0.8305 | exploratory signal |
| STRK/USDT | P34_200 | 98 | 0.9629 | 0.7925 | 0.9629 | -0.1494 | 0.7958 | rejected |
| STRK/USDT | P50_100 | 110 | 0.9058 | 0.6745 | 0.9058 | -0.5291 | 0.6892 | rejected |
| STRK/USDT | P50_144 | 119 | 1.0772 | 0.8439 | 1.0926 | 0.5965 | 0.8699 | exploratory signal |
| STRK/USDT | P50_200 | 107 | 0.9968 | 0.8124 | 1.0148 | 0.1371 | 0.8313 | exploratory signal |
| STRK/USDT | P55_100 | 105 | 0.9240 | 0.6840 | 0.9240 | -0.3918 | 0.6948 | rejected |
| STRK/USDT | P55_144 | 111 | 1.1000 | 0.8610 | 1.1166 | 0.7062 | 0.8895 | exploratory signal |
| STRK/USDT | P55_200 | 103 | 1.0455 | 0.8521 | 1.0646 | 0.3961 | 0.8724 | exploratory signal |
| STRK/USDT | P8_200 | 84 | 0.9225 | 0.7917 | 0.9019 | -0.4649 | 0.7771 | rejected |
| STRK/USDT | P8_89 | 177 | 0.9290 | 0.7509 | 0.9412 | -0.3656 | 0.7659 | rejected |
| STX/USDT | P100_200 | 92 | 1.1125 | 0.8386 | 1.1125 | 0.6028 | 0.8453 | exploratory signal |
| STX/USDT | P21_34 | 114 | 0.9847 | 0.6581 | 0.9847 | -0.0292 | 0.6591 | rejected |
| STX/USDT | P89_144 | 94 | 0.9259 | 0.6534 | 0.9259 | -0.3399 | 0.6539 | rejected |
| STX/USDT | P89_200 | 97 | 1.0656 | 0.8008 | 1.0656 | 0.3889 | 0.8061 | exploratory signal |
| STX/USDT | P8_12 | 103 | 0.9326 | 0.5741 | 0.9326 | -0.3191 | 0.5815 | rejected |
| SUI/USDT | P100_200 | 88 | 0.9169 | 0.6474 | 0.9169 | -0.3599 | 0.6408 | rejected |
| SUI/USDT | P20_200 | 84 | 0.9635 | 0.7976 | 0.9635 | -0.1297 | 0.7955 | rejected |
| SUI/USDT | P21_200 | 81 | 0.9460 | 0.7835 | 0.9460 | -0.2104 | 0.7796 | rejected |
| SUI/USDT | P26_200 | 74 | 0.9897 | 0.8235 | 0.9897 | 0.0003 | 0.8174 | rejected |
| SUI/USDT | P34_144 | 125 | 0.9569 | 0.7239 | 0.9569 | -0.1981 | 0.7216 | rejected |
| SUI/USDT | P50_200 | 89 | 1.0688 | 0.8562 | 1.0688 | 0.3731 | 0.8511 | exploratory signal |
| SUI/USDT | P55_200 | 93 | 1.0000 | 0.7925 | 1.0000 | 0.0512 | 0.7878 | rejected |
| SUI/USDT | P8_144 | 131 | 1.0759 | 0.8694 | 1.0759 | 0.5080 | 0.8721 | exploratory signal |
| SUPER/USDT | P12_100 | 165 | 0.9382 | 0.7142 | 0.9382 | -0.3373 | 0.7042 | rejected |
| SUPER/USDT | P12_144 | 143 | 0.9046 | 0.6993 | 0.9046 | -0.5523 | 0.6950 | rejected |
| SUPER/USDT | P20_144 | 161 | 0.9367 | 0.7072 | 0.9367 | -0.3499 | 0.6995 | rejected |
| SUPER/USDT | P21_144 | 160 | 0.9251 | 0.6975 | 0.9251 | -0.4306 | 0.6910 | rejected |
| SUPER/USDT | P21_200 | 125 | 0.9149 | 0.7026 | 0.9149 | -0.4395 | 0.6939 | rejected |
| SUPER/USDT | P26_100 | 173 | 0.9764 | 0.6854 | 0.9764 | -0.0854 | 0.6768 | rejected |
| SUPER/USDT | P26_144 | 145 | 0.9365 | 0.6889 | 0.9365 | -0.3292 | 0.6793 | rejected |
| SUPER/USDT | P26_200 | 126 | 0.9466 | 0.7147 | 0.9466 | -0.2471 | 0.7049 | rejected |
| SUPER/USDT | P26_89 | 173 | 0.9203 | 0.6411 | 0.9203 | -0.4816 | 0.6390 | rejected |
| SUPER/USDT | P34_100 | 149 | 1.1442 | 0.7965 | 1.1442 | 0.8997 | 0.7955 | exploratory signal |
| SUPER/USDT | P34_144 | 131 | 1.0830 | 0.7905 | 1.0830 | 0.5153 | 0.7804 | exploratory signal |
| SUPER/USDT | P34_200 | 110 | 0.9414 | 0.7175 | 0.9414 | -0.2664 | 0.7104 | rejected |
| SUPER/USDT | P34_89 | 150 | 1.0662 | 0.7240 | 1.0662 | 0.4677 | 0.7261 | exploratory signal |
| SUPER/USDT | P50_144 | 118 | 0.9901 | 0.6906 | 0.9901 | 0.0041 | 0.6804 | rejected |
| SUPER/USDT | P55_144 | 118 | 1.0886 | 0.7424 | 1.0886 | 0.5242 | 0.7396 | exploratory signal |
| SUPER/USDT | P89_144 | 96 | 0.9999 | 0.6393 | 0.9999 | 0.0517 | 0.6355 | rejected |
| SUPER/USDT | P8_144 | 118 | 0.9462 | 0.7679 | 0.9119 | -0.4810 | 0.7411 | rejected |
| SUPER/USDT | P8_200 | 64 | 1.2855 | 1.0890 | 1.1483 | 0.6273 | 0.9667 | exploratory signal |
| SYN/USDT | P12_144 | 126 | 1.1604 | 0.9935 | 1.1393 | 0.8500 | 0.9746 | exploratory signal |
| SYN/USDT | P12_200 | 100 | 1.0544 | 0.9139 | 1.0313 | 0.2189 | 0.8922 | exploratory signal |
| SYN/USDT | P20_144 | 107 | 0.9379 | 0.7984 | 0.9379 | -0.3083 | 0.8002 | rejected |
| SYN/USDT | P20_200 | 99 | 1.2628 | 1.0678 | 1.2314 | 1.1317 | 1.0362 | exploratory signal |
| SYN/USDT | P21_144 | 106 | 0.9548 | 0.8111 | 0.9548 | -0.2067 | 0.8132 | rejected |
| SYN/USDT | P21_200 | 96 | 1.1508 | 0.9775 | 1.1225 | 0.6509 | 0.9503 | exploratory signal |
| SYN/USDT | P26_144 | 121 | 0.9692 | 0.8202 | 0.9692 | -0.1325 | 0.8230 | rejected |
| SYN/USDT | P26_200 | 91 | 1.1537 | 1.0032 | 1.1537 | 0.7813 | 1.0030 | exploratory signal |
| SYN/USDT | P34_144 | 122 | 0.9150 | 0.7661 | 0.9150 | -0.4947 | 0.7708 | rejected |
| SYN/USDT | P34_200 | 100 | 0.9868 | 0.8317 | 0.9868 | -0.0177 | 0.8313 | rejected |
| TAIKO/USDT | P8_144 | 70 | 0.9576 | 0.7224 | 0.7411 | -1.3454 | 0.5279 | rejected |
| TAO/USDT | P26_100 | 125 | 0.9269 | 0.7463 | 0.9269 | -0.4106 | 0.7544 | rejected |
| TAO/USDT | P26_144 | 99 | 0.9286 | 0.7694 | 0.9286 | -0.3430 | 0.7721 | rejected |
| TAO/USDT | P26_200 | 94 | 0.9525 | 0.7826 | 0.9525 | -0.1967 | 0.7839 | rejected |
| TAO/USDT | P26_89 | 126 | 0.9390 | 0.7540 | 0.9390 | -0.3279 | 0.7609 | rejected |
| TAO/USDT | P34_200 | 87 | 0.9297 | 0.7531 | 0.9297 | -0.3199 | 0.7588 | rejected |
| TAO/USDT | P50_144 | 112 | 0.9694 | 0.7755 | 0.9694 | -0.1282 | 0.7857 | rejected |
| TAO/USDT | P50_200 | 97 | 0.9468 | 0.7600 | 0.9468 | -0.2458 | 0.7690 | rejected |
| TAO/USDT | P50_89 | 90 | 0.9602 | 0.7398 | 0.9602 | -0.1567 | 0.7444 | rejected |
| TAO/USDT | P55_100 | 94 | 0.9879 | 0.7575 | 0.9879 | -0.0136 | 0.7677 | rejected |
| TAO/USDT | P55_200 | 99 | 0.9451 | 0.7601 | 0.9451 | -0.2604 | 0.7701 | rejected |
| TAO/USDT | P55_89 | 80 | 0.9266 | 0.7035 | 0.9266 | -0.3196 | 0.7086 | rejected |
| TAO/USDT | P8_12 | 62 | 1.1375 | 0.8113 | 1.1375 | 0.5655 | 0.8106 | exploratory signal |
| TAO/USDT | P8_200 | 103 | 0.9649 | 0.8047 | 0.9353 | -0.3344 | 0.7760 | rejected |
| THETA/USDT | P21_144 | 142 | 0.9202 | 0.7265 | 0.9202 | -0.4708 | 0.7309 | rejected |
| THETA/USDT | P34_200 | 114 | 1.0359 | 0.8202 | 1.0359 | 0.2578 | 0.8262 | exploratory signal |
| THETA/USDT | P50_200 | 108 | 1.0144 | 0.7939 | 1.0144 | 0.1340 | 0.7957 | exploratory signal |
| THETA/USDT | P55_100 | 118 | 0.9210 | 0.6594 | 0.9210 | -0.4303 | 0.6696 | rejected |
| THETA/USDT | P55_200 | 107 | 0.9962 | 0.7789 | 0.9962 | 0.0337 | 0.7843 | rejected |
| TIA/USDT | P12_89 | 174 | 0.9230 | 0.7548 | 0.9230 | -0.4734 | 0.7504 | rejected |
| TIA/USDT | P20_26 | 66 | 0.9455 | 0.6460 | 0.9455 | -0.1807 | 0.6335 | rejected |
| TIA/USDT | P20_34 | 121 | 0.9558 | 0.6850 | 0.9558 | -0.1810 | 0.6657 | rejected |
| TIA/USDT | P20_50 | 170 | 0.9391 | 0.7138 | 0.9391 | -0.3570 | 0.7120 | rejected |
| TIA/USDT | P20_55 | 174 | 0.9532 | 0.7414 | 0.9532 | -0.2594 | 0.7394 | rejected |
| TIA/USDT | P21_50 | 169 | 0.9261 | 0.7029 | 0.9261 | -0.4395 | 0.6971 | rejected |
| TIA/USDT | P50_55 | 44 | 0.9707 | 0.7068 | 0.9707 | -0.0695 | 0.7110 | rejected |
| TURBO/USDT | P100_200 | 94 | 1.1854 | 0.8730 | 1.1854 | 1.0207 | 0.8820 | exploratory signal |
| TURBO/USDT | P144_200 | 76 | 0.9357 | 0.6222 | 0.9357 | -0.2836 | 0.6268 | rejected |
| TURBO/USDT | P89_100 | 42 | 0.9622 | 0.6015 | 0.9622 | -0.1021 | 0.6021 | rejected |
| TURBO/USDT | P89_200 | 106 | 1.1383 | 0.8472 | 1.1383 | 0.8288 | 0.8518 | exploratory signal |
| TWT/USDT | P12_200 | 88 | 1.0652 | 0.8485 | 1.0652 | 0.3563 | 0.8443 | exploratory signal |
| TWT/USDT | P20_200 | 86 | 0.9587 | 0.7445 | 0.9587 | -0.1588 | 0.7461 | rejected |
| TWT/USDT | P21_200 | 87 | 0.9770 | 0.7569 | 0.9770 | -0.0660 | 0.7590 | rejected |
| TWT/USDT | P50_55 | 47 | 1.0374 | 0.5775 | 1.0374 | 0.1627 | 0.5754 | exploratory signal |
| TWT/USDT | P8_100 | 182 | 0.9300 | 0.6861 | 0.9300 | -0.4104 | 0.6700 | rejected |
| TWT/USDT | P8_144 | 125 | 0.9105 | 0.7061 | 0.9105 | -0.4742 | 0.6984 | rejected |
| TWT/USDT | P8_200 | 73 | 1.2604 | 1.0174 | 1.2604 | 1.0492 | 1.0098 | exploratory signal |
| T/USDT | P12_200 | 52 | 1.3272 | 1.0711 | 1.3272 | 1.0564 | 1.0559 | exploratory signal |
| T/USDT | P8_200 | 76 | 1.1102 | 0.8766 | 1.1102 | 0.5264 | 0.8725 | exploratory signal |
| UNI/USDT | P100_200 | 75 | 1.1924 | 0.9266 | 1.1924 | 0.8496 | 0.9283 | exploratory signal |
| UNI/USDT | P26_200 | 90 | 0.9399 | 0.7956 | 0.9399 | -0.2598 | 0.7943 | rejected |
| UNI/USDT | P34_200 | 90 | 0.9448 | 0.7861 | 0.9448 | -0.2327 | 0.7845 | rejected |
| UNI/USDT | P50_100 | 103 | 1.0131 | 0.7661 | 1.0131 | 0.1224 | 0.7622 | exploratory signal |
| UNI/USDT | P50_144 | 109 | 0.9999 | 0.7910 | 0.9999 | 0.0549 | 0.7824 | rejected |
| UNI/USDT | P50_200 | 87 | 1.0482 | 0.8707 | 1.0482 | 0.2814 | 0.8710 | exploratory signal |
| UNI/USDT | P50_55 | 34 | 1.0219 | 0.7080 | 1.0219 | 0.0961 | 0.7103 | exploratory signal |
| UNI/USDT | P50_89 | 100 | 1.0688 | 0.7893 | 1.0688 | 0.4019 | 0.7893 | exploratory signal |
| UNI/USDT | P55_100 | 96 | 0.9634 | 0.7207 | 0.9634 | -0.1359 | 0.7153 | rejected |
| UNI/USDT | P55_144 | 106 | 0.9770 | 0.7658 | 0.9770 | -0.0669 | 0.7572 | rejected |
| UNI/USDT | P55_200 | 87 | 1.0137 | 0.8406 | 1.0137 | 0.1159 | 0.8381 | exploratory signal |
| UNI/USDT | P55_89 | 92 | 1.0101 | 0.7438 | 1.0101 | 0.1004 | 0.7389 | exploratory signal |
| UNI/USDT | P89_200 | 74 | 1.0882 | 0.8601 | 1.0882 | 0.4329 | 0.8620 | exploratory signal |
| UNI/USDT | P8_12 | 59 | 0.9199 | 0.6678 | 0.9199 | -0.2986 | 0.6681 | rejected |
| VELO/USDT | P100_144 | 72 | 1.0367 | 0.7680 | 1.0367 | 0.2159 | 0.7833 | exploratory signal |
| VELO/USDT | P12_100 | 199 | 0.9387 | 0.7668 | 0.9387 | -0.3919 | 0.7650 | rejected |
| VELO/USDT | P12_144 | 164 | 1.0285 | 0.8620 | 1.0146 | 0.1650 | 0.8476 | exploratory signal |
| VELO/USDT | P12_200 | 114 | 1.2723 | 1.1009 | 1.2464 | 1.2649 | 1.0736 | exploratory signal |
| VELO/USDT | P12_34 | 186 | 0.9800 | 0.7257 | 0.9800 | -0.0802 | 0.7378 | rejected |
| VELO/USDT | P12_50 | 229 | 0.9025 | 0.6981 | 0.9025 | -0.7147 | 0.6938 | rejected |
| VELO/USDT | P12_55 | 233 | 0.9035 | 0.7015 | 0.9035 | -0.7209 | 0.6992 | rejected |
| VELO/USDT | P12_89 | 207 | 0.9359 | 0.7663 | 0.9359 | -0.4316 | 0.7668 | rejected |
| VELO/USDT | P20_100 | 189 | 0.9181 | 0.7458 | 0.9181 | -0.5339 | 0.7420 | rejected |
| VELO/USDT | P20_144 | 165 | 0.9434 | 0.7935 | 0.9434 | -0.3187 | 0.7898 | rejected |
| VELO/USDT | P20_200 | 107 | 1.2339 | 1.0705 | 1.2073 | 1.0530 | 1.0416 | exploratory signal |
| VELO/USDT | P21_100 | 182 | 0.9527 | 0.7731 | 0.9527 | -0.2639 | 0.7677 | rejected |
| VELO/USDT | P21_144 | 159 | 0.9020 | 0.7562 | 0.9020 | -0.6090 | 0.7529 | rejected |
| VELO/USDT | P21_200 | 103 | 1.1457 | 0.9912 | 1.1208 | 0.6524 | 0.9652 | exploratory signal |
| VELO/USDT | P26_100 | 168 | 0.9535 | 0.7587 | 0.9535 | -0.2590 | 0.7598 | rejected |
| VELO/USDT | P26_144 | 141 | 0.9300 | 0.7757 | 0.9300 | -0.3910 | 0.7744 | rejected |
| VELO/USDT | P26_200 | 114 | 0.9359 | 0.7999 | 0.9359 | -0.3086 | 0.7952 | rejected |
| VELO/USDT | P26_89 | 154 | 0.9300 | 0.7487 | 0.9300 | -0.4218 | 0.7522 | rejected |
| VELO/USDT | P34_144 | 137 | 0.9020 | 0.7453 | 0.9020 | -0.5904 | 0.7480 | rejected |
| VELO/USDT | P34_200 | 99 | 1.0471 | 0.8983 | 1.0471 | 0.2878 | 0.8927 | exploratory signal |
| VELO/USDT | P50_144 | 140 | 0.9167 | 0.7395 | 0.9167 | -0.4790 | 0.7393 | rejected |
| VELO/USDT | P50_200 | 113 | 0.9215 | 0.7688 | 0.9215 | -0.3974 | 0.7664 | rejected |
| VELO/USDT | P55_144 | 138 | 0.9516 | 0.7649 | 0.9516 | -0.2506 | 0.7678 | rejected |
| VELO/USDT | P55_200 | 114 | 0.9802 | 0.8140 | 0.9802 | -0.0543 | 0.8108 | rejected |
| VELO/USDT | P8_100 | 215 | 0.9367 | 0.7740 | 0.9268 | -0.5033 | 0.7627 | rejected |
| VELO/USDT | P8_144 | 161 | 1.0016 | 0.8442 | 0.9881 | -0.0128 | 0.8320 | rejected |
| VELO/USDT | P8_200 | 121 | 1.0152 | 0.8744 | 0.9969 | 0.0410 | 0.8546 | rejected |
| VELO/USDT | P8_26 | 212 | 0.9215 | 0.6700 | 0.9215 | -0.5626 | 0.6762 | rejected |
| VELO/USDT | P8_89 | 217 | 0.9146 | 0.7501 | 0.9051 | -0.7080 | 0.7433 | rejected |
| WIF/USDT | P34_50 | 61 | 1.0441 | 0.7375 | 1.0441 | 0.2148 | 0.7381 | exploratory signal |
| WIF/USDT | P34_55 | 86 | 0.9574 | 0.6823 | 0.9574 | -0.1637 | 0.6847 | rejected |
| WIF/USDT | P50_89 | 113 | 0.9253 | 0.6778 | 0.9253 | -0.3656 | 0.6728 | rejected |
| WIF/USDT | P55_144 | 93 | 0.9830 | 0.7667 | 0.9830 | -0.0373 | 0.7694 | rejected |
| WIF/USDT | P55_89 | 97 | 0.9250 | 0.6782 | 0.9250 | -0.3485 | 0.6777 | rejected |
| WIN/USDT | P12_144 | 130 | 0.9994 | 0.7918 | 0.9994 | 0.0580 | 0.7721 | rejected |
| WIN/USDT | P12_200 | 96 | 1.2759 | 1.0616 | 1.2655 | 1.1939 | 1.0384 | exploratory signal |
| WIN/USDT | P20_144 | 119 | 0.9694 | 0.7388 | 0.9660 | -0.1282 | 0.7197 | rejected |
| WIN/USDT | P20_200 | 100 | 0.9423 | 0.7692 | 0.9405 | -0.2528 | 0.7559 | rejected |
| WIN/USDT | P21_144 | 118 | 0.9143 | 0.6934 | 0.9120 | -0.4326 | 0.6732 | rejected |
| WIN/USDT | P21_200 | 104 | 0.9166 | 0.7321 | 0.9155 | -0.3944 | 0.7193 | rejected |
| WIN/USDT | P26_100 | 145 | 0.9433 | 0.6851 | 0.9433 | -0.2828 | 0.6703 | rejected |
| WIN/USDT | P26_144 | 124 | 0.9186 | 0.6811 | 0.9186 | -0.4108 | 0.6670 | rejected |
| WIN/USDT | P8_144 | 127 | 0.9805 | 0.7935 | 0.9805 | -0.0517 | 0.7826 | rejected |
| WIN/USDT | P8_200 | 104 | 1.2949 | 1.0848 | 1.3047 | 1.4054 | 1.0781 | exploratory signal |
| WLD/USDT | P100_144 | 61 | 0.9036 | 0.6941 | 0.9036 | -0.3802 | 0.6951 | rejected |
| WLD/USDT | P12_144 | 139 | 0.9567 | 0.8350 | 0.9567 | -0.2047 | 0.8298 | rejected |
| WLD/USDT | P12_200 | 100 | 1.0029 | 0.8998 | 0.9336 | -0.3113 | 0.8298 | rejected |
| WLD/USDT | P20_100 | 159 | 0.9807 | 0.8243 | 0.9807 | -0.0568 | 0.8164 | rejected |
| WLD/USDT | P20_144 | 129 | 1.1282 | 0.9817 | 1.1282 | 0.7608 | 0.9761 | exploratory signal |
| WLD/USDT | P20_200 | 94 | 1.3171 | 1.1761 | 1.2811 | 1.3078 | 1.1347 | credible candidate |
| WLD/USDT | P20_89 | 163 | 1.0482 | 0.8739 | 1.0482 | 0.3726 | 0.8662 | exploratory signal |
| WLD/USDT | P21_100 | 160 | 0.9111 | 0.7612 | 0.9111 | -0.5239 | 0.7526 | rejected |
| WLD/USDT | P21_144 | 128 | 1.1103 | 0.9648 | 1.1103 | 0.6695 | 0.9602 | exploratory signal |
| WLD/USDT | P21_200 | 103 | 1.2454 | 1.1119 | 1.2454 | 1.1847 | 1.1074 | exploratory signal |
| WLD/USDT | P21_89 | 162 | 0.9781 | 0.8108 | 0.9781 | -0.0742 | 0.8024 | rejected |
| WLD/USDT | P26_100 | 152 | 0.9050 | 0.7446 | 0.9050 | -0.5580 | 0.7370 | rejected |
| WLD/USDT | P26_144 | 119 | 1.1324 | 0.9670 | 1.1324 | 0.7604 | 0.9633 | exploratory signal |
| WLD/USDT | P26_200 | 96 | 0.9999 | 0.8906 | 0.9999 | 0.0520 | 0.8854 | rejected |
| WLD/USDT | P26_89 | 152 | 0.9506 | 0.7755 | 0.9506 | -0.2561 | 0.7707 | rejected |
| WLD/USDT | P34_100 | 140 | 0.9676 | 0.7932 | 0.9676 | -0.1424 | 0.7915 | rejected |
| WLD/USDT | P34_144 | 119 | 1.0161 | 0.8633 | 1.0161 | 0.1482 | 0.8595 | exploratory signal |
| WLD/USDT | P34_200 | 96 | 0.9160 | 0.8134 | 0.9160 | -0.3966 | 0.8115 | rejected |
| WLD/USDT | P34_50 | 80 | 0.9361 | 0.6757 | 0.9361 | -0.2568 | 0.6720 | rejected |
| WLD/USDT | P34_55 | 94 | 0.9236 | 0.6918 | 0.9236 | -0.3435 | 0.6859 | rejected |
| WLD/USDT | P34_89 | 140 | 1.0715 | 0.8649 | 1.0715 | 0.4950 | 0.8651 | exploratory signal |
| WLD/USDT | P50_144 | 108 | 0.9659 | 0.8104 | 0.9659 | -0.1377 | 0.8105 | rejected |
| WLD/USDT | P55_144 | 101 | 1.0247 | 0.8511 | 1.0247 | 0.1828 | 0.8492 | exploratory signal |
| WLD/USDT | P55_200 | 85 | 1.0174 | 0.8842 | 1.0174 | 0.1318 | 0.8815 | exploratory signal |
| WLD/USDT | P55_89 | 92 | 0.9895 | 0.7526 | 0.9895 | -0.0039 | 0.7582 | rejected |
| WLD/USDT | P8_100 | 191 | 0.9903 | 0.8457 | 0.9903 | 0.0090 | 0.8303 | rejected |
| WLD/USDT | P8_144 | 161 | 0.9857 | 0.8552 | 0.9535 | -0.2453 | 0.8194 | rejected |
| WLD/USDT | P8_20 | 162 | 0.9460 | 0.7020 | 0.9460 | -0.2905 | 0.6926 | rejected |
| WLD/USDT | P8_21 | 168 | 0.9664 | 0.7213 | 0.9664 | -0.1553 | 0.7115 | rejected |
| WLD/USDT | P8_26 | 205 | 0.9066 | 0.6924 | 0.9066 | -0.6020 | 0.6746 | rejected |
| WLD/USDT | P8_89 | 205 | 1.0642 | 0.9065 | 1.0642 | 0.5091 | 0.8924 | exploratory signal |
| W/USDT | P100_200 | 107 | 0.9770 | 0.7521 | 0.9538 | -0.1956 | 0.7272 | rejected |
| W/USDT | P12_100 | 162 | 0.9965 | 0.7994 | 0.9965 | 0.0447 | 0.7932 | rejected |
| W/USDT | P12_144 | 130 | 1.1529 | 0.9579 | 1.1529 | 0.9138 | 0.9558 | exploratory signal |
| W/USDT | P12_200 | 80 | 1.2138 | 1.0512 | 1.0902 | 0.4972 | 0.9214 | exploratory signal |
| W/USDT | P12_89 | 166 | 0.9344 | 0.7418 | 0.9344 | -0.3828 | 0.7371 | rejected |
| W/USDT | P26_144 | 139 | 0.9523 | 0.7661 | 0.9523 | -0.2455 | 0.7681 | rejected |
| W/USDT | P26_200 | 107 | 1.0719 | 0.8886 | 1.0719 | 0.4234 | 0.8831 | exploratory signal |
| W/USDT | P50_100 | 125 | 1.0266 | 0.7564 | 1.0266 | 0.2167 | 0.7626 | exploratory signal |
| W/USDT | P50_144 | 139 | 0.9184 | 0.7074 | 0.9184 | -0.4753 | 0.7102 | rejected |
| W/USDT | P50_200 | 125 | 0.9109 | 0.7325 | 0.9109 | -0.4986 | 0.7342 | rejected |
| W/USDT | P50_89 | 119 | 1.0257 | 0.7411 | 1.0257 | 0.2067 | 0.7477 | exploratory signal |
| W/USDT | P55_100 | 114 | 0.9632 | 0.7038 | 0.9632 | -0.1619 | 0.7123 | rejected |
| W/USDT | P55_89 | 107 | 0.9765 | 0.6928 | 0.9765 | -0.0798 | 0.7037 | rejected |
| W/USDT | P89_100 | 45 | 1.0562 | 0.7382 | 1.0562 | 0.2297 | 0.7423 | exploratory signal |
| W/USDT | P89_200 | 118 | 0.9803 | 0.7619 | 0.9803 | -0.0509 | 0.7530 | rejected |
| W/USDT | P8_100 | 169 | 0.9455 | 0.7704 | 0.9455 | -0.3195 | 0.7712 | rejected |
| W/USDT | P8_144 | 136 | 1.0413 | 0.8653 | 1.0413 | 0.3080 | 0.8617 | exploratory signal |
| W/USDT | P8_200 | 108 | 1.1233 | 0.9563 | 1.1240 | 0.6870 | 0.9456 | exploratory signal |
| W/USDT | P8_89 | 172 | 0.9422 | 0.7592 | 0.9422 | -0.3388 | 0.7568 | rejected |
| XAI/USDT | P12_200 | 94 | 0.9132 | 0.7642 | 0.9528 | -0.2002 | 0.7993 | rejected |
| XAI/USDT | P8_200 | 92 | 1.0164 | 0.8640 | 1.0185 | 0.1512 | 0.8643 | exploratory signal |
| XCH/USDT | P12_144 | 199 | 0.9485 | 0.8106 | 0.9485 | -0.3392 | 0.8164 | rejected |
| XCH/USDT | P12_200 | 161 | 0.9315 | 0.8006 | 0.9315 | -0.4355 | 0.8066 | rejected |
| XCH/USDT | P20_100 | 221 | 0.9329 | 0.7623 | 0.9329 | -0.4696 | 0.7634 | rejected |
| XCH/USDT | P20_144 | 208 | 0.9496 | 0.7930 | 0.9496 | -0.3186 | 0.7934 | rejected |
| XCH/USDT | P20_200 | 169 | 0.9311 | 0.7847 | 0.9311 | -0.4432 | 0.7894 | rejected |
| XCH/USDT | P20_89 | 227 | 0.9385 | 0.7605 | 0.9385 | -0.4261 | 0.7616 | rejected |
| XCH/USDT | P21_100 | 215 | 0.9201 | 0.7528 | 0.9201 | -0.5732 | 0.7541 | rejected |
| XCH/USDT | P21_144 | 201 | 0.9460 | 0.7915 | 0.9460 | -0.3416 | 0.7917 | rejected |
| XCH/USDT | P21_89 | 219 | 0.9097 | 0.7371 | 0.9097 | -0.6654 | 0.7386 | rejected |
| XCH/USDT | P26_144 | 185 | 0.9020 | 0.7599 | 0.9020 | -0.6783 | 0.7601 | rejected |
| XCH/USDT | P26_200 | 154 | 0.9338 | 0.7924 | 0.9338 | -0.3970 | 0.7954 | rejected |
| XCH/USDT | P34_200 | 138 | 0.9306 | 0.7985 | 0.9306 | -0.4124 | 0.8052 | rejected |
| XCH/USDT | P8_144 | 202 | 0.9023 | 0.7717 | 0.9023 | -0.7153 | 0.7746 | rejected |
| XDC/USDT | P20_100 | 176 | 0.9055 | 0.5989 | 0.9055 | -0.6593 | 0.6169 | rejected |
| XDC/USDT | P89_100 | 41 | 1.0205 | 0.5444 | 1.0205 | 0.1017 | 0.5605 | exploratory signal |
| XLM/USDT | P50_55 | 36 | 1.0332 | 0.6289 | 1.0332 | 0.1314 | 0.6274 | exploratory signal |
| XPR/USDT | P100_200 | 79 | 0.9934 | 0.7014 | 0.9934 | 0.0165 | 0.7028 | rejected |
| XPR/USDT | P12_200 | 86 | 0.9764 | 0.7709 | 0.9972 | 0.0356 | 0.7872 | rejected |
| XPR/USDT | P20_200 | 79 | 0.9271 | 0.7330 | 0.9469 | -0.2171 | 0.7520 | rejected |
| XPR/USDT | P20_26 | 41 | 1.0155 | 0.6534 | 1.0155 | 0.0856 | 0.6570 | exploratory signal |
| XPR/USDT | P21_200 | 77 | 0.9370 | 0.7462 | 0.9575 | -0.1600 | 0.7649 | rejected |
| XPR/USDT | P21_26 | 37 | 0.9693 | 0.6326 | 0.9693 | -0.0662 | 0.6346 | rejected |
| XPR/USDT | P55_200 | 91 | 0.9693 | 0.7353 | 0.9654 | -0.1288 | 0.7364 | rejected |
| XPR/USDT | P89_200 | 81 | 1.1031 | 0.7865 | 1.1031 | 0.5057 | 0.7878 | exploratory signal |
| XPR/USDT | P8_144 | 119 | 0.9032 | 0.6890 | 0.8866 | -0.6296 | 0.6766 | rejected |
| XPR/USDT | P8_200 | 44 | 1.5710 | 1.3538 | 1.5261 | 1.5084 | 1.3106 | exploratory signal |
| XRP/USDT | P20_21 | 41 | 0.9374 | 0.5549 | 0.9374 | -0.1820 | 0.5602 | rejected |
| XTZ/USDT | P12_144 | 84 | 0.9317 | 0.7462 | 0.9317 | -0.2977 | 0.7466 | rejected |
| XTZ/USDT | P55_200 | 100 | 0.9744 | 0.7268 | 0.9744 | -0.0901 | 0.7376 | rejected |
| XTZ/USDT | P8_144 | 66 | 0.9610 | 0.8059 | 0.9367 | -0.2651 | 0.7835 | rejected |
| XTZ/USDT | P8_200 | 55 | 0.9419 | 0.7951 | 0.8874 | -0.4608 | 0.7393 | rejected |
| YGG/USDT | P34_200 | 113 | 0.9556 | 0.7791 | 0.9556 | -0.2066 | 0.7834 | rejected |
| YGG/USDT | P55_200 | 94 | 0.9365 | 0.7466 | 0.9365 | -0.2691 | 0.7385 | rejected |
| ZBCN/USDT | P100_200 | 107 | 0.9215 | 0.7523 | 0.9215 | -0.3766 | 0.7452 | rejected |
| ZBCN/USDT | P50_89 | 79 | 1.0576 | 0.8155 | 1.0576 | 0.3107 | 0.8173 | exploratory signal |
| ZBCN/USDT | P55_89 | 63 | 1.0256 | 0.7861 | 1.0256 | 0.1477 | 0.7851 | exploratory signal |
| ZBCN/USDT | P8_12 | 48 | 1.0921 | 0.8520 | 1.0921 | 0.3624 | 0.8541 | exploratory signal |
| ZBCN/USDT | P8_20 | 124 | 0.9775 | 0.7664 | 0.9775 | -0.0757 | 0.7672 | rejected |
| ZBCN/USDT | P8_26 | 187 | 0.9067 | 0.7142 | 0.9067 | -0.6927 | 0.7262 | rejected |
| ZEC/USDT | P100_144 | 88 | 1.0086 | 0.7864 | 1.0086 | 0.0921 | 0.7885 | exploratory signal |
| ZEC/USDT | P100_200 | 86 | 0.9257 | 0.7661 | 0.9257 | -0.3203 | 0.7629 | rejected |
| ZEC/USDT | P12_100 | 137 | 1.1327 | 0.9739 | 1.0794 | 0.5203 | 0.9233 | exploratory signal |
| ZEC/USDT | P12_144 | 109 | 0.9269 | 0.8011 | 0.9273 | -0.3531 | 0.8001 | rejected |
| ZEC/USDT | P12_34 | 186 | 0.9159 | 0.7257 | 0.9159 | -0.5447 | 0.7222 | rejected |
| ZEC/USDT | P12_89 | 140 | 1.0674 | 0.9087 | 1.0186 | 0.1746 | 0.8626 | exploratory signal |
| ZEC/USDT | P144_200 | 61 | 0.9301 | 0.7345 | 0.9301 | -0.2500 | 0.7313 | rejected |
| ZEC/USDT | P20_100 | 133 | 0.9109 | 0.7759 | 0.8967 | -0.5886 | 0.7619 | rejected |
| ZEC/USDT | P20_144 | 118 | 1.0249 | 0.8750 | 0.9881 | -0.0085 | 0.8402 | rejected |
| ZEC/USDT | P21_100 | 125 | 0.9444 | 0.8038 | 0.9285 | -0.3650 | 0.7869 | rejected |
| ZEC/USDT | P21_144 | 113 | 1.0109 | 0.8600 | 0.9736 | -0.0901 | 0.8262 | rejected |
| ZEC/USDT | P21_89 | 132 | 0.9104 | 0.7632 | 0.8801 | -0.6747 | 0.7315 | rejected |
| ZEC/USDT | P26_100 | 122 | 0.9907 | 0.8386 | 0.9734 | -0.0917 | 0.8185 | rejected |
| ZEC/USDT | P26_144 | 107 | 0.9061 | 0.7686 | 0.8893 | -0.5796 | 0.7539 | rejected |
| ZEC/USDT | P26_89 | 126 | 0.9741 | 0.8149 | 0.9250 | -0.3804 | 0.7679 | rejected |
| ZEC/USDT | P8_100 | 134 | 1.0237 | 0.8824 | 0.9606 | -0.1738 | 0.8229 | rejected |
| ZEC/USDT | P8_12 | 61 | 1.2715 | 0.9755 | 1.2715 | 1.0003 | 0.9712 | exploratory signal |
| ZEC/USDT | P8_144 | 100 | 1.0421 | 0.9078 | 1.0190 | 0.1539 | 0.8890 | exploratory signal |
| ZEC/USDT | P8_200 | 76 | 1.0183 | 0.9140 | 0.9582 | -0.1566 | 0.8594 | rejected |
| ZEC/USDT | P8_50 | 200 | 0.9204 | 0.7726 | 0.8913 | -0.7938 | 0.7482 | rejected |
| ZEC/USDT | P8_55 | 184 | 0.9382 | 0.7964 | 0.9262 | -0.4909 | 0.7878 | rejected |
| ZEC/USDT | P8_89 | 146 | 1.0253 | 0.8727 | 0.9510 | -0.2384 | 0.8018 | rejected |
| ZEN/USDT | P12_200 | 37 | 1.2002 | 1.0623 | 1.3991 | 1.1387 | 1.2442 | exploratory signal |
| ZEN/USDT | P8_100 | 121 | 1.0897 | 0.9330 | 1.1065 | 0.6482 | 0.9476 | exploratory signal |
| ZEN/USDT | P8_144 | 102 | 0.9916 | 0.8366 | 0.9644 | -0.1392 | 0.8108 | rejected |
| ZEN/USDT | P8_200 | 33 | 1.4808 | 1.3582 | 1.6713 | 1.7541 | 1.4974 | credible candidate |
| ZIL/USDT | P144_200 | 68 | 0.9895 | 0.6469 | 0.9895 | 0.0006 | 0.6333 | rejected |
| ZIL/USDT | P20_200 | 120 | 0.9231 | 0.7583 | 0.9523 | -0.2370 | 0.7863 | rejected |
| ZIL/USDT | P21_200 | 119 | 0.9081 | 0.7464 | 0.9375 | -0.3287 | 0.7736 | rejected |
| ZIL/USDT | P26_200 | 121 | 0.9600 | 0.7795 | 0.9600 | -0.1860 | 0.7830 | rejected |
| ZK/USDT | P12_200 | 98 | 0.9580 | 0.8088 | 0.9704 | -0.1089 | 0.8149 | rejected |
| ZK/USDT | P20_200 | 101 | 1.0224 | 0.8621 | 1.0159 | 0.1434 | 0.8549 | exploratory signal |
| ZK/USDT | P21_200 | 96 | 1.0994 | 0.9260 | 1.0906 | 0.5255 | 0.9172 | exploratory signal |
| ZK/USDT | P26_200 | 117 | 0.9997 | 0.8160 | 0.9899 | -0.0016 | 0.8082 | rejected |
| ZK/USDT | P89_100 | 57 | 1.0889 | 0.7402 | 1.0889 | 0.3836 | 0.7373 | exploratory signal |
| ZRO/USDT | P100_200 | 87 | 1.1107 | 0.9204 | 1.1107 | 0.6044 | 0.9266 | exploratory signal |
| ZRO/USDT | P12_100 | 159 | 0.9427 | 0.8164 | 0.9427 | -0.3290 | 0.8120 | rejected |
| ZRO/USDT | P12_144 | 143 | 0.9817 | 0.8467 | 0.9825 | -0.0502 | 0.8480 | rejected |
| ZRO/USDT | P12_34 | 173 | 1.0378 | 0.8106 | 1.0378 | 0.3342 | 0.8043 | exploratory signal |
| ZRO/USDT | P12_50 | 203 | 1.1219 | 0.9092 | 1.1219 | 0.9349 | 0.8990 | exploratory signal |
| ZRO/USDT | P12_55 | 202 | 1.0857 | 0.8948 | 1.0857 | 0.6757 | 0.8806 | exploratory signal |
| ZRO/USDT | P12_89 | 178 | 1.0146 | 0.8612 | 1.0146 | 0.1805 | 0.8609 | exploratory signal |
| ZRO/USDT | P21_100 | 163 | 0.9090 | 0.7654 | 0.8990 | -0.6652 | 0.7550 | rejected |
| ZRO/USDT | P21_89 | 173 | 0.9011 | 0.7550 | 0.9132 | -0.5847 | 0.7652 | rejected |
| ZRO/USDT | P26_89 | 167 | 0.9184 | 0.7625 | 0.9312 | -0.4340 | 0.7733 | rejected |
| ZRO/USDT | P34_89 | 152 | 1.0612 | 0.8683 | 1.0612 | 0.4581 | 0.8623 | exploratory signal |
| ZRO/USDT | P50_55 | 38 | 1.2964 | 0.9794 | 1.2964 | 0.8785 | 0.9728 | exploratory signal |
| ZRO/USDT | P55_144 | 108 | 0.9266 | 0.7757 | 0.9116 | -0.4630 | 0.7628 | rejected |
| ZRO/USDT | P55_89 | 109 | 0.9437 | 0.7320 | 0.9437 | -0.2536 | 0.7201 | rejected |
| ZRO/USDT | P89_144 | 76 | 1.0309 | 0.8195 | 1.0309 | 0.1948 | 0.8204 | exploratory signal |
| ZRO/USDT | P89_200 | 89 | 1.1134 | 0.9308 | 1.1134 | 0.6172 | 0.9345 | exploratory signal |
| ZRO/USDT | P8_100 | 160 | 1.0855 | 0.9471 | 1.0449 | 0.3726 | 0.9021 | exploratory signal |
| ZRO/USDT | P8_144 | 130 | 1.0156 | 0.8915 | 1.0280 | 0.2338 | 0.8984 | exploratory signal |
| ZRO/USDT | P8_20 | 133 | 0.9685 | 0.7545 | 0.9685 | -0.1346 | 0.7497 | rejected |
| ZRO/USDT | P8_50 | 223 | 0.9275 | 0.7591 | 0.9275 | -0.5229 | 0.7542 | rejected |
| ZRO/USDT | P8_55 | 212 | 0.9403 | 0.7840 | 0.9403 | -0.3972 | 0.7778 | rejected |
| ZRO/USDT | P8_89 | 171 | 1.0676 | 0.9198 | 1.0153 | 0.1832 | 0.8654 | exploratory signal |

## Leg 3b — The closest survivors: cells that also survive the cost stress

These are the verified cells whose out-of-sample net PF is above 1 both at the registered costs and at 2x costs. The last three columns are the full-sample result, which is what a promotion would have to survive as well.

| Symbol | Cell | OOS trades | Exact OOS PF | Exact OOS Sharpe | Exact stress OOS PF | Full-sample net PF | Full-sample stress PF | Label |
|---|---|---|---|---|---|---|---|---|
| AERO/USDT | P12_200 | 79 | 1.1491 | 0.7642 | 1.0137 | 1.1454 | 1.0317 | credible candidate |
| APT/USDT | P12_144 | 86 | 1.1795 | 0.8658 | 1.0375 | 0.9400 | 0.8070 | exploratory signal |
| APT/USDT | P12_200 | 36 | 1.4641 | 1.2354 | 1.2962 | 1.0656 | 0.9139 | exploratory signal |
| APT/USDT | P20_144 | 90 | 1.2432 | 1.1762 | 1.0744 | 0.9912 | 0.8406 | exploratory signal |
| APT/USDT | P21_144 | 93 | 1.2517 | 1.2323 | 1.0800 | 1.0362 | 0.8804 | exploratory signal |
| APT/USDT | P26_200 | 80 | 1.2284 | 1.0173 | 1.0591 | 1.0097 | 0.8649 | exploratory signal |
| APT/USDT | P34_200 | 72 | 1.1590 | 0.7136 | 1.0124 | 1.0818 | 0.9233 | exploratory signal |
| AVA/USDT | P20_200 | 105 | 1.2326 | 1.2074 | 1.0142 | 0.8490 | 0.7083 | exploratory signal |
| AVA/USDT | P21_200 | 105 | 1.2324 | 1.2067 | 1.0139 | 0.8316 | 0.6937 | exploratory signal |
| AVA/USDT | P26_200 | 99 | 1.2616 | 1.2779 | 1.0338 | 0.8463 | 0.7039 | exploratory signal |
| AVA/USDT | P34_200 | 97 | 1.3090 | 1.4280 | 1.0465 | 0.8734 | 0.7152 | exploratory signal |
| AVA/USDT | P50_200 | 88 | 1.3796 | 1.6157 | 1.0947 | 0.9483 | 0.7721 | exploratory signal |
| BLUR/USDT | P12_144 | 103 | 1.3406 | 1.6906 | 1.1106 | 1.0281 | 0.8659 | exploratory signal |
| BLUR/USDT | P12_200 | 86 | 1.3084 | 1.4079 | 1.1201 | 1.0764 | 0.9105 | exploratory signal |
| BLUR/USDT | P21_200 | 90 | 1.1885 | 0.9218 | 1.0125 | 1.0199 | 0.8593 | exploratory signal |
| BLUR/USDT | P34_200 | 89 | 1.1690 | 0.8438 | 1.0017 | 1.0570 | 0.8972 | exploratory signal |
| BLUR/USDT | P8_144 | 112 | 1.2691 | 1.4448 | 1.0464 | 1.0347 | 0.8783 | exploratory signal |
| BLUR/USDT | P8_200 | 83 | 1.3389 | 1.4745 | 1.1488 | 1.1877 | 1.0230 | credible candidate |
| BOME/USDT | P26_200 | 112 | 1.2403 | 1.2337 | 1.0387 | 0.9895 | 0.8568 | exploratory signal |
| BRETT/USDT | P8_144 | 78 | 1.1688 | 0.8800 | 1.0004 | 0.8902 | 0.7915 | exploratory signal |
| BRETT/USDT | P8_200 | 42 | 1.6888 | 1.9493 | 1.5322 | 1.0449 | 0.9495 | exploratory signal |
| CETUS/USDT | P12_200 | 68 | 1.2746 | 1.1335 | 1.1338 | 1.2391 | 1.1033 | credible candidate |
| CETUS/USDT | P8_200 | 85 | 1.4174 | 1.7508 | 1.2401 | 1.2740 | 1.1315 | credible candidate |
| CHR/USDT | P34_200 | 97 | 1.1662 | 0.8772 | 1.0019 | 0.9367 | 0.7907 | exploratory signal |
| COTI/USDT | P50_144 | 115 | 1.2656 | 1.4546 | 1.0217 | 0.8727 | 0.7127 | exploratory signal |
| COTI/USDT | P50_200 | 99 | 1.3026 | 1.4852 | 1.0758 | 1.0597 | 0.8962 | exploratory signal |
| COTI/USDT | P55_144 | 112 | 1.2911 | 1.5520 | 1.0354 | 0.8966 | 0.7256 | exploratory signal |
| DAG/USDT | P8_100 | 109 | 1.3177 | 1.5113 | 1.0588 | 0.7768 | 0.6673 | exploratory signal |
| DEXE/USDT | P100_200 | 61 | 1.6140 | 1.8955 | 1.3617 | 0.8062 | 0.6470 | exploratory signal |
| DEXE/USDT | P12_100 | 112 | 1.1871 | 1.0012 | 1.0307 | 0.9157 | 0.7605 | exploratory signal |
| DEXE/USDT | P12_144 | 88 | 1.2833 | 1.3059 | 1.1198 | 0.9756 | 0.8190 | exploratory signal |
| DEXE/USDT | P12_200 | 65 | 1.3235 | 1.4204 | 1.1782 | 1.0165 | 0.8607 | exploratory signal |
| DEXE/USDT | P20_144 | 90 | 1.2489 | 1.1870 | 1.0920 | 0.9166 | 0.7706 | exploratory signal |
| DEXE/USDT | P20_200 | 66 | 1.3381 | 1.4680 | 1.1830 | 0.9864 | 0.8408 | exploratory signal |
| DEXE/USDT | P21_144 | 89 | 1.2278 | 1.0952 | 1.0745 | 0.9016 | 0.7595 | exploratory signal |
| DEXE/USDT | P21_200 | 64 | 1.3506 | 1.4994 | 1.1946 | 0.9970 | 0.8482 | exploratory signal |
| DEXE/USDT | P26_144 | 82 | 1.1393 | 0.7059 | 1.0002 | 0.9355 | 0.7800 | exploratory signal |
| DEXE/USDT | P26_200 | 63 | 1.2250 | 1.0428 | 1.0851 | 0.9471 | 0.8032 | exploratory signal |
| DEXE/USDT | P34_144 | 88 | 1.2222 | 1.0586 | 1.0649 | 0.9170 | 0.7513 | exploratory signal |
| DEXE/USDT | P34_200 | 73 | 1.1888 | 0.8662 | 1.0460 | 0.8662 | 0.7251 | exploratory signal |
| DEXE/USDT | P50_144 | 89 | 1.4465 | 1.8547 | 1.2581 | 0.8699 | 0.7085 | exploratory signal |
| DEXE/USDT | P50_200 | 70 | 1.8239 | 2.5632 | 1.6091 | 1.0694 | 0.8885 | exploratory signal |
| DEXE/USDT | P55_144 | 76 | 1.4671 | 1.8373 | 1.2660 | 0.8847 | 0.7059 | exploratory signal |
| DEXE/USDT | P55_200 | 63 | 1.9333 | 2.6319 | 1.7085 | 0.9677 | 0.7986 | exploratory signal |
| DEXE/USDT | P89_200 | 56 | 1.7448 | 2.1281 | 1.4799 | 0.8904 | 0.7210 | exploratory signal |
| DEXE/USDT | P8_100 | 114 | 1.2388 | 1.2518 | 1.0877 | 0.9076 | 0.7501 | exploratory signal |
| DEXE/USDT | P8_144 | 83 | 1.6286 | 2.4762 | 1.4581 | 0.9214 | 0.7767 | exploratory signal |
| DEXE/USDT | P8_200 | 56 | 1.2721 | 1.1854 | 1.1409 | 0.9059 | 0.7682 | exploratory signal |
| DIA/USDT | P12_200 | 84 | 1.5029 | 2.0308 | 1.2510 | 1.1315 | 0.9534 | exploratory signal |
| DIA/USDT | P20_200 | 122 | 1.3064 | 1.5725 | 1.0449 | 0.9440 | 0.7763 | exploratory signal |
| DIA/USDT | P21_200 | 120 | 1.3177 | 1.6016 | 1.0516 | 0.9699 | 0.7985 | exploratory signal |
| DIA/USDT | P26_200 | 114 | 1.2789 | 1.3786 | 1.0211 | 0.9740 | 0.7945 | exploratory signal |
| DIA/USDT | P8_200 | 89 | 1.2941 | 1.3743 | 1.0808 | 1.0236 | 0.8644 | exploratory signal |
| EGLD/USDT | P55_200 | 99 | 1.3233 | 1.4725 | 1.0202 | 0.8953 | 0.7049 | exploratory signal |
| ENA/USDT | P20_200 | 106 | 1.2024 | 1.0480 | 1.0475 | 0.9190 | 0.8215 | exploratory signal |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.1879 | 1.0324 | 1.3253 | 1.0289 | credible candidate |
| ENA/USDT | P21_200 | 101 | 1.1506 | 0.7956 | 1.0043 | 0.8941 | 0.7989 | exploratory signal |
| ENA/USDT | P34_144 | 111 | 1.2519 | 1.3176 | 1.0600 | 0.9014 | 0.7862 | exploratory signal |
| ENA/USDT | P8_144 | 123 | 1.2020 | 1.1170 | 1.0433 | 1.0576 | 0.9441 | exploratory signal |
| FET/USDT | P12_200 | 36 | 1.5616 | 1.3738 | 1.4404 | 1.0341 | 0.9161 | exploratory signal |
| FET/USDT | P20_200 | 34 | 1.2336 | 0.6599 | 1.1306 | 1.0236 | 0.9042 | exploratory signal |
| FET/USDT | P21_200 | 39 | 1.1274 | 0.4174 | 1.0368 | 1.0077 | 0.8895 | exploratory signal |
| FET/USDT | P8_200 | 45 | 1.2115 | 0.7046 | 1.1183 | 1.0215 | 0.9132 | exploratory signal |
| FLUX/USDT | P8_200 | 93 | 1.2427 | 1.2438 | 1.0272 | 1.2228 | 1.0591 | credible candidate |
| GMT/USDT | P8_200 | 88 | 1.4743 | 1.9895 | 1.2697 | 0.9866 | 0.8399 | exploratory signal |
| GRT/USDT | P20_200 | 57 | 1.3953 | 1.4236 | 1.2070 | 1.1087 | 0.9679 | exploratory signal |
| GRT/USDT | P8_200 | 57 | 1.2529 | 0.9465 | 1.0880 | 0.9520 | 0.8433 | exploratory signal |
| IMX/USDT | P12_200 | 94 | 1.4025 | 1.8017 | 1.1843 | 0.9999 | 0.8682 | exploratory signal |
| IMX/USDT | P20_200 | 122 | 1.3382 | 1.7558 | 1.1116 | 1.1008 | 0.9382 | exploratory signal |
| IMX/USDT | P21_200 | 111 | 1.2771 | 1.4252 | 1.0591 | 1.0431 | 0.8926 | exploratory signal |
| IMX/USDT | P26_200 | 114 | 1.4801 | 2.2564 | 1.2246 | 1.1185 | 0.9501 | exploratory signal |
| IMX/USDT | P34_200 | 101 | 1.3871 | 1.8507 | 1.1430 | 1.1547 | 0.9774 | exploratory signal |
| IMX/USDT | P50_200 | 102 | 1.2397 | 1.2209 | 1.0091 | 1.0175 | 0.8471 | exploratory signal |
| IMX/USDT | P50_55 | 44 | 1.4581 | 1.3460 | 1.0113 | 1.2990 | 0.9259 | exploratory signal |
| IMX/USDT | P8_200 | 93 | 1.2911 | 1.3772 | 1.0899 | 1.2102 | 1.0487 | credible candidate |
| JASMY/USDT | P144_200 | 56 | 1.4928 | 1.5876 | 1.0619 | 1.0245 | 0.7809 | exploratory signal |
| MINA/USDT | P12_200 | 75 | 1.3342 | 1.2988 | 1.1513 | 0.9442 | 0.8021 | exploratory signal |
| PENDLE/USDT | P34_144 | 98 | 1.3020 | 1.4488 | 1.0713 | 0.8413 | 0.7069 | exploratory signal |
| POL/USDT | P20_144 | 73 | 1.2058 | 0.9025 | 1.0009 | 0.9890 | 0.8035 | exploratory signal |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.3904 | 1.1649 | 1.0429 | 0.8651 | exploratory signal |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.6027 | 1.2175 | 1.0354 | 0.8696 | exploratory signal |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.5210 | 1.1701 | 0.9932 | 0.8286 | exploratory signal |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.7600 | 1.1220 | 1.0278 | 0.8389 | exploratory signal |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.8688 | 1.3924 | 1.1216 | 0.9604 | exploratory signal |
| PUFFER/USDT | P20_200 | 81 | 1.4038 | 1.8699 | 1.2514 | 1.1884 | 1.0506 | credible candidate |
| PUFFER/USDT | P21_200 | 75 | 1.3789 | 1.7012 | 1.2253 | 1.1333 | 0.9964 | exploratory signal |
| PUFFER/USDT | P26_200 | 75 | 1.2674 | 1.2929 | 1.1275 | 1.0037 | 0.8831 | exploratory signal |
| PYTH/USDT | P8_200 | 82 | 1.1983 | 0.8804 | 1.0603 | 1.0817 | 0.9666 | exploratory signal |
| RENDER/USDT | P20_200 | 77 | 1.1739 | 0.8885 | 1.0086 | 1.0390 | 0.8988 | exploratory signal |
| RENDER/USDT | P8_200 | 45 | 1.1898 | 0.7068 | 1.0727 | 0.9713 | 0.8674 | exploratory signal |
| ROSE/USDT | P12_200 | 55 | 1.3298 | 1.2553 | 1.1638 | 0.9313 | 0.8163 | exploratory signal |
| ROSE/USDT | P34_200 | 88 | 1.3328 | 1.5329 | 1.1197 | 1.0394 | 0.8882 | exploratory signal |
| ROSE/USDT | P55_200 | 112 | 1.3264 | 1.6361 | 1.0699 | 1.0227 | 0.8555 | exploratory signal |
| RUNE/USDT | P50_144 | 120 | 1.5230 | 2.4239 | 1.1018 | 0.9328 | 0.7286 | exploratory signal |
| RUNE/USDT | P50_200 | 89 | 1.3239 | 1.4254 | 1.0085 | 1.0682 | 0.8698 | exploratory signal |
| SYN/USDT | P20_200 | 99 | 1.2314 | 1.1317 | 1.0362 | 0.9918 | 0.8525 | exploratory signal |
| SYN/USDT | P26_200 | 91 | 1.1537 | 0.7813 | 1.0030 | 0.9780 | 0.8471 | exploratory signal |
| TWT/USDT | P8_200 | 73 | 1.2604 | 1.0492 | 1.0098 | 0.8890 | 0.7168 | exploratory signal |
| T/USDT | P12_200 | 52 | 1.3272 | 1.0564 | 1.0559 | 0.9175 | 0.7291 | exploratory signal |
| VELO/USDT | P12_200 | 114 | 1.2464 | 1.2649 | 1.0736 | 0.9932 | 0.8813 | exploratory signal |
| VELO/USDT | P20_200 | 107 | 1.2073 | 1.0530 | 1.0416 | 0.9855 | 0.8674 | exploratory signal |
| WIN/USDT | P12_200 | 96 | 1.2655 | 1.1939 | 1.0384 | 0.8747 | 0.7033 | exploratory signal |
| WIN/USDT | P8_200 | 104 | 1.3047 | 1.4054 | 1.0781 | 1.0109 | 0.8218 | exploratory signal |
| WLD/USDT | P20_200 | 94 | 1.2811 | 1.3078 | 1.1347 | 1.1725 | 1.0544 | credible candidate |
| WLD/USDT | P21_200 | 103 | 1.2454 | 1.1847 | 1.1074 | 1.0863 | 0.9732 | exploratory signal |
| XPR/USDT | P8_200 | 44 | 1.5261 | 1.5084 | 1.3106 | 0.9178 | 0.7837 | exploratory signal |
| ZEN/USDT | P12_200 | 37 | 1.3991 | 1.1387 | 1.2442 | 1.0183 | 0.8795 | exploratory signal |
| ZEN/USDT | P8_200 | 33 | 1.6713 | 1.7541 | 1.4974 | 1.2569 | 1.1295 | credible candidate |

## Leg 3c — Why the exploratory signals did not promote

| Blocking gate | Cells |
|---|---|
| out-of-sample net PF still > 1 under 2x costs | 489 |
| full-sample net PF still > 1 under 2x costs | 580 |
| out-of-sample Sharpe > 0 | 0 |

## Leg 3d — Does the verdict depend on the out-of-sample window?

The closest survivors were re-verified at every window length. A cell that only looks good at one window length is an artifact of that choice.

| Symbol | Cell | OOS 20% PF / stress PF | OOS 35% PF / stress PF | OOS 50% PF / stress PF |
|---|---|---|---|---|
| AERO/USDT | P12_200 | 0.9885 / 0.8651 | 1.1491 / 1.0137 | 1.0609 / 0.9501 |
| APT/USDT | P12_144 | 1.4025 / 1.1789 | 1.1795 / 1.0375 | 1.0063 / 0.8606 |
| APT/USDT | P12_200 | 1.4887 / 1.2292 | 1.4641 / 1.2962 | 1.0507 / 0.9049 |
| APT/USDT | P20_144 | 1.3283 / 1.1143 | 1.2432 / 1.0744 | 1.0926 / 0.9172 |
| APT/USDT | P21_144 | 1.3262 / 1.1114 | 1.2517 / 1.0800 | 1.1400 / 0.9619 |
| APT/USDT | P26_200 | 1.3231 / 1.1007 | 1.2284 / 1.0591 | 1.0484 / 0.8893 |
| APT/USDT | P34_200 | 1.3160 / 1.0898 | 1.1590 / 1.0124 | 1.0950 / 0.9366 |
| AVA/USDT | P20_200 | 0.9722 / 0.8464 | 1.2326 / 1.0142 | 1.0428 / 0.8518 |
| AVA/USDT | P21_200 | 0.9719 / 0.8458 | 1.2324 / 1.0139 | 1.0660 / 0.8721 |
| AVA/USDT | P26_200 | 1.1201 / 0.9702 | 1.2616 / 1.0338 | 1.0784 / 0.8763 |
| AVA/USDT | P34_200 | 1.2066 / 1.0171 | 1.3090 / 1.0465 | 1.1004 / 0.8802 |
| AVA/USDT | P50_200 | 1.4690 / 1.2293 | 1.3796 / 1.0947 | 1.1542 / 0.9191 |
| BLUR/USDT | P12_144 | 1.2764 / 1.0375 | 1.3406 / 1.1106 | 1.0083 / 0.8147 |
| BLUR/USDT | P12_200 | 1.2160 / 1.0174 | 1.3084 / 1.1201 | 1.1416 / 0.9457 |
| BLUR/USDT | P21_200 | 1.0893 / 0.9178 | 1.1885 / 1.0125 | 1.0598 / 0.8727 |
| BLUR/USDT | P34_200 | 0.9275 / 0.7807 | 1.1690 / 1.0017 | 1.1762 / 0.9880 |
| BLUR/USDT | P8_144 | 1.2038 / 0.9817 | 1.2691 / 1.0464 | 1.0433 / 0.8547 |
| BLUR/USDT | P8_200 | 1.3212 / 1.1147 | 1.3389 / 1.1488 | 1.2613 / 1.0849 |
| BOME/USDT | P26_200 | 1.2228 / 1.0143 | 1.2403 / 1.0387 | 1.2579 / 1.0659 |
| BRETT/USDT | P8_144 | 1.1722 / 1.0061 | 1.1688 / 1.0004 | 1.0560 / 0.9214 |
| BRETT/USDT | P8_200 | 1.5857 / 1.4148 | 1.6888 / 1.5322 | 1.2354 / 1.1185 |
| CETUS/USDT | P12_200 | 1.0107 / 0.8909 | 1.2746 / 1.1338 | 1.1118 / 0.9812 |
| CETUS/USDT | P8_200 | 1.3014 / 1.1343 | 1.4174 / 1.2401 | 1.3585 / 1.1894 |
| CHR/USDT | P34_200 | 1.0528 / 0.9305 | 1.1662 / 1.0019 | 0.9039 / 0.7547 |
| COTI/USDT | P50_144 | 1.1056 / 0.9033 | 1.2656 / 1.0217 | 1.1659 / 0.9293 |
| COTI/USDT | P50_200 | 1.0187 / 0.8432 | 1.3026 / 1.0758 | 1.2881 / 1.0670 |
| COTI/USDT | P55_144 | 1.0722 / 0.8663 | 1.2911 / 1.0354 | 1.1690 / 0.9235 |
| DAG/USDT | P8_100 | 1.6037 / 1.3263 | 1.3177 / 1.0588 | 0.9778 / 0.8056 |
| DEXE/USDT | P100_200 | 1.8662 / 1.6677 | 1.6140 / 1.3617 | 1.1435 / 0.9129 |
| DEXE/USDT | P12_100 | 0.9818 / 0.9000 | 1.1871 / 1.0307 | 0.9971 / 0.8130 |
| DEXE/USDT | P12_144 | 1.4129 / 1.2961 | 1.2833 / 1.1198 | 1.1287 / 0.9344 |
| DEXE/USDT | P12_200 | 1.1245 / 1.0255 | 1.3235 / 1.1782 | 1.3809 / 1.1540 |
| DEXE/USDT | P20_144 | 1.2817 / 1.1723 | 1.2489 / 1.0920 | 1.0647 / 0.8881 |
| DEXE/USDT | P20_200 | 1.3915 / 1.2683 | 1.3381 / 1.1830 | 1.5091 / 1.2913 |
| DEXE/USDT | P21_144 | 1.2828 / 1.1741 | 1.2278 / 1.0745 | 1.0224 / 0.8558 |
| DEXE/USDT | P21_200 | 1.3913 / 1.2679 | 1.3506 / 1.1946 | 1.5040 / 1.2870 |
| DEXE/USDT | P26_144 | 1.0633 / 0.9659 | 1.1393 / 1.0002 | 0.9984 / 0.8420 |
| DEXE/USDT | P26_200 | 0.9922 / 0.8948 | 1.2250 / 1.0851 | 1.2634 / 1.0802 |
| DEXE/USDT | P34_144 | 0.9045 / 0.8122 | 1.2222 / 1.0649 | 1.0525 / 0.8688 |
| DEXE/USDT | P34_200 | 0.9684 / 0.8844 | 1.1888 / 1.0460 | 1.1682 / 0.9792 |
| DEXE/USDT | P50_144 | 1.2055 / 1.0648 | 1.4465 / 1.2581 | 1.1259 / 0.9329 |
| DEXE/USDT | P50_200 | 1.7249 / 1.5516 | 1.8239 / 1.6091 | 1.5032 / 1.2616 |
| DEXE/USDT | P55_144 | 1.1736 / 1.0371 | 1.4671 / 1.2660 | 1.1938 / 0.9510 |
| DEXE/USDT | P55_200 | 2.0835 / 1.9031 | 1.9333 / 1.7085 | 1.5723 / 1.3263 |
| DEXE/USDT | P89_200 | 1.7758 / 1.6233 | 1.7448 / 1.4799 | 1.2664 / 1.0176 |
| DEXE/USDT | P8_100 | 1.2223 / 1.1237 | 1.2388 / 1.0877 | 0.9821 / 0.8018 |
| DEXE/USDT | P8_144 | 1.3602 / 1.2663 | 1.6286 / 1.4581 | 1.1530 / 0.9637 |
| DEXE/USDT | P8_200 | 1.1502 / 1.0704 | 1.2721 / 1.1409 | 1.2100 / 0.9979 |
| DIA/USDT | P12_200 | 1.6330 / 1.3731 | 1.5029 / 1.2510 | 1.5013 / 1.2691 |
| DIA/USDT | P20_200 | 1.9955 / 1.6365 | 1.3064 / 1.0449 | 1.2043 / 0.9736 |
| DIA/USDT | P21_200 | 2.0329 / 1.6635 | 1.3177 / 1.0516 | 1.2327 / 0.9955 |
| DIA/USDT | P26_200 | 2.1903 / 1.8058 | 1.2789 / 1.0211 | 1.2825 / 1.0352 |
| DIA/USDT | P8_200 | 1.3533 / 1.1377 | 1.2941 / 1.0808 | 1.2390 / 1.0472 |
| EGLD/USDT | P55_200 | 1.5506 / 1.2200 | 1.3233 / 1.0202 | 1.1107 / 0.8590 |
| ENA/USDT | P20_200 | 1.1742 / 1.0049 | 1.2024 / 1.0475 | 1.0171 / 0.8891 |
| ENA/USDT | P20_21 | 1.4238 / 1.0529 | 1.3902 / 1.0324 | 1.5055 / 1.1359 |
| ENA/USDT | P21_200 | 1.0731 / 0.9135 | 1.1506 / 1.0043 | 0.9924 / 0.8694 |
| ENA/USDT | P34_144 | 1.1313 / 0.9452 | 1.2519 / 1.0600 | 1.1404 / 0.9701 |
| ENA/USDT | P8_144 | 1.0318 / 0.8860 | 1.2020 / 1.0433 | 1.1452 / 1.0022 |
| FET/USDT | P12_200 | 1.4800 / 1.3441 | 1.5616 / 1.4404 | 1.3907 / 1.2499 |
| FET/USDT | P20_200 | 1.2493 / 1.1382 | 1.2336 / 1.1306 | 1.3515 / 1.1961 |
| FET/USDT | P21_200 | 1.3534 / 1.2337 | 1.1274 / 1.0368 | 1.3613 / 1.2103 |
| FET/USDT | P8_200 | 1.3388 / 1.2324 | 1.2115 / 1.1183 | 1.1842 / 1.0667 |
| FLUX/USDT | P8_200 | 1.9026 / 1.6374 | 1.2427 / 1.0272 | 1.1846 / 1.0013 |
| GMT/USDT | P8_200 | 1.0768 / 0.9140 | 1.4743 / 1.2697 | 1.1887 / 0.9993 |
| GRT/USDT | P20_200 | 1.2513 / 1.0435 | 1.3953 / 1.2070 | 1.1981 / 1.0263 |
| GRT/USDT | P8_200 | 0.9770 / 0.8147 | 1.2529 / 1.0880 | 1.0564 / 0.9188 |
| IMX/USDT | P12_200 | 1.4783 / 1.2163 | 1.4025 / 1.1843 | 1.2024 / 1.0210 |
| IMX/USDT | P20_200 | 1.3114 / 1.0660 | 1.3382 / 1.1116 | 1.2332 / 1.0291 |
| IMX/USDT | P21_200 | 1.2901 / 1.0457 | 1.2771 / 1.0591 | 1.1494 / 0.9607 |
| IMX/USDT | P26_200 | 1.3068 / 1.0439 | 1.4801 / 1.2246 | 1.3019 / 1.0879 |
| IMX/USDT | P34_200 | 1.2938 / 1.0318 | 1.3871 / 1.1430 | 1.2097 / 1.0073 |
| IMX/USDT | P50_200 | 1.1890 / 0.9455 | 1.2397 / 1.0091 | 1.0919 / 0.8936 |
| IMX/USDT | P50_55 | 0.7177 / 0.4594 | 1.4581 / 1.0113 | 1.6521 / 1.1875 |
| IMX/USDT | P8_200 | 1.3886 / 1.1443 | 1.2911 / 1.0899 | 1.3184 / 1.1300 |
| JASMY/USDT | P144_200 | 1.1520 / 0.8349 | 1.4928 / 1.0619 | 1.2866 / 0.9289 |
| MINA/USDT | P12_200 | 1.6691 / 1.4458 | 1.3342 / 1.1513 | 0.8882 / 0.7392 |
| PENDLE/USDT | P34_144 | 0.9883 / 0.7877 | 1.3020 / 1.0713 | 1.1006 / 0.9001 |
| POL/USDT | P20_144 | 0.8915 / 0.7141 | 1.2058 / 1.0009 | 1.0309 / 0.8552 |
| POL/USDT | P20_200 | 1.1598 / 0.9799 | 1.3597 / 1.1649 | 1.2471 / 1.0631 |
| POL/USDT | P21_200 | 1.2883 / 1.0852 | 1.4246 / 1.2175 | 1.2338 / 1.0422 |
| POL/USDT | P26_200 | 1.0844 / 0.9066 | 1.3900 / 1.1701 | 1.0721 / 0.8920 |
| POL/USDT | P34_200 | 1.2127 / 0.9489 | 1.3951 / 1.1220 | 1.0744 / 0.8470 |
| POL/USDT | P8_200 | 0.8469 / 0.7028 | 1.6086 / 1.3924 | 1.1234 / 0.9519 |
| PUFFER/USDT | P20_200 | 1.2249 / 1.1155 | 1.4038 / 1.2514 | 1.4214 / 1.2723 |
| PUFFER/USDT | P21_200 | 1.2603 / 1.1470 | 1.3789 / 1.2253 | 1.3067 / 1.1541 |
| PUFFER/USDT | P26_200 | 1.0173 / 0.9208 | 1.2674 / 1.1275 | 1.2201 / 1.0799 |
| PYTH/USDT | P8_200 | 1.7690 / 1.5954 | 1.1983 / 1.0603 | 1.0345 / 0.9149 |
| RENDER/USDT | P20_200 | 0.9680 / 0.8403 | 1.1739 / 1.0086 | 1.1635 / 1.0105 |
| RENDER/USDT | P8_200 | 0.9518 / 0.8440 | 1.1898 / 1.0727 | 1.3248 / 1.1946 |
| ROSE/USDT | P12_200 | 0.8928 / 0.7479 | 1.3298 / 1.1638 | 0.8512 / 0.7492 |
| ROSE/USDT | P34_200 | 1.0123 / 0.8248 | 1.3328 / 1.1197 | 1.2002 / 1.0180 |
| ROSE/USDT | P55_200 | 1.3066 / 1.0179 | 1.3264 / 1.0699 | 1.1950 / 0.9776 |
| RUNE/USDT | P50_144 | 1.4362 / 1.0530 | 1.5230 / 1.1018 | 1.2827 / 0.9269 |
| RUNE/USDT | P50_200 | 1.3541 / 1.0299 | 1.3239 / 1.0085 | 1.2968 / 1.0120 |
| SYN/USDT | P20_200 | 1.4122 / 1.1998 | 1.2314 / 1.0362 | 0.9575 / 0.7946 |
| SYN/USDT | P26_200 | 1.1181 / 0.9490 | 1.1537 / 1.0030 | 0.9656 / 0.8158 |
| TWT/USDT | P8_200 | 1.3218 / 1.0752 | 1.2604 / 1.0098 | 1.0641 / 0.8334 |
| T/USDT | P12_200 | 1.5942 / 1.3770 | 1.3272 / 1.0559 | 0.7754 / 0.5778 |
| VELO/USDT | P12_200 | 1.2611 / 1.0920 | 1.2464 / 1.0736 | 1.1749 / 1.0201 |
| VELO/USDT | P20_200 | 1.3372 / 1.1556 | 1.2073 / 1.0416 | 1.0636 / 0.9191 |
| WIN/USDT | P12_200 | 1.9330 / 1.6034 | 1.2655 / 1.0384 | 1.0517 / 0.8379 |
| WIN/USDT | P8_200 | 1.6909 / 1.4075 | 1.3047 / 1.0781 | 1.0841 / 0.8726 |
| WLD/USDT | P20_200 | 1.7616 / 1.5989 | 1.2811 / 1.1347 | 1.2516 / 1.1022 |
| WLD/USDT | P21_200 | 1.6085 / 1.4621 | 1.2454 / 1.1074 | 1.1216 / 0.9841 |
| XPR/USDT | P8_200 | 1.4808 / 1.2439 | 1.5261 / 1.3106 | 1.2379 / 1.0497 |
| ZEN/USDT | P12_200 | 0.9404 / 0.7905 | 1.3991 / 1.2442 | 1.0349 / 0.8920 |
| ZEN/USDT | P8_200 | 1.1896 / 1.0147 | 1.6713 / 1.4974 | 1.1247 / 0.9986 |

| Symbol | Cell | OOS 20% trades | OOS 35% trades | OOS 50% trades |
|---|---|---|---|---|
| AERO/USDT | P12_200 | 67 | 89 | 117 |
| APT/USDT | P12_144 | 57 | 90 | 138 |
| APT/USDT | P12_200 | 40 | 38 | 83 |
| APT/USDT | P20_144 | 50 | 94 | 148 |
| APT/USDT | P21_144 | 50 | 97 | 149 |
| APT/USDT | P26_200 | 50 | 81 | 126 |
| APT/USDT | P34_200 | 50 | 73 | 124 |
| AVA/USDT | P20_200 | 44 | 105 | 163 |
| AVA/USDT | P21_200 | 44 | 105 | 165 |
| AVA/USDT | P26_200 | 41 | 99 | 162 |
| AVA/USDT | P34_200 | 41 | 97 | 158 |
| AVA/USDT | P50_200 | 42 | 88 | 139 |
| BLUR/USDT | P12_144 | 75 | 116 | 144 |
| BLUR/USDT | P12_200 | 60 | 90 | 120 |
| BLUR/USDT | P21_200 | 56 | 90 | 120 |
| BLUR/USDT | P34_200 | 64 | 89 | 136 |
| BLUR/USDT | P8_144 | 85 | 123 | 146 |
| BLUR/USDT | P8_200 | 65 | 88 | 97 |
| BOME/USDT | P26_200 | 67 | 112 | 152 |
| BRETT/USDT | P8_144 | 66 | 92 | 119 |
| BRETT/USDT | P8_200 | 38 | 45 | 77 |
| CETUS/USDT | P12_200 | 36 | 68 | 108 |
| CETUS/USDT | P8_200 | 37 | 86 | 119 |
| CHR/USDT | P34_200 | 48 | 97 | 160 |
| COTI/USDT | P50_144 | 71 | 115 | 173 |
| COTI/USDT | P50_200 | 60 | 99 | 144 |
| COTI/USDT | P55_144 | 68 | 112 | 167 |
| DAG/USDT | P8_100 | 67 | 109 | 197 |
| DEXE/USDT | P100_200 | 25 | 61 | 92 |
| DEXE/USDT | P12_100 | 40 | 112 | 195 |
| DEXE/USDT | P12_144 | 39 | 97 | 130 |
| DEXE/USDT | P12_200 | 39 | 86 | 110 |
| DEXE/USDT | P20_144 | 37 | 98 | 130 |
| DEXE/USDT | P20_200 | 39 | 89 | 103 |
| DEXE/USDT | P21_144 | 37 | 97 | 127 |
| DEXE/USDT | P21_200 | 39 | 87 | 100 |
| DEXE/USDT | P26_144 | 38 | 91 | 119 |
| DEXE/USDT | P26_200 | 41 | 85 | 93 |
| DEXE/USDT | P34_144 | 39 | 88 | 137 |
| DEXE/USDT | P34_200 | 36 | 79 | 104 |
| DEXE/USDT | P50_144 | 41 | 89 | 118 |
| DEXE/USDT | P50_200 | 30 | 71 | 100 |
| DEXE/USDT | P55_144 | 38 | 82 | 112 |
| DEXE/USDT | P55_200 | 27 | 64 | 91 |
| DEXE/USDT | P89_200 | 24 | 58 | 87 |
| DEXE/USDT | P8_100 | 43 | 119 | 202 |
| DEXE/USDT | P8_144 | 38 | 92 | 126 |
| DEXE/USDT | P8_200 | 37 | 79 | 102 |
| DIA/USDT | P12_200 | 65 | 90 | 103 |
| DIA/USDT | P20_200 | 62 | 128 | 148 |
| DIA/USDT | P21_200 | 63 | 126 | 145 |
| DIA/USDT | P26_200 | 59 | 116 | 144 |
| DIA/USDT | P8_200 | 71 | 95 | 109 |
| EGLD/USDT | P55_200 | 55 | 99 | 144 |
| ENA/USDT | P20_200 | 65 | 106 | 146 |
| ENA/USDT | P20_21 | 29 | 46 | 63 |
| ENA/USDT | P21_200 | 62 | 101 | 142 |
| ENA/USDT | P34_144 | 72 | 111 | 165 |
| ENA/USDT | P8_144 | 76 | 123 | 172 |
| FET/USDT | P12_200 | 30 | 36 | 70 |
| FET/USDT | P20_200 | 32 | 34 | 80 |
| FET/USDT | P21_200 | 31 | 39 | 88 |
| FET/USDT | P8_200 | 33 | 45 | 80 |
| FLUX/USDT | P8_200 | 59 | 125 | 132 |
| GMT/USDT | P8_200 | 53 | 91 | 128 |
| GRT/USDT | P20_200 | 51 | 64 | 97 |
| GRT/USDT | P8_200 | 51 | 62 | 85 |
| IMX/USDT | P12_200 | 66 | 100 | 141 |
| IMX/USDT | P20_200 | 72 | 129 | 169 |
| IMX/USDT | P21_200 | 74 | 118 | 160 |
| IMX/USDT | P26_200 | 70 | 114 | 172 |
| IMX/USDT | P34_200 | 62 | 107 | 158 |
| IMX/USDT | P50_200 | 63 | 102 | 159 |
| IMX/USDT | P50_55 | 25 | 44 | 67 |
| IMX/USDT | P8_200 | 66 | 100 | 136 |
| JASMY/USDT | P144_200 | 31 | 56 | 72 |
| MINA/USDT | P12_200 | 53 | 74 | 137 |
| PENDLE/USDT | P34_144 | 80 | 98 | 154 |
| POL/USDT | P20_144 | 35 | 73 | 109 |
| POL/USDT | P20_200 | 32 | 69 | 95 |
| POL/USDT | P21_200 | 34 | 71 | 102 |
| POL/USDT | P26_200 | 31 | 71 | 102 |
| POL/USDT | P34_200 | 52 | 95 | 140 |
| POL/USDT | P8_200 | 18 | 52 | 95 |
| PUFFER/USDT | P20_200 | 46 | 82 | 111 |
| PUFFER/USDT | P21_200 | 42 | 76 | 111 |
| PUFFER/USDT | P26_200 | 44 | 75 | 114 |
| PYTH/USDT | P8_200 | 51 | 85 | 109 |
| RENDER/USDT | P20_200 | 37 | 82 | 107 |
| RENDER/USDT | P8_200 | 36 | 45 | 68 |
| ROSE/USDT | P12_200 | 30 | 60 | 90 |
| ROSE/USDT | P34_200 | 46 | 88 | 125 |
| ROSE/USDT | P55_200 | 73 | 112 | 150 |
| RUNE/USDT | P50_144 | 76 | 120 | 171 |
| RUNE/USDT | P50_200 | 63 | 89 | 124 |
| SYN/USDT | P20_200 | 66 | 100 | 169 |
| SYN/USDT | P26_200 | 65 | 91 | 152 |
| TWT/USDT | P8_200 | 38 | 73 | 109 |
| T/USDT | P12_200 | 30 | 52 | 110 |
| VELO/USDT | P12_200 | 66 | 115 | 160 |
| VELO/USDT | P20_200 | 66 | 108 | 163 |
| WIN/USDT | P12_200 | 63 | 98 | 138 |
| WIN/USDT | P8_200 | 69 | 107 | 137 |
| WLD/USDT | P20_200 | 56 | 100 | 128 |
| WLD/USDT | P21_200 | 61 | 103 | 141 |
| XPR/USDT | P8_200 | 29 | 46 | 97 |
| ZEN/USDT | P12_200 | 29 | 38 | 94 |
| ZEN/USDT | P8_200 | 35 | 42 | 83 |

## Leg 4 — Selection-bias check against the in-sample winners

| Population | Cells | Out-of-sample PF > 1 | With enough OOS trades | Survive the full §3.4 gate |
|---|---|---|---|---|
| in-sample net PF > 1 (checked by the pipeline) | 287 | 132 | 128 | 10 |
| all cells | 17556 | 608 | 591 | 10 |

## Gates (PROMPT.md §3.3, §3.4)

- Grid cells evaluated out of sample: **17556** (the pipeline had only checked 287).
- Credible candidates found anywhere in the grid: **10**.
- Exploratory signals found anywhere in the grid: **587**.
- Screen survivors verified with a real backtest: **1426**.

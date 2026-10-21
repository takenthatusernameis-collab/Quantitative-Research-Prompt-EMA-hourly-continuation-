# Pooled Robustness — EMA Hourly Continuation Grid

**Source run:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T03:35:19.915777+00:00
**Universe:** 266 symbols, 17556 grid cells (net of costs)

## Leg 1 — Drop the N largest market-cap names

| Universe | Symbols | Trades | Pooled net PF | Pooled net P&L |
|---|---|---|---|---|
| all | 266 | 14241237 | 0.5225 | -149215079 |
| minus top 5 | 261 | 13970999 | 0.5248 | -146156752 |
| minus top 10 | 256 | 13691052 | 0.5263 | -143193946 |
| minus top 20 | 246 | 13146879 | 0.5280 | -137380088 |
| minus top 50 | 216 | 11560885 | 0.5303 | -120639897 |

The pooled net PF is a trade-level ratio of summed net wins to summed net losses, not a mean of per-cell profit factors.

## Leg 2 — Pooled result by market-cap rank bucket

| Rank bucket | Symbols | Trades | Pooled net PF |
|---|---|---|---|
| 101-200 | 100 | 5317386 | 0.5360 |
| 11-50 | 40 | 2130167 | 0.5037 |
| 201+ | 66 | 3469665 | 0.5302 |
| 51-100 | 50 | 2773834 | 0.5188 |
| 1-10 | 10 | 550185 | 0.4083 |

## Leg 3 — Subperiod stability of every net PF > 1 cell

Subperiods per cell: 4 (equal-time slices of the cell's own trade timeline).

| Symbol | Cell | Trades | Full-sample net PF | Subperiod net PF (trades) | Verdict |
|---|---|---|---|---|---|
| BABYDOGE/USDT | P100_144 | 13 | 1.4324 | inf(1) / n/a(0) / 0.9189(4) / 1.4632(8) | insufficient |
| BABYDOGE/USDT | P12_200 | 71 | 1.2044 | 1.5046(13) / 1.8859(36) / 0.7930(11) / 0.3533(11) | fragile |
| BABYDOGE/USDT | P12_26 | 28 | 1.2032 | 0.0000(2) / 0.0000(1) / 2.7209(12) / 1.0389(13) | fragile |
| BABYDOGE/USDT | P12_50 | 63 | 1.0013 | 0.1870(6) / 1.2774(46) / 1.5510(8) / 0.0000(3) | fragile |
| BABYDOGE/USDT | P20_100 | 54 | 1.0785 | 0.1926(6) / 1.2489(33) / 1.1277(11) / 2.7987(4) | fragile |
| BABYDOGE/USDT | P20_200 | 57 | 1.2921 | 1.4111(10) / 1.7033(28) / 0.9517(12) / 0.7117(7) | fragile |
| BABYDOGE/USDT | P20_26 | 14 | 1.2053 | inf(1) / 0.0000(1) / 3.6575(5) / 0.6634(7) | fragile |
| BABYDOGE/USDT | P20_50 | 35 | 1.3666 | 0.4672(3) / 1.6072(25) / 1.8415(6) / 0.0000(1) | fragile |
| BABYDOGE/USDT | P20_55 | 39 | 1.1769 | 0.4684(3) / 1.1095(29) / 4.6582(6) / 0.0000(1) | fragile |
| BABYDOGE/USDT | P21_100 | 49 | 1.0535 | 0.3775(7) / 1.2332(28) / 1.1277(11) / 1.8824(3) | fragile |
| BABYDOGE/USDT | P21_200 | 59 | 1.1936 | 1.4118(10) / 1.3326(29) / 0.9516(12) / 0.9456(8) | fragile |
| BABYDOGE/USDT | P21_26 | 12 | 1.2754 | inf(1) / 0.0000(1) / 2.7686(4) / 0.8890(6) | insufficient |
| BABYDOGE/USDT | P21_50 | 32 | 1.3326 | 0.4523(3) / 1.5895(22) / 1.8415(6) / 0.0000(1) | fragile |
| BABYDOGE/USDT | P21_55 | 37 | 1.1914 | 0.9059(4) / 1.0518(26) / 4.6582(6) / 0.0000(1) | fragile |
| BABYDOGE/USDT | P21_89 | 53 | 1.0380 | 0.3734(7) / 1.1634(34) / 0.9392(10) / inf(2) | fragile |
| BABYDOGE/USDT | P26_100 | 51 | 1.2095 | 0.3164(4) / 1.5863(19) / 1.0694(24) / 2.7802(4) | fragile |
| BABYDOGE/USDT | P26_200 | 62 | 1.1332 | 1.5697(8) / 0.9792(37) / 1.4169(10) / 1.2595(7) | fragile |
| BABYDOGE/USDT | P26_50 | 27 | 1.7955 | 0.0000(1) / 2.0327(13) / 1.7545(12) / inf(1) | fragile |
| BABYDOGE/USDT | P26_55 | 30 | 1.1667 | 0.9053(2) / 0.9108(12) / 1.3109(15) / inf(1) | fragile |
| BABYDOGE/USDT | P26_89 | 46 | 1.2989 | 0.2365(5) / 2.2056(17) / 1.0805(22) / inf(2) | fragile |
| BABYDOGE/USDT | P34_200 | 50 | 1.0099 | 0.9447(6) / 1.0437(17) / 0.9291(16) / 1.1225(11) | fragile |
| BABYDOGE/USDT | P34_89 | 41 | 1.1613 | 0.3133(4) / 1.4604(13) / 0.9850(21) / inf(3) | fragile |
| BABYDOGE/USDT | P50_100 | 34 | 1.1493 | inf(1) / 1.0619(13) / 1.1281(18) / 0.9245(2) | fragile |
| BABYDOGE/USDT | P50_200 | 46 | 1.4460 | 0.9309(4) / 1.7152(20) / 0.9280(16) / 4.7372(6) | fragile |
| BABYDOGE/USDT | P50_55 | 7 | 2.2274 | inf(1) / n/a(0) / 1.9141(3) / 1.6718(3) | insufficient |
| BABYDOGE/USDT | P50_89 | 28 | 1.6157 | inf(1) / 1.5658(11) / 1.1869(14) / inf(2) | stable |
| BABYDOGE/USDT | P55_200 | 43 | 1.2924 | 0.9309(4) / 1.4469(18) / 0.9353(16) / 3.7725(5) | fragile |
| BABYDOGE/USDT | P89_100 | 8 | 1.4779 | inf(1) / n/a(0) / 0.9244(2) / 1.2881(5) | insufficient |
| BABYDOGE/USDT | P89_144 | 21 | 1.2180 | inf(1) / 0.9237(6) / 1.0531(13) / inf(1) | fragile |
| BABYDOGE/USDT | P8_20 | 28 | 1.4021 | 0.9263(2) / n/a(0) / 0.9261(8) / 1.7930(18) | fragile |
| BABYDOGE/USDT | P8_21 | 33 | 1.3894 | 0.9278(2) / 1.3997(5) / 1.4972(8) / 1.4046(18) | fragile |
| BABYDOGE/USDT | P8_26 | 45 | 1.0298 | 0.0000(2) / 1.2577(36) / 0.9068(6) / 0.0000(1) | fragile |
| JASMY/USDT | P20_200 | 353 | 1.0097 | 1.3375(54) / 1.0187(85) / 1.1079(84) / 0.8415(130) | fragile |
| JASMY/USDT | P21_200 | 362 | 1.0341 | 1.2099(56) / 1.1531(95) / 1.1020(84) / 0.8553(127) | fragile |
| MOODENG/USDT | P8_200 | 213 | 1.0567 | 1.5790(40) / 1.3157(20) / 0.9409(81) / 0.9222(72) | fragile |
| SUPER/USDT | P8_200 | 307 | 1.0377 | 1.1335(100) / 0.9220(83) / 1.0374(88) / 1.0873(36) | fragile |

Verdict counts: insufficient=4, fragile=31, stable=1.

Verdict rules: `stable` = every slice that carries trades kept net PF > 1; `fragile` = the slices disagree on the sign; `loss_only` = no slice made money; `insufficient` = fewer than two slices carry at least 5 trades.

## Gates (PROMPT.md §3.3, §3.4)

- Cells with full-sample net PF > 1: **36** of 17556 (0.21%).
- Cells whose edge is stable in every subperiod: **1**.
- Cells judged fragile across subperiods: **31**.
- Cells with too few subperiod trades to judge: **4**.
- Cells with no subperiod making money: **0**.
- No cell may be promoted on full-sample net PF alone; the OOS and 2x-cost gates in `scripts/candidate_check.py` apply on top of these legs.

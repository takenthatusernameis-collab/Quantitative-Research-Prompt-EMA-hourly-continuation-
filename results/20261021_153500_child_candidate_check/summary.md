# Candidate Check — OOS + Cost Stress for net PF > 1 Grid Cells

**Source run:** `results/20261021_125403_grid`
**OOS fraction:** trailing 35% of bars
**Cost stress:** 2x fees and slippage
**Base costs:** 10 bps taker + 2 bps slippage per side

| Symbol | Cell | Label | Base PF | Base Sharpe | OOS PF | OOS Sharpe | OOS trades | Stress PF | Stress OOS PF |
|---|---|---|---|---|---|---|---|---|---|
| AERO/USDT | P12_200 | credible candidate | 1.1454 | 0.7536 | 1.1491 | 0.7642 | 89 | 1.0376 | 1.0137 |
| BLUR/USDT | P8_200 | credible candidate | 1.1877 | 0.8309 | 1.3389 | 1.4745 | 88 | 1.0185 | 1.1488 |
| CETUS/USDT | P8_200 | credible candidate | 1.2740 | 1.1430 | 1.4174 | 1.7508 | 86 | 1.1282 | 1.2401 |
| CETUS/USDT | P12_200 | credible candidate | 1.2391 | 1.0467 | 1.2746 | 1.1335 | 68 | 1.1052 | 1.1338 |
| ENA/USDT | P20_21 | credible candidate | 1.3253 | 0.9192 | 1.3902 | 1.1879 | 46 | 1.0275 | 1.0324 |
| FLUX/USDT | P8_200 | credible candidate | 1.2228 | 1.0219 | 1.2427 | 1.2438 | 125 | 1.0484 | 1.0272 |
| IMX/USDT | P8_200 | credible candidate | 1.2102 | 0.9746 | 1.2911 | 1.3772 | 100 | 1.0421 | 1.0899 |
| PUFFER/USDT | P20_200 | credible candidate | 1.1884 | 0.9480 | 1.4038 | 1.8699 | 82 | 1.0431 | 1.2514 |
| WLD/USDT | P20_200 | credible candidate | 1.1725 | 0.8127 | 1.2811 | 1.3078 | 100 | 1.0517 | 1.1347 |
| ZEN/USDT | P8_200 | credible candidate | 1.2569 | 0.7759 | 1.6713 | 1.7541 | 42 | 1.1223 | 1.4974 |

Decision gates (PROMPT.md §3.4): credible candidate = net OOS PF > 1, net OOS Sharpe > 0, >= 30 OOS trades, and net PF still > 1 under the cost stress.

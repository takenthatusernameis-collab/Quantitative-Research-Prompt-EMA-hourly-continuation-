# Candidate Check — OOS + Cost Stress for net PF > 1 Grid Cells

**Source run:** `results/20261019_135940_grid`
**OOS fraction:** trailing 35% of bars
**Cost stress:** 2x fees and slippage
**Base costs:** 10 bps taker + 2 bps slippage per side

| Symbol | Cell | Label | Base PF | Base Sharpe | OOS PF | OOS Sharpe | OOS trades | Stress PF | Stress OOS PF |
|---|---|---|---|---|---|---|---|---|---|
| JASMY/USDT | P20_200 | rejected | 1.0097 | 0.1189 | 0.9068 | -0.5973 | 174 | 0.7465 | 0.5944 |
| JASMY/USDT | P21_200 | rejected | 1.0341 | 0.2673 | 0.9167 | -0.5194 | 173 | 0.7576 | 0.6015 |
| SUPER/USDT | P8_200 | rejected | 1.0377 | 0.2611 | 0.9536 | -0.1638 | 78 | 0.8093 | 0.7176 |

Decision gates (PROMPT.md §3.4): credible candidate = net OOS PF > 1, net OOS Sharpe > 0, >= 30 OOS trades, and net PF still > 1 under the cost stress.

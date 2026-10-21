# EMA Hourly Continuation — ROSE/USDT P89_144

**Symbol:** ROSE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.5847 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -3.4526 |
| sortino_ratio | -1.0726 |
| max_drawdown | 0.7340 |
| cagr | -0.4024 |
| net_avg_win | 43.1034 |
| net_avg_loss | -70.7317 |
| avg_hold_time_bars | 4.9959 |
| exposure | 0.1099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

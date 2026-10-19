# EMA Hourly Continuation — LINK/USDT P20_50

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.4948 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.8843 |
| gross_win_rate | 0.4408 |
| sharpe_ratio | -8.0576 |
| sortino_ratio | -3.4069 |
| max_drawdown | 0.9862 |
| cagr | -0.8166 |
| net_avg_win | 24.6973 |
| net_avg_loss | -38.1157 |
| avg_hold_time_bars | 5.1052 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

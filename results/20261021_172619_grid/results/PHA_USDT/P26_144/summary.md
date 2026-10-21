# EMA Hourly Continuation — PHA/USDT P26_144

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8443 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -2.0214 |
| sortino_ratio | -0.5700 |
| max_drawdown | 0.4886 |
| cagr | -0.2315 |
| net_avg_win | 66.6138 |
| net_avg_loss | -79.6308 |
| avg_hold_time_bars | 24.0101 |
| exposure | 0.4311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

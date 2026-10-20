# EMA Hourly Continuation — CELO/USDT P21_50

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.4571 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.7833 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -7.1103 |
| sortino_ratio | -3.0798 |
| max_drawdown | 0.9764 |
| cagr | -0.7724 |
| net_avg_win | 19.9945 |
| net_avg_loss | -33.9860 |
| avg_hold_time_bars | 5.4213 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

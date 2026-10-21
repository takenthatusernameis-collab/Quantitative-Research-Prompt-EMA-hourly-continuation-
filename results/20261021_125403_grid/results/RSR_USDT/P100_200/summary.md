# EMA Hourly Continuation — RSR/USDT P100_200

**Symbol:** RSR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8563 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0520 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -0.7279 |
| sortino_ratio | -0.1777 |
| max_drawdown | 0.2306 |
| cagr | -0.0805 |
| net_avg_win | 75.9921 |
| net_avg_loss | -95.1320 |
| avg_hold_time_bars | 11.2153 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

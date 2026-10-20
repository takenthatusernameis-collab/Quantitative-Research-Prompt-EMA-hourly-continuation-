# EMA Hourly Continuation — PROM/USDT P8_20

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1592 |
| net_profit_factor | 0.4116 |
| net_win_rate | 0.3888 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -13.2668 |
| sortino_ratio | -7.4907 |
| max_drawdown | 0.9999 |
| cagr | -0.9777 |
| net_avg_win | 11.3004 |
| net_avg_loss | -17.4658 |
| avg_hold_time_bars | 3.6778 |
| exposure | 0.2661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

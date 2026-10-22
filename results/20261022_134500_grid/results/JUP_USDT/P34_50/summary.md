# EMA Hourly Continuation — JUP/USDT P34_50

**Symbol:** JUP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.4756 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.9554 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -7.3006 |
| sortino_ratio | -3.1261 |
| max_drawdown | 0.9802 |
| cagr | -0.7861 |
| net_avg_win | 21.0435 |
| net_avg_loss | -37.6462 |
| avg_hold_time_bars | 2.5861 |
| exposure | 0.1079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

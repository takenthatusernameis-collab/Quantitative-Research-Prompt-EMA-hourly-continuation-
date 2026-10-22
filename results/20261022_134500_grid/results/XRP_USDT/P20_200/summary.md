# EMA Hourly Continuation — XRP/USDT P20_200

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.4996 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9335 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -4.0109 |
| sortino_ratio | -1.0988 |
| max_drawdown | 0.7599 |
| cagr | -0.4244 |
| net_avg_win | 41.1580 |
| net_avg_loss | -72.4299 |
| avg_hold_time_bars | 36.1003 |
| exposure | 0.6383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

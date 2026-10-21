# EMA Hourly Continuation — SYN/USDT P55_100

**Symbol:** SYN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7873 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.5245 |
| sortino_ratio | -0.4265 |
| max_drawdown | 0.4066 |
| cagr | -0.1786 |
| net_avg_win | 75.5751 |
| net_avg_loss | -96.4926 |
| avg_hold_time_bars | 8.7795 |
| exposure | 0.1520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

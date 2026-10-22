# EMA Hourly Continuation — OGN/USDT P8_50

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.7215 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9578 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -3.1058 |
| sortino_ratio | -1.2052 |
| max_drawdown | 0.7556 |
| cagr | -0.4245 |
| net_avg_win | 54.2488 |
| net_avg_loss | -70.2968 |
| avg_hold_time_bars | 13.3096 |
| exposure | 0.4475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

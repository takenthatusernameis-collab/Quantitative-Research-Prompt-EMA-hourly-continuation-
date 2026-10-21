# EMA Hourly Continuation — PHA/USDT P20_100

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7925 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.6105 |
| sortino_ratio | -0.5015 |
| max_drawdown | 0.4677 |
| cagr | -0.2072 |
| net_avg_win | 72.7503 |
| net_avg_loss | -87.2795 |
| avg_hold_time_bars | 18.8088 |
| exposure | 0.4070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

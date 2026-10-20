# EMA Hourly Continuation — PHA/USDT P20_34

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1151 |
| net_profit_factor | 0.4084 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -9.2543 |
| sortino_ratio | -4.4274 |
| max_drawdown | 0.9963 |
| cagr | -0.8912 |
| net_avg_win | 13.8368 |
| net_avg_loss | -25.7475 |
| avg_hold_time_bars | 2.8375 |
| exposure | 0.1485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

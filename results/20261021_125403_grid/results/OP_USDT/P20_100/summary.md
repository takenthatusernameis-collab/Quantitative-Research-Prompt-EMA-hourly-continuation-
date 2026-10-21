# EMA Hourly Continuation — OP/USDT P20_100

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7976 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9823 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -1.5502 |
| sortino_ratio | -0.4493 |
| max_drawdown | 0.4505 |
| cagr | -0.1876 |
| net_avg_win | 78.8907 |
| net_avg_loss | -96.0737 |
| avg_hold_time_bars | 23.4369 |
| exposure | 0.4389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

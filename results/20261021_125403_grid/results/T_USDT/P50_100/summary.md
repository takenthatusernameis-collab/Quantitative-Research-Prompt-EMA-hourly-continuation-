# EMA Hourly Continuation — T/USDT P50_100

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -3.1469 |
| sortino_ratio | -0.8945 |
| max_drawdown | 0.6556 |
| cagr | -0.3360 |
| net_avg_win | 50.6299 |
| net_avg_loss | -75.1527 |
| avg_hold_time_bars | 10.9849 |
| exposure | 0.1973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

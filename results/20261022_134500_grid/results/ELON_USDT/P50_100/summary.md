# EMA Hourly Continuation — ELON/USDT P50_100

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.4118 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.7296 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -5.9669 |
| sortino_ratio | -2.0953 |
| max_drawdown | 0.9250 |
| cagr | -0.6360 |
| net_avg_win | 23.8796 |
| net_avg_loss | -45.5144 |
| avg_hold_time_bars | 5.4756 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

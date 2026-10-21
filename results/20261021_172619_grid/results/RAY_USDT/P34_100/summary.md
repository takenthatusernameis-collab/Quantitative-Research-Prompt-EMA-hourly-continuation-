# EMA Hourly Continuation — RAY/USDT P34_100

**Symbol:** RAY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.9099 |
| net_win_rate | 0.5341 |
| gross_profit_factor | 1.1292 |
| gross_win_rate | 0.5341 |
| sharpe_ratio | -0.5495 |
| sortino_ratio | -0.1664 |
| max_drawdown | 0.2939 |
| cagr | -0.0782 |
| net_avg_win | 79.5583 |
| net_avg_loss | -100.2276 |
| avg_hold_time_bars | 10.9864 |
| exposure | 0.2197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

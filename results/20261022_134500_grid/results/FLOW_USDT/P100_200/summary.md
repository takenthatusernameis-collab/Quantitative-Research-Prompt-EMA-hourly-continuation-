# EMA Hourly Continuation — FLOW/USDT P100_200

**Symbol:** FLOW/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.5367 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -3.9850 |
| sortino_ratio | -1.1153 |
| max_drawdown | 0.7448 |
| cagr | -0.4150 |
| net_avg_win | 48.4101 |
| net_avg_loss | -73.2405 |
| avg_hold_time_bars | 9.4734 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

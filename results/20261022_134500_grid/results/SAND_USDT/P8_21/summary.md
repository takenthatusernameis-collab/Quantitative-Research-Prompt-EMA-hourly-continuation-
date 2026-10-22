# EMA Hourly Continuation — SAND/USDT P8_21

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1612 |
| net_profit_factor | 0.2769 |
| net_win_rate | 0.4218 |
| gross_profit_factor | 0.7468 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -12.4958 |
| sortino_ratio | -7.0974 |
| max_drawdown | 0.9999 |
| cagr | -0.9730 |
| net_avg_win | 5.6303 |
| net_avg_loss | -14.8364 |
| avg_hold_time_bars | 3.1737 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

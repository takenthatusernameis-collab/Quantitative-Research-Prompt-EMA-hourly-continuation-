# EMA Hourly Continuation — ONDO/USDT P8_26

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.8644 |
| net_win_rate | 0.5338 |
| gross_profit_factor | 1.1263 |
| gross_win_rate | 0.5338 |
| sharpe_ratio | -1.0267 |
| sortino_ratio | -0.3657 |
| max_drawdown | 0.4047 |
| cagr | -0.1581 |
| net_avg_win | 69.0128 |
| net_avg_loss | -91.4083 |
| avg_hold_time_bars | 6.8946 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

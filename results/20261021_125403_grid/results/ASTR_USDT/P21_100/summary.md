# EMA Hourly Continuation — ASTR/USDT P21_100

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0474 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -1.5953 |
| sortino_ratio | -0.4938 |
| max_drawdown | 0.4926 |
| cagr | -0.2039 |
| net_avg_win | 70.4999 |
| net_avg_loss | -92.6803 |
| avg_hold_time_bars | 20.3654 |
| exposure | 0.4313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — SAFE/USDT P8_12

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6953 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9868 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.1441 |
| sortino_ratio | -0.5583 |
| max_drawdown | 0.4778 |
| cagr | -0.2246 |
| net_avg_win | 66.5485 |
| net_avg_loss | -92.8356 |
| avg_hold_time_bars | 6.3792 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

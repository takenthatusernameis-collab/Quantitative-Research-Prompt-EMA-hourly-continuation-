# EMA Hourly Continuation — CWEB/USDT P100_200

**Symbol:** CWEB/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.5741 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -3.3391 |
| sortino_ratio | -0.8013 |
| max_drawdown | 0.6695 |
| cagr | -0.3274 |
| net_avg_win | 62.9715 |
| net_avg_loss | -94.3116 |
| avg_hold_time_bars | 14.7329 |
| exposure | 0.1955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

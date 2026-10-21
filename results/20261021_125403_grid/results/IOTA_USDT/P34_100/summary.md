# EMA Hourly Continuation — IOTA/USDT P34_100

**Symbol:** IOTA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6463 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -3.0678 |
| sortino_ratio | -0.9202 |
| max_drawdown | 0.6744 |
| cagr | -0.3450 |
| net_avg_win | 59.7765 |
| net_avg_loss | -75.2004 |
| avg_hold_time_bars | 12.0493 |
| exposure | 0.2443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

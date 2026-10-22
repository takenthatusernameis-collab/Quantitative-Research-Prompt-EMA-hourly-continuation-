# EMA Hourly Continuation — MOVR/USDT P8_50

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.7776 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9791 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.1537 |
| sortino_ratio | -0.8405 |
| max_drawdown | 0.6388 |
| cagr | -0.3211 |
| net_avg_win | 59.0681 |
| net_avg_loss | -74.3496 |
| avg_hold_time_bars | 13.2997 |
| exposure | 0.4498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

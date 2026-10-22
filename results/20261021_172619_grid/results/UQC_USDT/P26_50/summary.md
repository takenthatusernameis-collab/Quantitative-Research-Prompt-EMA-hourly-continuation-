# EMA Hourly Continuation — UQC/USDT P26_50

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.3754 |
| net_win_rate | 0.3176 |
| gross_profit_factor | 0.5469 |
| gross_win_rate | 0.3176 |
| sharpe_ratio | -5.1346 |
| sortino_ratio | -1.0978 |
| max_drawdown | 0.7453 |
| cagr | -0.4143 |
| net_avg_win | 60.1341 |
| net_avg_loss | -74.5602 |
| avg_hold_time_bars | 44.9399 |
| exposure | 0.4739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

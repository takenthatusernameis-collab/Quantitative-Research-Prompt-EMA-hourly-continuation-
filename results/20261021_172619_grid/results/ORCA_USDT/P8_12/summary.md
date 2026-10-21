# EMA Hourly Continuation — ORCA/USDT P8_12

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7903 |
| net_win_rate | 0.5505 |
| gross_profit_factor | 1.2481 |
| gross_win_rate | 0.5573 |
| sharpe_ratio | -1.5061 |
| sortino_ratio | -0.4550 |
| max_drawdown | 0.4390 |
| cagr | -0.1881 |
| net_avg_win | 63.9572 |
| net_avg_loss | -99.0980 |
| avg_hold_time_bars | 5.1972 |
| exposure | 0.1030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

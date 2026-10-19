# EMA Hourly Continuation — UNI/USDT P8_55

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1083 |
| net_profit_factor | 0.6006 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -6.1987 |
| sortino_ratio | -2.8576 |
| max_drawdown | 0.9703 |
| cagr | -0.7503 |
| net_avg_win | 29.3343 |
| net_avg_loss | -41.4208 |
| avg_hold_time_bars | 9.3657 |
| exposure | 0.4610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

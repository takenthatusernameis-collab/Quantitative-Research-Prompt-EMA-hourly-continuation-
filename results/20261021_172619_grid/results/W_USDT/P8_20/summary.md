# EMA Hourly Continuation — W/USDT P8_20

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.7810 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.8992 |
| sortino_ratio | -0.6366 |
| max_drawdown | 0.5395 |
| cagr | -0.2537 |
| net_avg_win | 67.2434 |
| net_avg_loss | -88.6680 |
| avg_hold_time_bars | 5.0092 |
| exposure | 0.1239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

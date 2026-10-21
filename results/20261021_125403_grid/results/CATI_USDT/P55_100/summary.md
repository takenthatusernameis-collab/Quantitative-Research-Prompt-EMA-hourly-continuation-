# EMA Hourly Continuation — CATI/USDT P55_100

**Symbol:** CATI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.6098 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8075 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -2.8008 |
| sortino_ratio | -0.6973 |
| max_drawdown | 0.5106 |
| cagr | -0.2753 |
| net_avg_win | 66.9763 |
| net_avg_loss | -88.8003 |
| avg_hold_time_bars | 10.5098 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

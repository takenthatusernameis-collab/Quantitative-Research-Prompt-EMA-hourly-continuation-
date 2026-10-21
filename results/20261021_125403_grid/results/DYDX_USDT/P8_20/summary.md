# EMA Hourly Continuation — DYDX/USDT P8_20

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.7167 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9788 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2761 |
| sortino_ratio | -0.7621 |
| max_drawdown | 0.5829 |
| cagr | -0.2940 |
| net_avg_win | 54.2086 |
| net_avg_loss | -75.6378 |
| avg_hold_time_bars | 5.5276 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

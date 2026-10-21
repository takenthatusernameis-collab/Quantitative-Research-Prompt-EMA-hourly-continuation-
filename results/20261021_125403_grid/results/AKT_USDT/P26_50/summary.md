# EMA Hourly Continuation — AKT/USDT P26_50

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8088 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0527 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.2230 |
| sortino_ratio | -0.3382 |
| max_drawdown | 0.3765 |
| cagr | -0.1442 |
| net_avg_win | 72.0373 |
| net_avg_loss | -94.5404 |
| avg_hold_time_bars | 6.7371 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

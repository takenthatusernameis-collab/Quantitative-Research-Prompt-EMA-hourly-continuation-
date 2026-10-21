# EMA Hourly Continuation — INJ/USDT P20_50

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8654 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0998 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -1.0375 |
| sortino_ratio | -0.3277 |
| max_drawdown | 0.3834 |
| cagr | -0.1421 |
| net_avg_win | 81.8489 |
| net_avg_loss | -103.6599 |
| avg_hold_time_bars | 7.3937 |
| exposure | 0.1613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

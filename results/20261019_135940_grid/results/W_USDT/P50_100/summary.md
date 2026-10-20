# EMA Hourly Continuation — W/USDT P50_100

**Symbol:** W/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6025 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -3.5723 |
| sortino_ratio | -1.2374 |
| max_drawdown | 0.7955 |
| cagr | -0.4502 |
| net_avg_win | 39.1499 |
| net_avg_loss | -63.2928 |
| avg_hold_time_bars | 6.0770 |
| exposure | 0.1685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

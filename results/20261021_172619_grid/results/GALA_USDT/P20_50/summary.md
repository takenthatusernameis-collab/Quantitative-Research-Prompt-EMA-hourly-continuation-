# EMA Hourly Continuation — GALA/USDT P20_50

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6759 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8796 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.8011 |
| sortino_ratio | -0.8888 |
| max_drawdown | 0.6535 |
| cagr | -0.3345 |
| net_avg_win | 57.8166 |
| net_avg_loss | -74.8439 |
| avg_hold_time_bars | 6.9737 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

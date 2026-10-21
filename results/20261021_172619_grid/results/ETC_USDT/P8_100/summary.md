# EMA Hourly Continuation — ETC/USDT P8_100

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.7218 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9610 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -2.1585 |
| sortino_ratio | -0.6563 |
| max_drawdown | 0.5448 |
| cagr | -0.2598 |
| net_avg_win | 61.6689 |
| net_avg_loss | -82.8427 |
| avg_hold_time_bars | 31.8896 |
| exposure | 0.6566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

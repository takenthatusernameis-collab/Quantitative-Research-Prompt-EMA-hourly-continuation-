# EMA Hourly Continuation — ETC/USDT P20_50

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6285 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.4474 |
| sortino_ratio | -1.1056 |
| max_drawdown | 0.7210 |
| cagr | -0.3962 |
| net_avg_win | 50.6252 |
| net_avg_loss | -74.6441 |
| avg_hold_time_bars | 7.8317 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

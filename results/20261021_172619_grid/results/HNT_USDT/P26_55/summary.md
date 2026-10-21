# EMA Hourly Continuation — HNT/USDT P26_55

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.7451 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.7500 |
| sortino_ratio | -0.5043 |
| max_drawdown | 0.4526 |
| cagr | -0.2068 |
| net_avg_win | 64.4614 |
| net_avg_loss | -84.4080 |
| avg_hold_time_bars | 7.4988 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

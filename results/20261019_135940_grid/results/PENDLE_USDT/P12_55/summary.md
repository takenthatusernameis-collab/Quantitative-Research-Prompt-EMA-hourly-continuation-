# EMA Hourly Continuation — PENDLE/USDT P12_55

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.5902 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -5.7012 |
| sortino_ratio | -2.5675 |
| max_drawdown | 0.9559 |
| cagr | -0.7096 |
| net_avg_win | 28.7832 |
| net_avg_loss | -41.9249 |
| avg_hold_time_bars | 7.8530 |
| exposure | 0.3691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

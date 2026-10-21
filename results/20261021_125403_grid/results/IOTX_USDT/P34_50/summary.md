# EMA Hourly Continuation — IOTX/USDT P34_50

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6691 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.2013 |
| sortino_ratio | -0.5501 |
| max_drawdown | 0.4925 |
| cagr | -0.2216 |
| net_avg_win | 62.9451 |
| net_avg_loss | -92.8376 |
| avg_hold_time_bars | 5.8344 |
| exposure | 0.0801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — PENDLE/USDT P100_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5030 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.7571 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -3.9399 |
| sortino_ratio | -1.1567 |
| max_drawdown | 0.7553 |
| cagr | -0.4246 |
| net_avg_win | 38.9440 |
| net_avg_loss | -62.3893 |
| avg_hold_time_bars | 7.9657 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

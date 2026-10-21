# EMA Hourly Continuation — ZBCN/USDT P26_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 1.0109 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1528 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | 0.1294 |
| sortino_ratio | 0.0357 |
| max_drawdown | 0.2362 |
| cagr | 0.0084 |
| net_avg_win | 100.0204 |
| net_avg_loss | -115.7348 |
| avg_hold_time_bars | 30.4553 |
| exposure | 0.5044 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

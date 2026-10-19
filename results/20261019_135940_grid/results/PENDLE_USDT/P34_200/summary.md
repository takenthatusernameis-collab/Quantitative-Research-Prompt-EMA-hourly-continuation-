# EMA Hourly Continuation — PENDLE/USDT P34_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5893 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8084 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -3.1119 |
| sortino_ratio | -0.8364 |
| max_drawdown | 0.6473 |
| cagr | -0.3333 |
| net_avg_win | 55.2056 |
| net_avg_loss | -75.8576 |
| avg_hold_time_bars | 33.1348 |
| exposure | 0.5588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

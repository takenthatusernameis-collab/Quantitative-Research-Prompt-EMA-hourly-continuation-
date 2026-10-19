# EMA Hourly Continuation — KMNO/USDT P34_200

**Symbol:** KMNO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6173 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8449 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -2.9540 |
| sortino_ratio | -0.7996 |
| max_drawdown | 0.6131 |
| cagr | -0.3140 |
| net_avg_win | 59.9958 |
| net_avg_loss | -79.2073 |
| avg_hold_time_bars | 27.5510 |
| exposure | 0.4617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

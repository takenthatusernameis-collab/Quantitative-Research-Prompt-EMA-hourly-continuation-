# EMA Hourly Continuation — IOTA/USDT P12_200

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7635 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0419 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -1.6115 |
| sortino_ratio | -0.4351 |
| max_drawdown | 0.4482 |
| cagr | -0.1878 |
| net_avg_win | 71.0198 |
| net_avg_loss | -94.5471 |
| avg_hold_time_bars | 45.2888 |
| exposure | 0.7555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

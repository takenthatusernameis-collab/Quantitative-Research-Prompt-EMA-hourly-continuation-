# EMA Hourly Continuation — DEGEN/USDT P89_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 1.0363 |
| net_win_rate | 0.5578 |
| gross_profit_factor | 1.2502 |
| gross_win_rate | 0.5578 |
| sharpe_ratio | 0.2304 |
| sortino_ratio | 0.0531 |
| max_drawdown | 0.1366 |
| cagr | 0.0183 |
| net_avg_win | 94.6834 |
| net_avg_loss | -115.2413 |
| avg_hold_time_bars | 18.4582 |
| exposure | 0.2109 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

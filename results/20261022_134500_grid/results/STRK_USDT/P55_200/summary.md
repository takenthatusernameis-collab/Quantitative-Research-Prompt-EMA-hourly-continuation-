# EMA Hourly Continuation — STRK/USDT P55_200

**Symbol:** STRK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7001 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0155 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.1151 |
| sortino_ratio | -0.5812 |
| max_drawdown | 0.5727 |
| cagr | -0.2477 |
| net_avg_win | 61.1453 |
| net_avg_loss | -88.2388 |
| avg_hold_time_bars | 20.9485 |
| exposure | 0.3695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

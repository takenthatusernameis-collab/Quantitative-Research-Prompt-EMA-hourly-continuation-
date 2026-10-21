# EMA Hourly Continuation — EGLD/USDT P8_200

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.8298 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.0421 |
| sortino_ratio | -0.2704 |
| max_drawdown | 0.3544 |
| cagr | -0.1187 |
| net_avg_win | 80.8615 |
| net_avg_loss | -96.8564 |
| avg_hold_time_bars | 51.7204 |
| exposure | 0.7735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

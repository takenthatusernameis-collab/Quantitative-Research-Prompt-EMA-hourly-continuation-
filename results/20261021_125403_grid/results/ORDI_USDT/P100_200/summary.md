# EMA Hourly Continuation — ORDI/USDT P100_200

**Symbol:** ORDI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.5994 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7366 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -2.4461 |
| sortino_ratio | -0.5751 |
| max_drawdown | 0.4997 |
| cagr | -0.2327 |
| net_avg_win | 60.5714 |
| net_avg_loss | -77.7310 |
| avg_hold_time_bars | 11.4710 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — FLOW/USDT P50_200

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6092 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8583 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -3.0157 |
| sortino_ratio | -0.8233 |
| max_drawdown | 0.6298 |
| cagr | -0.3243 |
| net_avg_win | 56.7678 |
| net_avg_loss | -78.1830 |
| avg_hold_time_bars | 23.0398 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

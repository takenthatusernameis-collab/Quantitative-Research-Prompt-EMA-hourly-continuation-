# EMA Hourly Continuation — PIXEL/USDT P26_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.9315 |
| net_win_rate | 0.5375 |
| gross_profit_factor | 1.1784 |
| gross_win_rate | 0.5440 |
| sharpe_ratio | -0.3487 |
| sortino_ratio | -0.0870 |
| max_drawdown | 0.1972 |
| cagr | -0.0444 |
| net_avg_win | 89.1379 |
| net_avg_loss | -111.1953 |
| avg_hold_time_bars | 45.9935 |
| exposure | 0.6389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

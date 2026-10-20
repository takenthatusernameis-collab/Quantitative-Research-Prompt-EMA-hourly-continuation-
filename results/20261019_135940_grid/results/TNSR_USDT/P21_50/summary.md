# EMA Hourly Continuation — TNSR/USDT P21_50

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.6571 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -5.0407 |
| sortino_ratio | -2.1579 |
| max_drawdown | 0.9323 |
| cagr | -0.6453 |
| net_avg_win | 39.5477 |
| net_avg_loss | -56.4189 |
| avg_hold_time_bars | 5.2328 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

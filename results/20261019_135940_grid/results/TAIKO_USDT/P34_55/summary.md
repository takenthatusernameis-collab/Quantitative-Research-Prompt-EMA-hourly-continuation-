# EMA Hourly Continuation — TAIKO/USDT P34_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 769 |
| net_profit_factor | 0.4589 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -7.7528 |
| sortino_ratio | -3.1204 |
| max_drawdown | 0.9776 |
| cagr | -0.7938 |
| net_avg_win | 23.8627 |
| net_avg_loss | -42.7625 |
| avg_hold_time_bars | 3.6229 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

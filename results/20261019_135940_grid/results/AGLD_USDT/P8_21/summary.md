# EMA Hourly Continuation — AGLD/USDT P8_21

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1458 |
| net_profit_factor | 0.4158 |
| net_win_rate | 0.4335 |
| gross_profit_factor | 0.8325 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -9.5555 |
| sortino_ratio | -5.1469 |
| max_drawdown | 0.9982 |
| cagr | -0.9176 |
| net_avg_win | 11.2399 |
| net_avg_loss | -20.6843 |
| avg_hold_time_bars | 3.9705 |
| exposure | 0.2620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

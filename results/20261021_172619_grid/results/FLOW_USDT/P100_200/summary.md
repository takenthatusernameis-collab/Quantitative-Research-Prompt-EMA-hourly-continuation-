# EMA Hourly Continuation — FLOW/USDT P100_200

**Symbol:** FLOW/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.6633 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8624 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -2.2267 |
| sortino_ratio | -0.5219 |
| max_drawdown | 0.4558 |
| cagr | -0.2134 |
| net_avg_win | 71.9112 |
| net_avg_loss | -91.4583 |
| avg_hold_time_bars | 12.9114 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

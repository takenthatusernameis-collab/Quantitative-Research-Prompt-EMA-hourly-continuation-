# EMA Hourly Continuation — PENDLE/USDT P50_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -3.2781 |
| sortino_ratio | -1.0378 |
| max_drawdown | 0.7349 |
| cagr | -0.3926 |
| net_avg_win | 43.4968 |
| net_avg_loss | -65.9239 |
| avg_hold_time_bars | 12.7667 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

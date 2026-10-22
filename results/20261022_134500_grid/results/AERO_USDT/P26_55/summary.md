# EMA Hourly Continuation — AERO/USDT P26_55

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 847 |
| net_profit_factor | 0.4348 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.7385 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -6.4311 |
| sortino_ratio | -2.6236 |
| max_drawdown | 0.9619 |
| cagr | -0.7269 |
| net_avg_win | 19.4682 |
| net_avg_loss | -36.4319 |
| avg_hold_time_bars | 4.2633 |
| exposure | 0.1641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

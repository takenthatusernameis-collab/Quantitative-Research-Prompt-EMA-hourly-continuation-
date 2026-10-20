# EMA Hourly Continuation — AEVO/USDT P20_50

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.5369 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8833 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -6.5514 |
| sortino_ratio | -2.9169 |
| max_drawdown | 0.9723 |
| cagr | -0.7538 |
| net_avg_win | 25.1201 |
| net_avg_loss | -38.1133 |
| avg_hold_time_bars | 5.1794 |
| exposure | 0.2339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

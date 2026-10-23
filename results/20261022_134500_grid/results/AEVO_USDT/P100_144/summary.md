# EMA Hourly Continuation — AEVO/USDT P100_144

**Symbol:** AEVO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.4989 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8458 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -4.9099 |
| sortino_ratio | -1.5879 |
| max_drawdown | 0.8524 |
| cagr | -0.5281 |
| net_avg_win | 36.1520 |
| net_avg_loss | -59.0793 |
| avg_hold_time_bars | 4.1478 |
| exposure | 0.0978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

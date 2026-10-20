# EMA Hourly Continuation — AEVO/USDT P26_34

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1139 |
| net_profit_factor | 0.2927 |
| net_win_rate | 0.3845 |
| gross_profit_factor | 0.7165 |
| gross_win_rate | 0.4276 |
| sharpe_ratio | -11.8381 |
| sortino_ratio | -5.7184 |
| max_drawdown | 0.9993 |
| cagr | -0.9441 |
| net_avg_win | 9.4438 |
| net_avg_loss | -20.1561 |
| avg_hold_time_bars | 2.2625 |
| exposure | 0.1166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — AEVO/USDT P21_100

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7119 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 1.0167 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -3.1951 |
| sortino_ratio | -1.1701 |
| max_drawdown | 0.7709 |
| cagr | -0.4221 |
| net_avg_win | 56.4406 |
| net_avg_loss | -76.0391 |
| avg_hold_time_bars | 14.0149 |
| exposure | 0.4249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

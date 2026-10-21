# EMA Hourly Continuation — AEVO/USDT P21_100

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7794 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.9009 |
| sortino_ratio | -0.6070 |
| max_drawdown | 0.5534 |
| cagr | -0.2444 |
| net_avg_win | 73.0983 |
| net_avg_loss | -89.0631 |
| avg_hold_time_bars | 18.0318 |
| exposure | 0.4104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

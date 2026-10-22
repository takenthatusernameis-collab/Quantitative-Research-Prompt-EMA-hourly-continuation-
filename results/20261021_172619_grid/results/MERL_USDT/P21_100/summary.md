# EMA Hourly Continuation — MERL/USDT P21_100

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7671 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9001 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -1.8989 |
| sortino_ratio | -0.5808 |
| max_drawdown | 0.5443 |
| cagr | -0.2354 |
| net_avg_win | 74.2691 |
| net_avg_loss | -85.7541 |
| avg_hold_time_bars | 19.0108 |
| exposure | 0.4003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

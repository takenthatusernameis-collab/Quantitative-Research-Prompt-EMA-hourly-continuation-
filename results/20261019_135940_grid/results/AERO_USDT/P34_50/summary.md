# EMA Hourly Continuation — AERO/USDT P34_50

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.3207 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.6374 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -7.9963 |
| sortino_ratio | -3.2347 |
| max_drawdown | 0.9825 |
| cagr | -0.7996 |
| net_avg_win | 13.4061 |
| net_avg_loss | -31.1012 |
| avg_hold_time_bars | 2.8829 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LQTY/USDT P8_200

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.5136 |
| sortino_ratio | -0.3642 |
| max_drawdown | 0.3800 |
| cagr | -0.1582 |
| net_avg_win | 66.5731 |
| net_avg_loss | -87.5450 |
| avg_hold_time_bars | 63.5651 |
| exposure | 0.8399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

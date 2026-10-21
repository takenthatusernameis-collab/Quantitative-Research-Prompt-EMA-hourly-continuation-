# EMA Hourly Continuation — LUNC/USDT P26_200

**Symbol:** LUNC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7839 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9826 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.4473 |
| sortino_ratio | -0.4006 |
| max_drawdown | 0.4295 |
| cagr | -0.1697 |
| net_avg_win | 72.3578 |
| net_avg_loss | -91.8166 |
| avg_hold_time_bars | 28.4027 |
| exposure | 0.4841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

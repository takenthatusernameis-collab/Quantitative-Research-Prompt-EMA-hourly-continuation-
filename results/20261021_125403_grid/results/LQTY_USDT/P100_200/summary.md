# EMA Hourly Continuation — LQTY/USDT P100_200

**Symbol:** LQTY/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7398 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.5961 |
| sortino_ratio | -0.3967 |
| max_drawdown | 0.3717 |
| cagr | -0.1665 |
| net_avg_win | 70.7427 |
| net_avg_loss | -90.7258 |
| avg_hold_time_bars | 11.5099 |
| exposure | 0.1583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

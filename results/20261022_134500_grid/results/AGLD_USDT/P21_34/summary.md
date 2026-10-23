# EMA Hourly Continuation — AGLD/USDT P21_34

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1115 |
| net_profit_factor | 0.4259 |
| net_win_rate | 0.4215 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -8.9697 |
| sortino_ratio | -4.2511 |
| max_drawdown | 0.9945 |
| cagr | -0.8727 |
| net_avg_win | 15.6967 |
| net_avg_loss | -26.8563 |
| avg_hold_time_bars | 3.4547 |
| exposure | 0.1743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

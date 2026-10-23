# EMA Hourly Continuation — POLYX/USDT P89_100

**Symbol:** POLYX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.3136 |
| net_win_rate | 0.3965 |
| gross_profit_factor | 0.8503 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -8.5320 |
| sortino_ratio | -2.9365 |
| max_drawdown | 0.9792 |
| cagr | -0.7854 |
| net_avg_win | 19.6176 |
| net_avg_loss | -41.1044 |
| avg_hold_time_bars | 2.8887 |
| exposure | 0.0755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

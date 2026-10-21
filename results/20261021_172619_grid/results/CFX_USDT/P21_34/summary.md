# EMA Hourly Continuation — CFX/USDT P21_34

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.0601 |
| sortino_ratio | -0.5030 |
| max_drawdown | 0.4952 |
| cagr | -0.2053 |
| net_avg_win | 63.4410 |
| net_avg_loss | -91.1108 |
| avg_hold_time_bars | 5.7405 |
| exposure | 0.0754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

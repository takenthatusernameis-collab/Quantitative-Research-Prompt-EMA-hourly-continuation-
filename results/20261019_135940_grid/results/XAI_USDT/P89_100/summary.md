# EMA Hourly Continuation — XAI/USDT P89_100

**Symbol:** XAI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.3491 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.7542 |
| gross_win_rate | 0.4283 |
| sharpe_ratio | -8.8973 |
| sortino_ratio | -3.2426 |
| max_drawdown | 0.9849 |
| cagr | -0.8115 |
| net_avg_win | 20.8790 |
| net_avg_loss | -38.8973 |
| avg_hold_time_bars | 2.2601 |
| exposure | 0.0660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

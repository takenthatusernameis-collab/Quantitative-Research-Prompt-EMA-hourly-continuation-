# EMA Hourly Continuation — EWT/USDT P34_55

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.6344 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8578 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -2.2598 |
| sortino_ratio | -0.5103 |
| max_drawdown | 0.4488 |
| cagr | -0.2086 |
| net_avg_win | 66.4563 |
| net_avg_loss | -90.0134 |
| avg_hold_time_bars | 7.9761 |
| exposure | 0.0910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

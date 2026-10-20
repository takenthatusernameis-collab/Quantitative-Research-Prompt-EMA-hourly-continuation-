# EMA Hourly Continuation — CHR/USDT P26_50

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.4887 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -7.3604 |
| sortino_ratio | -3.2531 |
| max_drawdown | 0.9817 |
| cagr | -0.7921 |
| net_avg_win | 21.8564 |
| net_avg_loss | -34.7577 |
| avg_hold_time_bars | 3.9297 |
| exposure | 0.1744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

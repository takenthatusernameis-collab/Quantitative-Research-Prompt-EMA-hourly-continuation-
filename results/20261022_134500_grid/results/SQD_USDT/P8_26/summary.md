# EMA Hourly Continuation — SQD/USDT P8_26

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1401 |
| net_profit_factor | 0.5599 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -8.3934 |
| sortino_ratio | -4.4765 |
| max_drawdown | 0.9953 |
| cagr | -0.8889 |
| net_avg_win | 20.3886 |
| net_avg_loss | -28.9913 |
| avg_hold_time_bars | 3.8544 |
| exposure | 0.2538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CYBER/USDT P34_50

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 855 |
| net_profit_factor | 0.4653 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -8.5713 |
| sortino_ratio | -3.5545 |
| max_drawdown | 0.9892 |
| cagr | -0.8345 |
| net_avg_win | 23.3218 |
| net_avg_loss | -38.0587 |
| avg_hold_time_bars | 3.6819 |
| exposure | 0.1431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

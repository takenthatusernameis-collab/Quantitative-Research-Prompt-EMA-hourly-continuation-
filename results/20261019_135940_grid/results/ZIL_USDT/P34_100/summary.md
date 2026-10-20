# EMA Hourly Continuation — ZIL/USDT P34_100

**Symbol:** ZIL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.5807 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -4.7758 |
| sortino_ratio | -1.7455 |
| max_drawdown | 0.8890 |
| cagr | -0.5658 |
| net_avg_win | 38.5542 |
| net_avg_loss | -58.9116 |
| avg_hold_time_bars | 8.2940 |
| exposure | 0.2526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

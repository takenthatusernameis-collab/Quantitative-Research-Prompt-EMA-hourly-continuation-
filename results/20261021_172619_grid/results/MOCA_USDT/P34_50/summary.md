# EMA Hourly Continuation — MOCA/USDT P34_50

**Symbol:** MOCA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.6115 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -2.6582 |
| sortino_ratio | -0.6653 |
| max_drawdown | 0.5068 |
| cagr | -0.2617 |
| net_avg_win | 60.3881 |
| net_avg_loss | -86.7461 |
| avg_hold_time_bars | 5.4065 |
| exposure | 0.0753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ORCA/USDT P20_50

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.5564 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9310 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -5.9162 |
| sortino_ratio | -2.4722 |
| max_drawdown | 0.9555 |
| cagr | -0.7047 |
| net_avg_win | 28.5346 |
| net_avg_loss | -45.6234 |
| avg_hold_time_bars | 5.8809 |
| exposure | 0.2379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

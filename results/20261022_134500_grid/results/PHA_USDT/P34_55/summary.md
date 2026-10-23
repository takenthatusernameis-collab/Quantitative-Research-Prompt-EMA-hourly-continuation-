# EMA Hourly Continuation — PHA/USDT P34_55

**Symbol:** PHA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.3940 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.7702 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -7.6632 |
| sortino_ratio | -3.2212 |
| max_drawdown | 0.9819 |
| cagr | -0.7954 |
| net_avg_win | 16.6178 |
| net_avg_loss | -32.3905 |
| avg_hold_time_bars | 2.9819 |
| exposure | 0.1198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

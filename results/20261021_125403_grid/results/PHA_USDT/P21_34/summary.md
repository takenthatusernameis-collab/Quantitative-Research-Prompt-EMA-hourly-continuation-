# EMA Hourly Continuation — PHA/USDT P21_34

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8097 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0860 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -1.2793 |
| sortino_ratio | -0.3423 |
| max_drawdown | 0.4041 |
| cagr | -0.1463 |
| net_avg_win | 77.9064 |
| net_avg_loss | -103.7566 |
| avg_hold_time_bars | 4.9942 |
| exposure | 0.0783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

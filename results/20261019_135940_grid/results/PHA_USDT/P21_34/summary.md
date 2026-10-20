# EMA Hourly Continuation — PHA/USDT P21_34

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.4081 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -9.3962 |
| sortino_ratio | -4.4578 |
| max_drawdown | 0.9965 |
| cagr | -0.8941 |
| net_avg_win | 14.1681 |
| net_avg_loss | -26.1427 |
| avg_hold_time_bars | 2.7750 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MEW/USDT P21_34

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1081 |
| net_profit_factor | 0.4069 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 0.7296 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -9.7470 |
| sortino_ratio | -4.5573 |
| max_drawdown | 0.9963 |
| cagr | -0.8928 |
| net_avg_win | 15.5348 |
| net_avg_loss | -26.2068 |
| avg_hold_time_bars | 2.6984 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — IOTA/USDT P21_144

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.8396 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0251 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -1.0811 |
| sortino_ratio | -0.2968 |
| max_drawdown | 0.3471 |
| cagr | -0.1293 |
| net_avg_win | 83.1047 |
| net_avg_loss | -100.6122 |
| avg_hold_time_bars | 30.9700 |
| exposure | 0.5166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

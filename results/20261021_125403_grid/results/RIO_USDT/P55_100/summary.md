# EMA Hourly Continuation — RIO/USDT P55_100

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6755 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7923 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -2.2946 |
| sortino_ratio | -0.5689 |
| max_drawdown | 0.5025 |
| cagr | -0.2309 |
| net_avg_win | 75.0197 |
| net_avg_loss | -85.8799 |
| avg_hold_time_bars | 7.7574 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

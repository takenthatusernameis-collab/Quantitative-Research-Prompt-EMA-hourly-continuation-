# EMA Hourly Continuation — LPT/USDT P8_21

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9826 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -3.2473 |
| sortino_ratio | -1.2225 |
| max_drawdown | 0.7620 |
| cagr | -0.4291 |
| net_avg_win | 51.4297 |
| net_avg_loss | -72.4562 |
| avg_hold_time_bars | 5.0116 |
| exposure | 0.1570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — KSM/USDT P8_50

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.5314 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8700 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -7.1821 |
| sortino_ratio | -3.3107 |
| max_drawdown | 0.9834 |
| cagr | -0.8031 |
| net_avg_win | 23.1323 |
| net_avg_loss | -34.7941 |
| avg_hold_time_bars | 9.7447 |
| exposure | 0.4806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

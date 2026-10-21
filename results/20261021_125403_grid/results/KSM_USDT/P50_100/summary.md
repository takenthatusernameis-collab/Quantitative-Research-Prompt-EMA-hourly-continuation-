# EMA Hourly Continuation — KSM/USDT P50_100

**Symbol:** KSM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6973 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.1740 |
| sortino_ratio | -0.6096 |
| max_drawdown | 0.5327 |
| cagr | -0.2433 |
| net_avg_win | 61.7133 |
| net_avg_loss | -85.3204 |
| avg_hold_time_bars | 8.5509 |
| exposure | 0.1489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

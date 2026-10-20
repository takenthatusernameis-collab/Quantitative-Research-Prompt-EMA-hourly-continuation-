# EMA Hourly Continuation — HNT/USDT P34_100

**Symbol:** HNT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.5043 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.7614 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -5.1127 |
| sortino_ratio | -1.8955 |
| max_drawdown | 0.9034 |
| cagr | -0.5929 |
| net_avg_win | 29.9616 |
| net_avg_loss | -47.4062 |
| avg_hold_time_bars | 9.4190 |
| exposure | 0.2933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

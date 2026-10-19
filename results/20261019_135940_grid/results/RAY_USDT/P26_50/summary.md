# EMA Hourly Continuation — RAY/USDT P26_50

**Symbol:** RAY/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.5730 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -5.7546 |
| sortino_ratio | -2.4288 |
| max_drawdown | 0.9551 |
| cagr | -0.6942 |
| net_avg_win | 29.5482 |
| net_avg_loss | -47.3880 |
| avg_hold_time_bars | 3.8944 |
| exposure | 0.1593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

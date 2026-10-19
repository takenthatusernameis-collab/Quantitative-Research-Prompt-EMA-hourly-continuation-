# EMA Hourly Continuation — LTC/USDT P34_100

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.3612 |
| net_win_rate | 0.4078 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -7.5981 |
| sortino_ratio | -2.7715 |
| max_drawdown | 0.9713 |
| cagr | -0.7525 |
| net_avg_win | 20.1610 |
| net_avg_loss | -38.4402 |
| avg_hold_time_bars | 9.1184 |
| exposure | 0.2765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

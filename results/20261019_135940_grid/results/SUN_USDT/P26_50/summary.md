# EMA Hourly Continuation — SUN/USDT P26_50

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 818 |
| net_profit_factor | 0.2152 |
| net_win_rate | 0.3337 |
| gross_profit_factor | 0.7395 |
| gross_win_rate | 0.4022 |
| sharpe_ratio | -12.6791 |
| sortino_ratio | -5.3256 |
| max_drawdown | 0.9993 |
| cagr | -0.9430 |
| net_avg_win | 10.0356 |
| net_avg_loss | -23.3623 |
| avg_hold_time_bars | 5.4523 |
| exposure | 0.2018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XRP/USDT P21_100

**Symbol:** XRP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.4520 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.9234 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -6.6871 |
| sortino_ratio | -2.4697 |
| max_drawdown | 0.9609 |
| cagr | -0.7123 |
| net_avg_win | 26.0321 |
| net_avg_loss | -44.2889 |
| avg_hold_time_bars | 12.1650 |
| exposure | 0.3854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

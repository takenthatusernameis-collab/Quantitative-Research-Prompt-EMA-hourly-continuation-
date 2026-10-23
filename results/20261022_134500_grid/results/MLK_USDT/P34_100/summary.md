# EMA Hourly Continuation — MLK/USDT P34_100

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.2730 |
| net_win_rate | 0.2700 |
| gross_profit_factor | 0.5029 |
| gross_win_rate | 0.2823 |
| sharpe_ratio | -13.0297 |
| sortino_ratio | -5.5809 |
| max_drawdown | 0.9992 |
| cagr | -0.9388 |
| net_avg_win | 15.6327 |
| net_avg_loss | -21.1759 |
| avg_hold_time_bars | 6.7615 |
| exposure | 0.2720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

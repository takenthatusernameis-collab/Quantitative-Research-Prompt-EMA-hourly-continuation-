# EMA Hourly Continuation — KCS/USDT P21_89

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.2881 |
| net_win_rate | 0.3939 |
| gross_profit_factor | 0.7279 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -9.1561 |
| sortino_ratio | -3.3953 |
| max_drawdown | 0.9893 |
| cagr | -0.8338 |
| net_avg_win | 14.8813 |
| net_avg_loss | -33.5574 |
| avg_hold_time_bars | 12.3968 |
| exposure | 0.3849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

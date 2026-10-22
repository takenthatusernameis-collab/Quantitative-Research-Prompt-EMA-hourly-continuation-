# EMA Hourly Continuation — JUP/USDT P21_26

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.2900 |
| net_win_rate | 0.3792 |
| gross_profit_factor | 0.7905 |
| gross_win_rate | 0.4189 |
| sharpe_ratio | -13.1982 |
| sortino_ratio | -6.5715 |
| max_drawdown | 0.9998 |
| cagr | -0.9674 |
| net_avg_win | 9.0942 |
| net_avg_loss | -19.1584 |
| avg_hold_time_bars | 1.7407 |
| exposure | 0.0937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

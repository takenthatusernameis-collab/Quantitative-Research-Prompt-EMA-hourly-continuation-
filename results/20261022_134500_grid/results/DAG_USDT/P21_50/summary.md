# EMA Hourly Continuation — DAG/USDT P21_50

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1020 |
| net_profit_factor | 0.3887 |
| net_win_rate | 0.3931 |
| gross_profit_factor | 0.6435 |
| gross_win_rate | 0.4069 |
| sharpe_ratio | -9.4520 |
| sortino_ratio | -4.2386 |
| max_drawdown | 0.9955 |
| cagr | -0.8837 |
| net_avg_win | 15.7874 |
| net_avg_loss | -26.3098 |
| avg_hold_time_bars | 3.9010 |
| exposure | 0.1809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — PHA/USDT P55_100

**Symbol:** PHA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.4497 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.7423 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -6.1643 |
| sortino_ratio | -2.2094 |
| max_drawdown | 0.9369 |
| cagr | -0.6612 |
| net_avg_win | 27.8549 |
| net_avg_loss | -44.6641 |
| avg_hold_time_bars | 5.0688 |
| exposure | 0.1507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

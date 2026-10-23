# EMA Hourly Continuation — ONT/USDT P55_100

**Symbol:** ONT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.4781 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8033 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -5.1712 |
| sortino_ratio | -1.8345 |
| max_drawdown | 0.8937 |
| cagr | -0.5796 |
| net_avg_win | 28.7319 |
| net_avg_loss | -49.5835 |
| avg_hold_time_bars | 5.9361 |
| exposure | 0.1682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

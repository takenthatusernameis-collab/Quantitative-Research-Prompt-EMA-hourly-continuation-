# EMA Hourly Continuation — OP/USDT P34_50

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.8271 |
| net_win_rate | 0.5378 |
| gross_profit_factor | 1.1400 |
| gross_win_rate | 0.5378 |
| sharpe_ratio | -0.8439 |
| sortino_ratio | -0.1934 |
| max_drawdown | 0.2465 |
| cagr | -0.0855 |
| net_avg_win | 71.2653 |
| net_avg_loss | -100.2772 |
| avg_hold_time_bars | 5.1873 |
| exposure | 0.0592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

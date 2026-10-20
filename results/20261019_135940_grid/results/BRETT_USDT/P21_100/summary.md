# EMA Hourly Continuation — BRETT/USDT P21_100

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -3.9055 |
| sortino_ratio | -1.3848 |
| max_drawdown | 0.7918 |
| cagr | -0.4819 |
| net_avg_win | 50.0471 |
| net_avg_loss | -65.1851 |
| avg_hold_time_bars | 14.3721 |
| exposure | 0.4163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

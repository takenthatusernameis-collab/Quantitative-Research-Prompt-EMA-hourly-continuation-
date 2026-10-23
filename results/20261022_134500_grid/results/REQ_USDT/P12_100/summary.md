# EMA Hourly Continuation — REQ/USDT P12_100

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.4668 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 0.8503 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -7.9957 |
| sortino_ratio | -3.2268 |
| max_drawdown | 0.9839 |
| cagr | -0.8039 |
| net_avg_win | 25.3923 |
| net_avg_loss | -37.3297 |
| avg_hold_time_bars | 14.0504 |
| exposure | 0.5320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

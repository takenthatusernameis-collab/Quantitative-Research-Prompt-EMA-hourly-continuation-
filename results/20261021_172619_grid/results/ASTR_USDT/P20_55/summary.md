# EMA Hourly Continuation — ASTR/USDT P20_55

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9936 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -2.8504 |
| sortino_ratio | -0.9805 |
| max_drawdown | 0.6854 |
| cagr | -0.3633 |
| net_avg_win | 54.7799 |
| net_avg_loss | -77.7625 |
| avg_hold_time_bars | 8.4276 |
| exposure | 0.2212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

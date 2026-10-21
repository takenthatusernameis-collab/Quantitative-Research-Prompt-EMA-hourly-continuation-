# EMA Hourly Continuation — PYTH/USDT P34_100

**Symbol:** PYTH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7528 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9204 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -1.6963 |
| sortino_ratio | -0.4837 |
| max_drawdown | 0.4432 |
| cagr | -0.1998 |
| net_avg_win | 67.6202 |
| net_avg_loss | -84.1604 |
| avg_hold_time_bars | 13.2932 |
| exposure | 0.2411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

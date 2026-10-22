# EMA Hourly Continuation — THETA/USDT P55_100

**Symbol:** THETA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.4926 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -4.9217 |
| sortino_ratio | -1.7234 |
| max_drawdown | 0.8845 |
| cagr | -0.5721 |
| net_avg_win | 29.0981 |
| net_avg_loss | -52.7910 |
| avg_hold_time_bars | 4.9823 |
| exposure | 0.1411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

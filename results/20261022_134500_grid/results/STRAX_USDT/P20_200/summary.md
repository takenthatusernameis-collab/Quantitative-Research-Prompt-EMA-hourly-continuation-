# EMA Hourly Continuation — STRAX/USDT P20_200

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.5281 |
| net_win_rate | 0.4081 |
| gross_profit_factor | 0.7391 |
| gross_win_rate | 0.4151 |
| sharpe_ratio | -5.2564 |
| sortino_ratio | -1.7745 |
| max_drawdown | 0.8766 |
| cagr | -0.5674 |
| net_avg_win | 42.0970 |
| net_avg_loss | -54.9532 |
| avg_hold_time_bars | 21.3678 |
| exposure | 0.5578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

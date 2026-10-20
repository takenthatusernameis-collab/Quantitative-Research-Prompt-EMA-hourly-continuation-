# EMA Hourly Continuation — CGPT/USDT P100_200

**Symbol:** CGPT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.6432 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9945 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -2.7371 |
| sortino_ratio | -0.7401 |
| max_drawdown | 0.6036 |
| cagr | -0.2991 |
| net_avg_win | 58.8160 |
| net_avg_loss | -88.0317 |
| avg_hold_time_bars | 7.9756 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

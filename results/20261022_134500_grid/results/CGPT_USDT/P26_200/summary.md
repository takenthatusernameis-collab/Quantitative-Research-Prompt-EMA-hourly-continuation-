# EMA Hourly Continuation — CGPT/USDT P26_200

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7497 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0192 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.8189 |
| sortino_ratio | -0.5003 |
| max_drawdown | 0.4599 |
| cagr | -0.2122 |
| net_avg_win | 70.6752 |
| net_avg_loss | -94.7647 |
| avg_hold_time_bars | 31.7375 |
| exposure | 0.5496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

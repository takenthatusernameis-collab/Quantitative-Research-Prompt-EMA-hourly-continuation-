# EMA Hourly Continuation — SWFTC/USDT P26_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.4516 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.7408 |
| gross_win_rate | 0.4244 |
| sharpe_ratio | -6.7383 |
| sortino_ratio | -2.5395 |
| max_drawdown | 0.9567 |
| cagr | -0.7128 |
| net_avg_win | 26.4306 |
| net_avg_loss | -41.9239 |
| avg_hold_time_bars | 9.2885 |
| exposure | 0.3015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CGPT/USDT P26_100

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.6304 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.9254 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -4.1033 |
| sortino_ratio | -1.4172 |
| max_drawdown | 0.8224 |
| cagr | -0.4946 |
| net_avg_win | 51.0319 |
| net_avg_loss | -67.2133 |
| avg_hold_time_bars | 12.4040 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

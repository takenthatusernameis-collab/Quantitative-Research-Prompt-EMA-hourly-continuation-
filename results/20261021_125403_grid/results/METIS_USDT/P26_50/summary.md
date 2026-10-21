# EMA Hourly Continuation — METIS/USDT P26_50

**Symbol:** METIS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7242 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.2078 |
| sortino_ratio | -0.6756 |
| max_drawdown | 0.5661 |
| cagr | -0.2656 |
| net_avg_win | 62.6948 |
| net_avg_loss | -85.4317 |
| avg_hold_time_bars | 6.1231 |
| exposure | 0.1266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

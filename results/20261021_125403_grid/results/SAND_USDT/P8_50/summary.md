# EMA Hourly Continuation — SAND/USDT P8_50

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.7046 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -2.9001 |
| sortino_ratio | -1.0683 |
| max_drawdown | 0.7176 |
| cagr | -0.3878 |
| net_avg_win | 53.3033 |
| net_avg_loss | -68.5184 |
| avg_hold_time_bars | 14.6462 |
| exposure | 0.4440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

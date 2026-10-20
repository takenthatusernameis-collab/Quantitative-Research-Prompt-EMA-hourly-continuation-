# EMA Hourly Continuation — ROSE/USDT P8_144

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.8954 |
| net_win_rate | 0.5355 |
| gross_profit_factor | 1.1707 |
| gross_win_rate | 0.5427 |
| sharpe_ratio | -0.6530 |
| sortino_ratio | -0.1921 |
| max_drawdown | 0.3068 |
| cagr | -0.0899 |
| net_avg_win | 79.7772 |
| net_avg_loss | -102.7382 |
| avg_hold_time_bars | 41.0640 |
| exposure | 0.7877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

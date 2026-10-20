# EMA Hourly Continuation — ROSE/USDT P8_100

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 1.0133 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -2.7946 |
| sortino_ratio | -0.9921 |
| max_drawdown | 0.7043 |
| cagr | -0.3758 |
| net_avg_win | 52.7135 |
| net_avg_loss | -72.6859 |
| avg_hold_time_bars | 24.0443 |
| exposure | 0.6907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

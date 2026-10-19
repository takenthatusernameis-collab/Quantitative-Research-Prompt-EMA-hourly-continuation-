# EMA Hourly Continuation — AKT/USDT P50_100

**Symbol:** AKT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6658 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0912 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -3.4743 |
| sortino_ratio | -1.2419 |
| max_drawdown | 0.7852 |
| cagr | -0.4543 |
| net_avg_win | 47.0278 |
| net_avg_loss | -72.6122 |
| avg_hold_time_bars | 5.7519 |
| exposure | 0.1707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

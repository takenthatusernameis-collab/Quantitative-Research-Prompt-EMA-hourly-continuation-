# EMA Hourly Continuation — IMX/USDT P12_100

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.9225 |
| sortino_ratio | -1.0731 |
| max_drawdown | 0.7384 |
| cagr | -0.3977 |
| net_avg_win | 42.7296 |
| net_avg_loss | -61.8584 |
| avg_hold_time_bars | 17.9882 |
| exposure | 0.5519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

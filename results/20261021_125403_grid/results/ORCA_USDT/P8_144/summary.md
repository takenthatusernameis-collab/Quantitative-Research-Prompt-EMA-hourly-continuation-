# EMA Hourly Continuation — ORCA/USDT P8_144

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8029 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.3068 |
| sortino_ratio | -0.3729 |
| max_drawdown | 0.3894 |
| cagr | -0.1601 |
| net_avg_win | 72.2584 |
| net_avg_loss | -89.5454 |
| avg_hold_time_bars | 40.3965 |
| exposure | 0.7363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

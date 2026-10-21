# EMA Hourly Continuation — ORCA/USDT P8_100

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.8336 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0267 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.2165 |
| sortino_ratio | -0.3929 |
| max_drawdown | 0.4121 |
| cagr | -0.1685 |
| net_avg_win | 71.4215 |
| net_avg_loss | -89.4685 |
| avg_hold_time_bars | 28.6444 |
| exposure | 0.6627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

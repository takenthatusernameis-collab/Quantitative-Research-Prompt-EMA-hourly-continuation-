# EMA Hourly Continuation — ORCA/USDT P8_34

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.8129 |
| net_win_rate | 0.5179 |
| gross_profit_factor | 1.0924 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -2.1396 |
| sortino_ratio | -0.8740 |
| max_drawdown | 0.6847 |
| cagr | -0.3337 |
| net_avg_win | 66.1521 |
| net_avg_loss | -87.4098 |
| avg_hold_time_bars | 8.8323 |
| exposure | 0.3256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

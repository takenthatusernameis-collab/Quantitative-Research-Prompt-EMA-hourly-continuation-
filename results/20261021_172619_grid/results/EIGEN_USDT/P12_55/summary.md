# EMA Hourly Continuation — EIGEN/USDT P12_55

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7907 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -1.9371 |
| sortino_ratio | -0.6763 |
| max_drawdown | 0.4938 |
| cagr | -0.2687 |
| net_avg_win | 75.8496 |
| net_avg_loss | -89.1275 |
| avg_hold_time_bars | 12.3061 |
| exposure | 0.3355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

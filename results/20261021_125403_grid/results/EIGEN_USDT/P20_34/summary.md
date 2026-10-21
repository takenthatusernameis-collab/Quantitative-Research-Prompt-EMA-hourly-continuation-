# EMA Hourly Continuation — EIGEN/USDT P20_34

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.7991 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0015 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.1639 |
| sortino_ratio | -0.2986 |
| max_drawdown | 0.3403 |
| cagr | -0.1292 |
| net_avg_win | 74.4482 |
| net_avg_loss | -95.3352 |
| avg_hold_time_bars | 5.6858 |
| exposure | 0.0826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

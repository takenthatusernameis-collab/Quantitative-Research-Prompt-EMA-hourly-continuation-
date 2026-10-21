# EMA Hourly Continuation — THETA/USDT P8_144

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.8366 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9892 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.0907 |
| sortino_ratio | -0.3032 |
| max_drawdown | 0.3759 |
| cagr | -0.1323 |
| net_avg_win | 81.6621 |
| net_avg_loss | -96.5816 |
| avg_hold_time_bars | 43.0106 |
| exposure | 0.7390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

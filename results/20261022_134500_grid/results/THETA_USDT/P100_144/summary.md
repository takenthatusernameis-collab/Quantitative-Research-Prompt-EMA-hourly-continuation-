# EMA Hourly Continuation — THETA/USDT P100_144

**Symbol:** THETA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.4260 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.8193 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -5.5561 |
| sortino_ratio | -1.7577 |
| max_drawdown | 0.8873 |
| cagr | -0.5791 |
| net_avg_win | 30.1756 |
| net_avg_loss | -54.7532 |
| avg_hold_time_bars | 3.3320 |
| exposure | 0.0757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

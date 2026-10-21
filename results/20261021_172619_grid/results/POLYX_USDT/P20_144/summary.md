# EMA Hourly Continuation — POLYX/USDT P20_144

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8116 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.2984 |
| sortino_ratio | -0.3694 |
| max_drawdown | 0.3899 |
| cagr | -0.1580 |
| net_avg_win | 75.9415 |
| net_avg_loss | -94.5151 |
| avg_hold_time_bars | 29.9874 |
| exposure | 0.5398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

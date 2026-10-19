# EMA Hourly Continuation — THETA/USDT P26_55

**Symbol:** THETA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.4778 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8338 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -6.9710 |
| sortino_ratio | -2.9769 |
| max_drawdown | 0.9748 |
| cagr | -0.7640 |
| net_avg_win | 21.5689 |
| net_avg_loss | -37.4334 |
| avg_hold_time_bars | 4.0461 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

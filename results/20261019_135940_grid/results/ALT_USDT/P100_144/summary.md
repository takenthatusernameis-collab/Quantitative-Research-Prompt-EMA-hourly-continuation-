# EMA Hourly Continuation — ALT/USDT P100_144

**Symbol:** ALT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.5329 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8942 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -3.9069 |
| sortino_ratio | -1.1729 |
| max_drawdown | 0.7589 |
| cagr | -0.4264 |
| net_avg_win | 41.4764 |
| net_avg_loss | -66.5698 |
| avg_hold_time_bars | 6.0535 |
| exposure | 0.1235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

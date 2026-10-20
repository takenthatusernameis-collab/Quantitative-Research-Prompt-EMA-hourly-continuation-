# EMA Hourly Continuation — CGPT/USDT P26_55

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 831 |
| net_profit_factor | 0.4911 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -6.4061 |
| sortino_ratio | -2.5990 |
| max_drawdown | 0.9607 |
| cagr | -0.7222 |
| net_avg_win | 24.7714 |
| net_avg_loss | -41.2768 |
| avg_hold_time_bars | 4.5884 |
| exposure | 0.1733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

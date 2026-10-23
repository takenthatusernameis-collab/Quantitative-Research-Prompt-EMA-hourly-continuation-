# EMA Hourly Continuation — ORCA/USDT P50_55

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.2813 |
| net_win_rate | 0.3795 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -10.8031 |
| sortino_ratio | -4.2886 |
| max_drawdown | 0.9971 |
| cagr | -0.9011 |
| net_avg_win | 13.6942 |
| net_avg_loss | -29.7702 |
| avg_hold_time_bars | 2.6911 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

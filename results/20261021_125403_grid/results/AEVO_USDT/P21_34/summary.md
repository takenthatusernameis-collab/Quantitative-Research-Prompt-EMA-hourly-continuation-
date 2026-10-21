# EMA Hourly Continuation — AEVO/USDT P21_34

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.7951 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -3.5074 |
| sortino_ratio | -0.9996 |
| max_drawdown | 0.6956 |
| cagr | -0.3677 |
| net_avg_win | 51.2218 |
| net_avg_loss | -72.1731 |
| avg_hold_time_bars | 5.1621 |
| exposure | 0.0937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

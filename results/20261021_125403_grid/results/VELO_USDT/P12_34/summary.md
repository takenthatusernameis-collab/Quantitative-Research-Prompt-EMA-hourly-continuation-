# EMA Hourly Continuation — VELO/USDT P12_34

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8597 |
| net_win_rate | 0.5238 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5238 |
| sharpe_ratio | -0.9805 |
| sortino_ratio | -0.3238 |
| max_drawdown | 0.3605 |
| cagr | -0.1415 |
| net_avg_win | 70.8915 |
| net_avg_loss | -90.7113 |
| avg_hold_time_bars | 6.9638 |
| exposure | 0.1662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

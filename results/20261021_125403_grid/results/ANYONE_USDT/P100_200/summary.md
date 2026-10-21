# EMA Hourly Continuation — ANYONE/USDT P100_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.7374 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -1.4404 |
| sortino_ratio | -0.3185 |
| max_drawdown | 0.3779 |
| cagr | -0.1369 |
| net_avg_win | 77.9130 |
| net_avg_loss | -92.9062 |
| avg_hold_time_bars | 15.7936 |
| exposure | 0.1740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

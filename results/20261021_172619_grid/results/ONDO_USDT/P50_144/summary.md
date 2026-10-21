# EMA Hourly Continuation — ONDO/USDT P50_144

**Symbol:** ONDO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.7337 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.7701 |
| sortino_ratio | -0.4662 |
| max_drawdown | 0.4303 |
| cagr | -0.1928 |
| net_avg_win | 70.7484 |
| net_avg_loss | -86.7889 |
| avg_hold_time_bars | 15.2310 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DYDX/USDT P50_144

**Symbol:** DYDX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7831 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9760 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.3933 |
| sortino_ratio | -0.3806 |
| max_drawdown | 0.3820 |
| cagr | -0.1616 |
| net_avg_win | 71.3642 |
| net_avg_loss | -90.1297 |
| avg_hold_time_bars | 17.3489 |
| exposure | 0.2870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

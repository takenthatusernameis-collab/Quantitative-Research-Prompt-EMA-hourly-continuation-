# EMA Hourly Continuation — ARB/USDT P55_100

**Symbol:** ARB/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.5585 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -4.1419 |
| sortino_ratio | -1.4385 |
| max_drawdown | 0.8223 |
| cagr | -0.4946 |
| net_avg_win | 35.5120 |
| net_avg_loss | -60.4807 |
| avg_hold_time_bars | 5.2554 |
| exposure | 0.1431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

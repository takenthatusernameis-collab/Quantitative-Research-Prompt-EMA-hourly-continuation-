# EMA Hourly Continuation — RLC/USDT P12_100

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0475 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -2.5532 |
| sortino_ratio | -0.8305 |
| max_drawdown | 0.6562 |
| cagr | -0.3307 |
| net_avg_win | 59.3765 |
| net_avg_loss | -84.6873 |
| avg_hold_time_bars | 26.2052 |
| exposure | 0.6385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

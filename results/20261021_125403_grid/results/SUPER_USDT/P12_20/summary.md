# EMA Hourly Continuation — SUPER/USDT P12_20

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7059 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0333 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -2.1950 |
| sortino_ratio | -0.5864 |
| max_drawdown | 0.5144 |
| cagr | -0.2377 |
| net_avg_win | 67.7832 |
| net_avg_loss | -97.1353 |
| avg_hold_time_bars | 4.4454 |
| exposure | 0.0703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

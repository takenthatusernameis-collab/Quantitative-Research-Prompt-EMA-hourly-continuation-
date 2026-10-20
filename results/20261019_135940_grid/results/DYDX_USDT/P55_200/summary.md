# EMA Hourly Continuation — DYDX/USDT P55_200

**Symbol:** DYDX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7914 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0571 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -1.3428 |
| sortino_ratio | -0.3700 |
| max_drawdown | 0.3812 |
| cagr | -0.1591 |
| net_avg_win | 69.7226 |
| net_avg_loss | -93.9713 |
| avg_hold_time_bars | 22.0000 |
| exposure | 0.3720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RUNE/USDT P55_100

**Symbol:** RUNE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.8304 |
| net_win_rate | 0.5350 |
| gross_profit_factor | 1.1187 |
| gross_win_rate | 0.5350 |
| sharpe_ratio | -0.8827 |
| sortino_ratio | -0.2262 |
| max_drawdown | 0.3343 |
| cagr | -0.0996 |
| net_avg_win | 67.5070 |
| net_avg_loss | -93.5410 |
| avg_hold_time_bars | 9.2707 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

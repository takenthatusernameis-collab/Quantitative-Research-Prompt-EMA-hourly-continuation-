# EMA Hourly Continuation — AERO/USDT P12_26

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.8360 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.0967 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -1.0722 |
| sortino_ratio | -0.3232 |
| max_drawdown | 0.3727 |
| cagr | -0.1392 |
| net_avg_win | 69.5139 |
| net_avg_loss | -92.8361 |
| avg_hold_time_bars | 5.4381 |
| exposure | 0.1078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

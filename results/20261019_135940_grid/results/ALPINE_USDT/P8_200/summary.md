# EMA Hourly Continuation — ALPINE/USDT P8_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5180 |
| gross_profit_factor | 1.0857 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -0.9178 |
| sortino_ratio | -0.1942 |
| max_drawdown | 0.2541 |
| cagr | -0.0873 |
| net_avg_win | 76.2519 |
| net_avg_loss | -101.1127 |
| avg_hold_time_bars | 85.2703 |
| exposure | 0.8605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ANKR/USDT P89_100

**Symbol:** ANKR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 162 |
| net_profit_factor | 0.5343 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8272 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -2.6194 |
| sortino_ratio | -0.4777 |
| max_drawdown | 0.4347 |
| cagr | -0.1991 |
| net_avg_win | 68.0967 |
| net_avg_loss | -101.9639 |
| avg_hold_time_bars | 13.1358 |
| exposure | 0.0967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

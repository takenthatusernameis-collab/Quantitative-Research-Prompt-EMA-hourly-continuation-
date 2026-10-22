# EMA Hourly Continuation — CATI/USDT P20_100

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.6518 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8021 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -2.8435 |
| sortino_ratio | -0.8611 |
| max_drawdown | 0.6006 |
| cagr | -0.3296 |
| net_avg_win | 61.8688 |
| net_avg_loss | -78.0312 |
| avg_hold_time_bars | 20.5620 |
| exposure | 0.4272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

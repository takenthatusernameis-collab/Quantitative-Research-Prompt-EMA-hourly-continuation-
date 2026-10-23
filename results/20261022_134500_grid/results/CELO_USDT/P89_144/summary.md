# EMA Hourly Continuation — CELO/USDT P89_144

**Symbol:** CELO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.4805 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.8184 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -4.8400 |
| sortino_ratio | -1.4539 |
| max_drawdown | 0.8310 |
| cagr | -0.5046 |
| net_avg_win | 39.3748 |
| net_avg_loss | -61.9314 |
| avg_hold_time_bars | 5.8366 |
| exposure | 0.1196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

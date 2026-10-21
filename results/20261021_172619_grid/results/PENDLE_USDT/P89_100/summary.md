# EMA Hourly Continuation — PENDLE/USDT P89_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 105 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9278 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.0667 |
| sortino_ratio | -0.1565 |
| max_drawdown | 0.1896 |
| cagr | -0.0691 |
| net_avg_win | 76.4235 |
| net_avg_loss | -102.6513 |
| avg_hold_time_bars | 4.2762 |
| exposure | 0.0204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

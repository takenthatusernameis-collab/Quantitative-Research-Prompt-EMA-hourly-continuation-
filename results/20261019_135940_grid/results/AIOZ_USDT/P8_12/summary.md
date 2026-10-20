# EMA Hourly Continuation — AIOZ/USDT P8_12

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1910 |
| net_profit_factor | 0.3277 |
| net_win_rate | 0.3613 |
| gross_profit_factor | 0.7511 |
| gross_win_rate | 0.4026 |
| sharpe_ratio | -17.4789 |
| sortino_ratio | -10.9374 |
| max_drawdown | 1.0000 |
| cagr | -0.9969 |
| net_avg_win | 7.0657 |
| net_avg_loss | -12.1929 |
| avg_hold_time_bars | 1.8215 |
| exposure | 0.1581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

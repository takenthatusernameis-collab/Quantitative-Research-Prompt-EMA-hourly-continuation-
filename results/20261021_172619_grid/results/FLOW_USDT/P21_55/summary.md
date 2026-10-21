# EMA Hourly Continuation — FLOW/USDT P21_55

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6703 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9209 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -3.1498 |
| sortino_ratio | -1.0446 |
| max_drawdown | 0.7139 |
| cagr | -0.3810 |
| net_avg_win | 56.0513 |
| net_avg_loss | -74.2620 |
| avg_hold_time_bars | 8.0019 |
| exposure | 0.1964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

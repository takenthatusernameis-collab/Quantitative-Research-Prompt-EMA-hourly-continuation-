# EMA Hourly Continuation — DOGE/USDT P50_144

**Symbol:** DOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.5727 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9665 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -3.9487 |
| sortino_ratio | -1.2231 |
| max_drawdown | 0.7858 |
| cagr | -0.4491 |
| net_avg_win | 44.2701 |
| net_avg_loss | -71.5183 |
| avg_hold_time_bars | 12.6708 |
| exposure | 0.2816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

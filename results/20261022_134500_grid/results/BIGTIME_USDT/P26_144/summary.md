# EMA Hourly Continuation — BIGTIME/USDT P26_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.8231 |
| net_win_rate | 0.5245 |
| gross_profit_factor | 1.1184 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -1.3990 |
| sortino_ratio | -0.4294 |
| max_drawdown | 0.4620 |
| cagr | -0.1844 |
| net_avg_win | 76.0318 |
| net_avg_loss | -101.8995 |
| avg_hold_time_bars | 23.2068 |
| exposure | 0.4925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — FLIP/USDT P26_144

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.5381 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7758 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -3.7913 |
| sortino_ratio | -1.0395 |
| max_drawdown | 0.7185 |
| cagr | -0.3900 |
| net_avg_win | 49.8990 |
| net_avg_loss | -71.9309 |
| avg_hold_time_bars | 26.8947 |
| exposure | 0.4645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

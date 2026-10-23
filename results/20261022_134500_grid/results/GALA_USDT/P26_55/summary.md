# EMA Hourly Continuation — GALA/USDT P26_55

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.4569 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.7930 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -7.7258 |
| sortino_ratio | -3.3961 |
| max_drawdown | 0.9857 |
| cagr | -0.8080 |
| net_avg_win | 19.8046 |
| net_avg_loss | -33.0051 |
| avg_hold_time_bars | 3.9524 |
| exposure | 0.1737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — AUCTION/USDT P26_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6094 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -3.9301 |
| sortino_ratio | -1.3075 |
| max_drawdown | 0.7954 |
| cagr | -0.4571 |
| net_avg_win | 47.3255 |
| net_avg_loss | -69.3602 |
| avg_hold_time_bars | 7.7832 |
| exposure | 0.1934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

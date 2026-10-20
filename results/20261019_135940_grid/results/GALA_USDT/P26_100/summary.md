# EMA Hourly Continuation — GALA/USDT P26_100

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5924 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8753 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -4.0829 |
| sortino_ratio | -1.4456 |
| max_drawdown | 0.8327 |
| cagr | -0.4989 |
| net_avg_win | 40.4465 |
| net_avg_loss | -59.6123 |
| avg_hold_time_bars | 12.6929 |
| exposure | 0.3664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

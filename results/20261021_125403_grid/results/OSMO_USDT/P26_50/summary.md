# EMA Hourly Continuation — OSMO/USDT P26_50

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6028 |
| net_win_rate | 0.4461 |
| gross_profit_factor | 0.8720 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -3.8800 |
| sortino_ratio | -1.1931 |
| max_drawdown | 0.7544 |
| cagr | -0.4229 |
| net_avg_win | 54.8729 |
| net_avg_loss | -73.3226 |
| avg_hold_time_bars | 7.0560 |
| exposure | 0.1488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

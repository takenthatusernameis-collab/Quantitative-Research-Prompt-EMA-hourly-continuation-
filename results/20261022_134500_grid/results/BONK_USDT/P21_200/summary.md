# EMA Hourly Continuation — BONK/USDT P21_200

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6884 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9725 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -2.3640 |
| sortino_ratio | -0.6382 |
| max_drawdown | 0.6057 |
| cagr | -0.2691 |
| net_avg_win | 66.1601 |
| net_avg_loss | -90.1576 |
| avg_hold_time_bars | 37.0665 |
| exposure | 0.6335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

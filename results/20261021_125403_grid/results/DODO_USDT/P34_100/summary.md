# EMA Hourly Continuation — DODO/USDT P34_100

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7542 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -2.0545 |
| sortino_ratio | -0.6383 |
| max_drawdown | 0.5538 |
| cagr | -0.2538 |
| net_avg_win | 68.7699 |
| net_avg_loss | -88.1564 |
| avg_hold_time_bars | 11.1835 |
| exposure | 0.2399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

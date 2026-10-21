# EMA Hourly Continuation — ATOM/USDT P34_100

**Symbol:** ATOM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 0.9691 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.5907 |
| sortino_ratio | -0.4461 |
| max_drawdown | 0.4507 |
| cagr | -0.1857 |
| net_avg_win | 59.4779 |
| net_avg_loss | -81.3209 |
| avg_hold_time_bars | 15.0000 |
| exposure | 0.2605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

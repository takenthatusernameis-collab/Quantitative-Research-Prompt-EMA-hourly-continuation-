# EMA Hourly Continuation — GTC/USDT P20_34

**Symbol:** GTC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6106 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8610 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -3.3612 |
| sortino_ratio | -1.0159 |
| max_drawdown | 0.7059 |
| cagr | -0.3723 |
| net_avg_win | 52.2294 |
| net_avg_loss | -73.4695 |
| avg_hold_time_bars | 5.5379 |
| exposure | 0.1128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

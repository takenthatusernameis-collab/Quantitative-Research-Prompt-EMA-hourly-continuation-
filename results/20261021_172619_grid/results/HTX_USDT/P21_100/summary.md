# EMA Hourly Continuation — HTX/USDT P21_100

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.5599 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8917 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -5.0319 |
| sortino_ratio | -1.5511 |
| max_drawdown | 0.8495 |
| cagr | -0.5195 |
| net_avg_win | 52.5381 |
| net_avg_loss | -73.6276 |
| avg_hold_time_bars | 20.9526 |
| exposure | 0.4399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

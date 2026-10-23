# EMA Hourly Continuation — SAFE/USDT P55_100

**Symbol:** SAFE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.5453 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.9117 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -4.5217 |
| sortino_ratio | -1.5399 |
| max_drawdown | 0.8487 |
| cagr | -0.5208 |
| net_avg_win | 37.4629 |
| net_avg_loss | -59.9976 |
| avg_hold_time_bars | 6.9827 |
| exposure | 0.1845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

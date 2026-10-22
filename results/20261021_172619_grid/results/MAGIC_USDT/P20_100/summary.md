# EMA Hourly Continuation — MAGIC/USDT P20_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.8453 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0703 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.2646 |
| sortino_ratio | -0.4005 |
| max_drawdown | 0.4305 |
| cagr | -0.1702 |
| net_avg_win | 81.4050 |
| net_avg_loss | -102.4279 |
| avg_hold_time_bars | 21.5934 |
| exposure | 0.4780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

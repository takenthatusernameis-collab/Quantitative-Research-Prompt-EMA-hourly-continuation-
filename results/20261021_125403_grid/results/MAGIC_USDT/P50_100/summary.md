# EMA Hourly Continuation — MAGIC/USDT P50_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.7561 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.9389 |
| sortino_ratio | -0.5601 |
| max_drawdown | 0.4950 |
| cagr | -0.2270 |
| net_avg_win | 72.7361 |
| net_avg_loss | -96.1945 |
| avg_hold_time_bars | 8.9286 |
| exposure | 0.1648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

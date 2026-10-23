# EMA Hourly Continuation — ALPINE/USDT P100_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.5333 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -4.1362 |
| sortino_ratio | -1.2339 |
| max_drawdown | 0.7724 |
| cagr | -0.4414 |
| net_avg_win | 43.0325 |
| net_avg_loss | -69.7551 |
| avg_hold_time_bars | 11.3136 |
| exposure | 0.2263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

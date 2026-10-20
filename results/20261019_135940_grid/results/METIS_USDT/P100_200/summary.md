# EMA Hourly Continuation — METIS/USDT P100_200

**Symbol:** METIS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.5513 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.8173 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -3.8167 |
| sortino_ratio | -1.0665 |
| max_drawdown | 0.7273 |
| cagr | -0.4012 |
| net_avg_win | 51.1283 |
| net_avg_loss | -72.6923 |
| avg_hold_time_bars | 10.2626 |
| exposure | 0.1847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RENDER/USDT P26_200

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 1.0213 |
| net_win_rate | 0.5463 |
| gross_profit_factor | 1.1837 |
| gross_win_rate | 0.5463 |
| sharpe_ratio | 0.1602 |
| sortino_ratio | 0.0376 |
| max_drawdown | 0.1097 |
| cagr | 0.0112 |
| net_avg_win | 94.2391 |
| net_avg_loss | -111.0814 |
| avg_hold_time_bars | 48.3436 |
| exposure | 0.5792 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

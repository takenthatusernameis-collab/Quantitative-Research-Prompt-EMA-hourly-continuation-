# EMA Hourly Continuation — PUFFER/USDT P26_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 1.0037 |
| net_win_rate | 0.5342 |
| gross_profit_factor | 1.1423 |
| gross_win_rate | 0.5342 |
| sharpe_ratio | 0.0726 |
| sortino_ratio | 0.0179 |
| max_drawdown | 0.1501 |
| cagr | 0.0020 |
| net_avg_win | 88.3269 |
| net_avg_loss | -100.9200 |
| avg_hold_time_bars | 42.1239 |
| exposure | 0.5578 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CELO/USDT P50_200

**Symbol:** CELO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 1.0146 |
| net_win_rate | 0.5559 |
| gross_profit_factor | 1.2465 |
| gross_win_rate | 0.5559 |
| sharpe_ratio | 0.1384 |
| sortino_ratio | 0.0345 |
| max_drawdown | 0.2108 |
| cagr | 0.0091 |
| net_avg_win | 98.5806 |
| net_avg_loss | -121.6408 |
| avg_hold_time_bars | 29.7424 |
| exposure | 0.3970 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

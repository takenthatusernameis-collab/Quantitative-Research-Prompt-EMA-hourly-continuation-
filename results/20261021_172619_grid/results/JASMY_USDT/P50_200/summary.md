# EMA Hourly Continuation — JASMY/USDT P50_200

**Symbol:** JASMY/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 1.2194 |
| net_win_rate | 0.5939 |
| gross_profit_factor | 1.4593 |
| gross_win_rate | 0.5939 |
| sharpe_ratio | 1.0248 |
| sortino_ratio | 0.2446 |
| max_drawdown | 0.1369 |
| cagr | 0.1036 |
| net_avg_win | 100.7242 |
| net_avg_loss | -120.7831 |
| avg_hold_time_bars | 35.3602 |
| exposure | 0.4195 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

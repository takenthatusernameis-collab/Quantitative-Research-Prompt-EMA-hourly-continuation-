# EMA Hourly Continuation — JASMY/USDT P55_200

**Symbol:** JASMY/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 1.1982 |
| net_win_rate | 0.5923 |
| gross_profit_factor | 1.4438 |
| gross_win_rate | 0.5923 |
| sharpe_ratio | 1.0040 |
| sortino_ratio | 0.2511 |
| max_drawdown | 0.1217 |
| cagr | 0.1062 |
| net_avg_win | 102.5728 |
| net_avg_loss | -124.3888 |
| avg_hold_time_bars | 28.0105 |
| exposure | 0.3654 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

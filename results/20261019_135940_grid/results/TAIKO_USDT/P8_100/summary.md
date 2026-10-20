# EMA Hourly Continuation — TAIKO/USDT P8_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.6674 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 1.0011 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -3.4281 |
| sortino_ratio | -1.2290 |
| max_drawdown | 0.7869 |
| cagr | -0.4481 |
| net_avg_win | 50.2548 |
| net_avg_loss | -71.7415 |
| avg_hold_time_bars | 22.6882 |
| exposure | 0.6746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

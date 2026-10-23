# EMA Hourly Continuation — SAFE/USDT P20_200

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7140 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9942 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.9552 |
| sortino_ratio | -0.5410 |
| max_drawdown | 0.4999 |
| cagr | -0.2265 |
| net_avg_win | 62.4411 |
| net_avg_loss | -86.0884 |
| avg_hold_time_bars | 36.7769 |
| exposure | 0.6417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

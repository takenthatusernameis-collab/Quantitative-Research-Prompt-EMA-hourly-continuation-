# EMA Hourly Continuation — JASMY/USDT P34_100

**Symbol:** JASMY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.6383 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -3.5400 |
| sortino_ratio | -1.2957 |
| max_drawdown | 0.8079 |
| cagr | -0.4602 |
| net_avg_win | 41.6019 |
| net_avg_loss | -64.0272 |
| avg_hold_time_bars | 8.1736 |
| exposure | 0.2504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

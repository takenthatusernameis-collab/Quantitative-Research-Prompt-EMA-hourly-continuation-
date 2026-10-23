# EMA Hourly Continuation — ALEX/USDT P26_55

**Symbol:** ALEX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.4464 |
| net_win_rate | 0.3767 |
| gross_profit_factor | 0.7958 |
| gross_win_rate | 0.3979 |
| sharpe_ratio | -8.3881 |
| sortino_ratio | -3.2275 |
| max_drawdown | 0.9845 |
| cagr | -0.8053 |
| net_avg_win | 27.9232 |
| net_avg_loss | -37.7999 |
| avg_hold_time_bars | 6.8674 |
| exposure | 0.2354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

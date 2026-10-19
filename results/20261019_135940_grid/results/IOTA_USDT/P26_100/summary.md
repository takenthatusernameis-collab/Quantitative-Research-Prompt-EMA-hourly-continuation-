# EMA Hourly Continuation — IOTA/USDT P26_100

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5381 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -5.1995 |
| sortino_ratio | -1.8531 |
| max_drawdown | 0.9048 |
| cagr | -0.5989 |
| net_avg_win | 35.8684 |
| net_avg_loss | -53.4765 |
| avg_hold_time_bars | 11.8171 |
| exposure | 0.3524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

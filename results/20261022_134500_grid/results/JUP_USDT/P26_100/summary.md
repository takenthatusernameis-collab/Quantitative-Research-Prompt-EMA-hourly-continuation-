# EMA Hourly Continuation — JUP/USDT P26_100

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5532 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8224 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -4.7733 |
| sortino_ratio | -1.7461 |
| max_drawdown | 0.8871 |
| cagr | -0.5697 |
| net_avg_win | 35.5915 |
| net_avg_loss | -52.6415 |
| avg_hold_time_bars | 10.5441 |
| exposure | 0.3259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

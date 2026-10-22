# EMA Hourly Continuation — MLK/USDT P20_100

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.4965 |
| net_win_rate | 0.3698 |
| gross_profit_factor | 0.6598 |
| gross_win_rate | 0.3718 |
| sharpe_ratio | -5.5196 |
| sortino_ratio | -1.7422 |
| max_drawdown | 0.8730 |
| cagr | -0.5552 |
| net_avg_win | 46.1494 |
| net_avg_loss | -54.5360 |
| avg_hold_time_bars | 15.3141 |
| exposure | 0.3486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

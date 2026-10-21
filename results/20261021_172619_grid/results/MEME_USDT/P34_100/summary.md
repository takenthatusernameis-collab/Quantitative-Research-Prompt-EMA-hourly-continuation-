# EMA Hourly Continuation — MEME/USDT P34_100

**Symbol:** MEME/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7683 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.7322 |
| sortino_ratio | -0.5150 |
| max_drawdown | 0.4979 |
| cagr | -0.2114 |
| net_avg_win | 69.9420 |
| net_avg_loss | -88.5405 |
| avg_hold_time_bars | 13.6898 |
| exposure | 0.2688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

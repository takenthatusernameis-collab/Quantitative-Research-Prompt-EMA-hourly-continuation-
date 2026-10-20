# EMA Hourly Continuation — MEME/USDT P55_100

**Symbol:** MEME/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.5423 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8770 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -4.8449 |
| sortino_ratio | -1.7323 |
| max_drawdown | 0.8802 |
| cagr | -0.5687 |
| net_avg_win | 34.7157 |
| net_avg_loss | -55.6649 |
| avg_hold_time_bars | 5.6698 |
| exposure | 0.1662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

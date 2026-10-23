# EMA Hourly Continuation — MEME/USDT P12_20

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1480 |
| net_profit_factor | 0.3121 |
| net_win_rate | 0.4061 |
| gross_profit_factor | 0.7571 |
| gross_win_rate | 0.4318 |
| sharpe_ratio | -12.3589 |
| sortino_ratio | -6.7612 |
| max_drawdown | 0.9998 |
| cagr | -0.9664 |
| net_avg_win | 7.5473 |
| net_avg_loss | -16.5346 |
| avg_hold_time_bars | 2.4345 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

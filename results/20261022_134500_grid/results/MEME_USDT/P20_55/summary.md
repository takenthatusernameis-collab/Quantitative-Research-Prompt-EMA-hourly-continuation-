# EMA Hourly Continuation — MEME/USDT P20_55

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.5642 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -6.4351 |
| sortino_ratio | -2.8759 |
| max_drawdown | 0.9723 |
| cagr | -0.7504 |
| net_avg_win | 27.3969 |
| net_avg_loss | -40.0745 |
| avg_hold_time_bars | 5.1767 |
| exposure | 0.2384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

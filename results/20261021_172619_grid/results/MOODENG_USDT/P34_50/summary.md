# EMA Hourly Continuation — MOODENG/USDT P34_50

**Symbol:** MOODENG/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -2.5516 |
| sortino_ratio | -0.6289 |
| max_drawdown | 0.4695 |
| cagr | -0.2510 |
| net_avg_win | 69.3836 |
| net_avg_loss | -92.7153 |
| avg_hold_time_bars | 5.3415 |
| exposure | 0.0727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

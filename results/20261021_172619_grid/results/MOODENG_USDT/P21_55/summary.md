# EMA Hourly Continuation — MOODENG/USDT P21_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7845 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9769 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.9465 |
| sortino_ratio | -0.6385 |
| max_drawdown | 0.5061 |
| cagr | -0.2558 |
| net_avg_win | 77.9696 |
| net_avg_loss | -96.2314 |
| avg_hold_time_bars | 8.7921 |
| exposure | 0.2106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

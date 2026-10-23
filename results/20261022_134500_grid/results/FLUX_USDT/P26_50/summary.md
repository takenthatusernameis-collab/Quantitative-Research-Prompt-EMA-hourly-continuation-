# EMA Hourly Continuation — FLUX/USDT P26_50

**Symbol:** FLUX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.4595 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -7.2736 |
| sortino_ratio | -3.1323 |
| max_drawdown | 0.9807 |
| cagr | -0.7904 |
| net_avg_win | 19.0666 |
| net_avg_loss | -35.9814 |
| avg_hold_time_bars | 3.3369 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — AIOZ/USDT P8_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.8046 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9783 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.9760 |
| sortino_ratio | -0.7574 |
| max_drawdown | 0.6418 |
| cagr | -0.2960 |
| net_avg_win | 67.9737 |
| net_avg_loss | -82.3874 |
| avg_hold_time_bars | 12.3366 |
| exposure | 0.4032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

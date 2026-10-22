# EMA Hourly Continuation — JUP/USDT P89_100

**Symbol:** JUP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.2298 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.6106 |
| gross_win_rate | 0.3805 |
| sharpe_ratio | -9.7532 |
| sortino_ratio | -3.4405 |
| max_drawdown | 0.9897 |
| cagr | -0.8370 |
| net_avg_win | 13.6682 |
| net_avg_loss | -33.9875 |
| avg_hold_time_bars | 1.8316 |
| exposure | 0.0495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

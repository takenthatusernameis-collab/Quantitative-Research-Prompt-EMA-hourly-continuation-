# EMA Hourly Continuation — DEEP/USDT P21_50

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.8650 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0780 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.9668 |
| sortino_ratio | -0.3043 |
| max_drawdown | 0.2737 |
| cagr | -0.1337 |
| net_avg_win | 80.5158 |
| net_avg_loss | -101.1702 |
| avg_hold_time_bars | 7.1224 |
| exposure | 0.1549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

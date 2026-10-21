# EMA Hourly Continuation — EIGEN/USDT P26_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8196 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -1.2616 |
| sortino_ratio | -0.3847 |
| max_drawdown | 0.3279 |
| cagr | -0.1640 |
| net_avg_win | 75.9023 |
| net_avg_loss | -91.1244 |
| avg_hold_time_bars | 12.9434 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

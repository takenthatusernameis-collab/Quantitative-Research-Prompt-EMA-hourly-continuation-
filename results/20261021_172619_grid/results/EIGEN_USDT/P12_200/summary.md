# EMA Hourly Continuation — EIGEN/USDT P12_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.9364 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0526 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -0.2981 |
| sortino_ratio | -0.0704 |
| max_drawdown | 0.1698 |
| cagr | -0.0356 |
| net_avg_win | 93.3073 |
| net_avg_loss | -105.2284 |
| avg_hold_time_bars | 61.9273 |
| exposure | 0.7581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

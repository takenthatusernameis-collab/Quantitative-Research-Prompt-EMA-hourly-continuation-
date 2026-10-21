# EMA Hourly Continuation — EIGEN/USDT P20_21

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.7750 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9948 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9527 |
| sortino_ratio | -0.1641 |
| max_drawdown | 0.1914 |
| cagr | -0.0732 |
| net_avg_win | 84.3246 |
| net_avg_loss | -108.8034 |
| avg_hold_time_bars | 4.6441 |
| exposure | 0.0305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

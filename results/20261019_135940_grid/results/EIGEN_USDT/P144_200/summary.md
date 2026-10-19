# EMA Hourly Continuation — EIGEN/USDT P144_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.5836 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9436 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -3.5823 |
| sortino_ratio | -1.0363 |
| max_drawdown | 0.6415 |
| cagr | -0.3935 |
| net_avg_win | 54.8319 |
| net_avg_loss | -84.6559 |
| avg_hold_time_bars | 3.8121 |
| exposure | 0.0734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

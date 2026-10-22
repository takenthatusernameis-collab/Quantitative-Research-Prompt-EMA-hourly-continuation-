# EMA Hourly Continuation — EIGEN/USDT P55_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.5541 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -4.8172 |
| sortino_ratio | -1.8284 |
| max_drawdown | 0.8402 |
| cagr | -0.5861 |
| net_avg_win | 36.9885 |
| net_avg_loss | -60.7011 |
| avg_hold_time_bars | 3.8186 |
| exposure | 0.1254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

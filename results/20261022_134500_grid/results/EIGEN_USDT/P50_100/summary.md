# EMA Hourly Continuation — EIGEN/USDT P50_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6126 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -4.3959 |
| sortino_ratio | -1.5607 |
| max_drawdown | 0.7965 |
| cagr | -0.5398 |
| net_avg_win | 50.3740 |
| net_avg_loss | -73.4224 |
| avg_hold_time_bars | 6.1264 |
| exposure | 0.1807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — EIGEN/USDT P21_26

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.7549 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9579 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.0682 |
| sortino_ratio | -0.1914 |
| max_drawdown | 0.2029 |
| cagr | -0.0846 |
| net_avg_win | 81.0328 |
| net_avg_loss | -104.0442 |
| avg_hold_time_bars | 5.6719 |
| exposure | 0.0404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — EIGEN/USDT P34_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.8956 |
| net_win_rate | 0.5343 |
| gross_profit_factor | 1.1388 |
| gross_win_rate | 0.5343 |
| sharpe_ratio | -0.5231 |
| sortino_ratio | -0.1195 |
| max_drawdown | 0.2457 |
| cagr | -0.0557 |
| net_avg_win | 87.2959 |
| net_avg_loss | -111.8410 |
| avg_hold_time_bars | 5.3137 |
| exposure | 0.0603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

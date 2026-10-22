# EMA Hourly Continuation — EIGEN/USDT P12_20

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.4287 |
| net_win_rate | 0.4160 |
| gross_profit_factor | 0.8005 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -11.4267 |
| sortino_ratio | -6.1802 |
| max_drawdown | 0.9984 |
| cagr | -0.9564 |
| net_avg_win | 14.9851 |
| net_avg_loss | -24.8951 |
| avg_hold_time_bars | 2.0799 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

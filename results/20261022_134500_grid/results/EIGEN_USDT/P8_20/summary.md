# EMA Hourly Continuation — EIGEN/USDT P8_20

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1389 |
| net_profit_factor | 0.5248 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -9.8868 |
| sortino_ratio | -5.7219 |
| max_drawdown | 0.9971 |
| cagr | -0.9410 |
| net_avg_win | 17.8458 |
| net_avg_loss | -27.1771 |
| avg_hold_time_bars | 2.5644 |
| exposure | 0.1982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

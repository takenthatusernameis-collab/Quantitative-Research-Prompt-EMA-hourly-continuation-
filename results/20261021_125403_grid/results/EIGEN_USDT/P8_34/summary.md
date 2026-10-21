# EMA Hourly Continuation — EIGEN/USDT P8_34

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.7625 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -2.1698 |
| sortino_ratio | -0.8345 |
| max_drawdown | 0.5723 |
| cagr | -0.3199 |
| net_avg_win | 60.9179 |
| net_avg_loss | -75.4407 |
| avg_hold_time_bars | 8.7841 |
| exposure | 0.2899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

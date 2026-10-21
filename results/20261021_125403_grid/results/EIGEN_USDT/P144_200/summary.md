# EMA Hourly Continuation — EIGEN/USDT P144_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.6945 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -1.7025 |
| sortino_ratio | -0.3560 |
| max_drawdown | 0.3124 |
| cagr | -0.1507 |
| net_avg_win | 78.9453 |
| net_avg_loss | -99.1639 |
| avg_hold_time_bars | 5.7102 |
| exposure | 0.0559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

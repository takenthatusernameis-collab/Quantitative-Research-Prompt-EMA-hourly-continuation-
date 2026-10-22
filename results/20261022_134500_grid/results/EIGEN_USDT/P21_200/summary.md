# EMA Hourly Continuation — EIGEN/USDT P21_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8545 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.0824 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -1.0159 |
| sortino_ratio | -0.2883 |
| max_drawdown | 0.3450 |
| cagr | -0.1286 |
| net_avg_win | 86.0157 |
| net_avg_loss | -108.4006 |
| avg_hold_time_bars | 33.1574 |
| exposure | 0.5978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

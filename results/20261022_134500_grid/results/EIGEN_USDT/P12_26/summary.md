# EMA Hourly Continuation — EIGEN/USDT P12_26

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1137 |
| net_profit_factor | 0.5163 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -8.8427 |
| sortino_ratio | -4.6221 |
| max_drawdown | 0.9916 |
| cagr | -0.8989 |
| net_avg_win | 21.2359 |
| net_avg_loss | -32.0572 |
| avg_hold_time_bars | 2.7792 |
| exposure | 0.1758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

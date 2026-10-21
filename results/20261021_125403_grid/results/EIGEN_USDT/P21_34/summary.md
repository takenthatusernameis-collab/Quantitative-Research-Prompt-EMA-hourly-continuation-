# EMA Hourly Continuation — EIGEN/USDT P21_34

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0250 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -1.0271 |
| sortino_ratio | -0.2514 |
| max_drawdown | 0.3210 |
| cagr | -0.1103 |
| net_avg_win | 77.3366 |
| net_avg_loss | -99.0455 |
| avg_hold_time_bars | 5.7890 |
| exposure | 0.0763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

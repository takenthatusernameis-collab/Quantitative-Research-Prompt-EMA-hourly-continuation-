# EMA Hourly Continuation — EIGEN/USDT P34_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8843 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -0.6678 |
| sortino_ratio | -0.1740 |
| max_drawdown | 0.2355 |
| cagr | -0.0800 |
| net_avg_win | 88.3927 |
| net_avg_loss | -101.4488 |
| avg_hold_time_bars | 30.0444 |
| exposure | 0.4514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

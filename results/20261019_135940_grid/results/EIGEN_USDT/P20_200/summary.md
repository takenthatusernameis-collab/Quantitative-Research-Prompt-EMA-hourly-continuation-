# EMA Hourly Continuation — EIGEN/USDT P20_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.8574 |
| net_win_rate | 0.5210 |
| gross_profit_factor | 1.0911 |
| gross_win_rate | 0.5210 |
| sharpe_ratio | -0.9952 |
| sortino_ratio | -0.2867 |
| max_drawdown | 0.3447 |
| cagr | -0.1282 |
| net_avg_win | 84.7556 |
| net_avg_loss | -107.5002 |
| avg_hold_time_bars | 32.5629 |
| exposure | 0.6052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

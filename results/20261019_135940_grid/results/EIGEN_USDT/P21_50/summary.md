# EMA Hourly Continuation — EIGEN/USDT P21_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.5720 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.8793 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.4833 |
| sortino_ratio | -2.4018 |
| max_drawdown | 0.9049 |
| cagr | -0.6824 |
| net_avg_win | 32.9466 |
| net_avg_loss | -50.4546 |
| avg_hold_time_bars | 4.6399 |
| exposure | 0.2029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

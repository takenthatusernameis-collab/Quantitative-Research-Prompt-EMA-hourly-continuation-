# EMA Hourly Continuation — EIGEN/USDT P12_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.9234 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0668 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -0.5037 |
| sortino_ratio | -0.1521 |
| max_drawdown | 0.2652 |
| cagr | -0.0728 |
| net_avg_win | 93.0915 |
| net_avg_loss | -107.7653 |
| avg_hold_time_bars | 28.3389 |
| exposure | 0.5677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

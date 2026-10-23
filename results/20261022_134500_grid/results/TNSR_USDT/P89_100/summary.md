# EMA Hourly Continuation — TNSR/USDT P89_100

**Symbol:** TNSR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.3826 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.8279 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -7.3078 |
| sortino_ratio | -2.5165 |
| max_drawdown | 0.9598 |
| cagr | -0.7184 |
| net_avg_win | 24.1647 |
| net_avg_loss | -45.9631 |
| avg_hold_time_bars | 2.4024 |
| exposure | 0.0635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — VR/USDT P21_50

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.5378 |
| sortino_ratio | -0.6596 |
| max_drawdown | 0.5435 |
| cagr | -0.2635 |
| net_avg_win | 67.2287 |
| net_avg_loss | -89.4106 |
| avg_hold_time_bars | 12.1701 |
| exposure | 0.1853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ANKR/USDT P21_200

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.6724 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -2.6048 |
| sortino_ratio | -0.6953 |
| max_drawdown | 0.5720 |
| cagr | -0.2794 |
| net_avg_win | 68.5152 |
| net_avg_loss | -91.5455 |
| avg_hold_time_bars | 42.5606 |
| exposure | 0.6868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

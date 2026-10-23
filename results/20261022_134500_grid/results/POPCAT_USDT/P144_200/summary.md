# EMA Hourly Continuation — POPCAT/USDT P144_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5685 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8946 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -3.6665 |
| sortino_ratio | -1.0487 |
| max_drawdown | 0.6742 |
| cagr | -0.3957 |
| net_avg_win | 52.6466 |
| net_avg_loss | -81.3319 |
| avg_hold_time_bars | 4.3887 |
| exposure | 0.0823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

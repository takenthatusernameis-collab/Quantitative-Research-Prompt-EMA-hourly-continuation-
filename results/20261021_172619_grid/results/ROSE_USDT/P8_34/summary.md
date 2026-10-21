# EMA Hourly Continuation — ROSE/USDT P8_34

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.7665 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.2501 |
| sortino_ratio | -0.8982 |
| max_drawdown | 0.6586 |
| cagr | -0.3383 |
| net_avg_win | 54.7589 |
| net_avg_loss | -71.0726 |
| avg_hold_time_bars | 8.3621 |
| exposure | 0.2950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

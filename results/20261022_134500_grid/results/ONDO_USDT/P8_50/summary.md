# EMA Hourly Continuation — ONDO/USDT P8_50

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1156 |
| net_profit_factor | 0.5928 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9268 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -5.8964 |
| sortino_ratio | -2.8025 |
| max_drawdown | 0.9693 |
| cagr | -0.7457 |
| net_avg_win | 25.8084 |
| net_avg_loss | -38.9676 |
| avg_hold_time_bars | 8.1687 |
| exposure | 0.4292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

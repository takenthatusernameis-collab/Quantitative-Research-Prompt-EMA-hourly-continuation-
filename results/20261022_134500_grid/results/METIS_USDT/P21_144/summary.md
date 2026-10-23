# EMA Hourly Continuation — METIS/USDT P21_144

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5850 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8372 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -4.0918 |
| sortino_ratio | -1.2920 |
| max_drawdown | 0.7952 |
| cagr | -0.4671 |
| net_avg_win | 49.5387 |
| net_avg_loss | -66.6819 |
| avg_hold_time_bars | 22.3372 |
| exposure | 0.5209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

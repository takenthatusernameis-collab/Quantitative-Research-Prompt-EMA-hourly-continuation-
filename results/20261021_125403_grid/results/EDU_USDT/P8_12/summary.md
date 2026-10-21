# EMA Hourly Continuation — EDU/USDT P8_12

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.5669 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8207 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -3.8918 |
| sortino_ratio | -1.2025 |
| max_drawdown | 0.7529 |
| cagr | -0.4254 |
| net_avg_win | 46.7101 |
| net_avg_loss | -66.8633 |
| avg_hold_time_bars | 4.4947 |
| exposure | 0.0958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

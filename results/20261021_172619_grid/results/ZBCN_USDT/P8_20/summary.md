# EMA Hourly Continuation — ZBCN/USDT P8_20

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.9070 |
| net_win_rate | 0.5337 |
| gross_profit_factor | 1.1304 |
| gross_win_rate | 0.5337 |
| sharpe_ratio | -0.5354 |
| sortino_ratio | -0.1563 |
| max_drawdown | 0.2380 |
| cagr | -0.0737 |
| net_avg_win | 78.4653 |
| net_avg_loss | -98.9977 |
| avg_hold_time_bars | 6.1372 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

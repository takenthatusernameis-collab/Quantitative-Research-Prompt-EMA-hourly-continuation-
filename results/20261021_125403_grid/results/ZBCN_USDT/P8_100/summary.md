# EMA Hourly Continuation — ZBCN/USDT P8_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.9602 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1064 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.2384 |
| sortino_ratio | -0.0812 |
| max_drawdown | 0.2643 |
| cagr | -0.0456 |
| net_avg_win | 90.6167 |
| net_avg_loss | -105.6640 |
| avg_hold_time_bars | 23.0055 |
| exposure | 0.5843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DEEP/USDT P50_55

**Symbol:** DEEP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 88 |
| net_profit_factor | 0.9015 |
| net_win_rate | 0.5568 |
| gross_profit_factor | 1.2449 |
| gross_win_rate | 0.5568 |
| sharpe_ratio | -0.3106 |
| sortino_ratio | -0.0471 |
| max_drawdown | 0.0871 |
| cagr | -0.0225 |
| net_avg_win | 83.8784 |
| net_avg_loss | -116.8973 |
| avg_hold_time_bars | 4.6818 |
| exposure | 0.0233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

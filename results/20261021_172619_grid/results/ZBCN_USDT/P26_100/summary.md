# EMA Hourly Continuation — ZBCN/USDT P26_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8551 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.0462 |
| sortino_ratio | -0.3302 |
| max_drawdown | 0.3821 |
| cagr | -0.1438 |
| net_avg_win | 77.9435 |
| net_avg_loss | -93.0787 |
| avg_hold_time_bars | 11.8239 |
| exposure | 0.2609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

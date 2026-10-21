# EMA Hourly Continuation — EGLD/USDT P8_100

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.8427 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0486 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.2524 |
| sortino_ratio | -0.4005 |
| max_drawdown | 0.4897 |
| cagr | -0.1699 |
| net_avg_win | 79.0964 |
| net_avg_loss | -97.7245 |
| avg_hold_time_bars | 28.8629 |
| exposure | 0.6507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

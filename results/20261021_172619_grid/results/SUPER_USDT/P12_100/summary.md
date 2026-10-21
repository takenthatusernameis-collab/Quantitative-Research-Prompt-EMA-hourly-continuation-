# EMA Hourly Continuation — SUPER/USDT P12_100

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.8585 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0412 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -0.9906 |
| sortino_ratio | -0.3181 |
| max_drawdown | 0.4076 |
| cagr | -0.1391 |
| net_avg_win | 73.9988 |
| net_avg_loss | -91.1609 |
| avg_hold_time_bars | 25.0220 |
| exposure | 0.5687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

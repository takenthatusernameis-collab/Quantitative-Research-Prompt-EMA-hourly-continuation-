# EMA Hourly Continuation — IOTA/USDT P20_100

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7162 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8972 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -2.4600 |
| sortino_ratio | -0.7505 |
| max_drawdown | 0.5996 |
| cagr | -0.2917 |
| net_avg_win | 68.3201 |
| net_avg_loss | -82.9893 |
| avg_hold_time_bars | 20.1609 |
| exposure | 0.4215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

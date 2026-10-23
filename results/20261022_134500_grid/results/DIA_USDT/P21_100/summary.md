# EMA Hourly Continuation — DIA/USDT P21_100

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -4.6132 |
| sortino_ratio | -1.6453 |
| max_drawdown | 0.8750 |
| cagr | -0.5460 |
| net_avg_win | 43.5982 |
| net_avg_loss | -59.8499 |
| avg_hold_time_bars | 14.0508 |
| exposure | 0.4126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

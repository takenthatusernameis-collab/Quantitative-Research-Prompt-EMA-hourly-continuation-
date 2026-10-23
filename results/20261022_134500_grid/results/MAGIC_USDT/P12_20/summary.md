# EMA Hourly Continuation — MAGIC/USDT P12_20

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1391 |
| net_profit_factor | 0.4106 |
| net_win_rate | 0.4206 |
| gross_profit_factor | 0.9544 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -11.3939 |
| sortino_ratio | -6.0350 |
| max_drawdown | 0.9995 |
| cagr | -0.9512 |
| net_avg_win | 11.9011 |
| net_avg_loss | -21.0385 |
| avg_hold_time_bars | 2.9590 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

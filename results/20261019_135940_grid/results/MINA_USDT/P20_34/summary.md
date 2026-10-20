# EMA Hourly Continuation — MINA/USDT P20_34

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1181 |
| net_profit_factor | 0.4129 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -9.6525 |
| sortino_ratio | -4.7290 |
| max_drawdown | 0.9970 |
| cagr | -0.9006 |
| net_avg_win | 13.6405 |
| net_avg_loss | -25.4585 |
| avg_hold_time_bars | 3.0974 |
| exposure | 0.1663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

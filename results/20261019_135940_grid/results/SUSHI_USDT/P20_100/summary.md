# EMA Hourly Continuation — SUSHI/USDT P20_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9109 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -4.6028 |
| sortino_ratio | -1.6742 |
| max_drawdown | 0.8749 |
| cagr | -0.5576 |
| net_avg_win | 42.1052 |
| net_avg_loss | -59.7229 |
| avg_hold_time_bars | 13.9174 |
| exposure | 0.4270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — IOTA/USDT P21_26

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 212 |
| net_profit_factor | 0.6392 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9312 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -2.0632 |
| sortino_ratio | -0.4309 |
| max_drawdown | 0.4149 |
| cagr | -0.1786 |
| net_avg_win | 67.7250 |
| net_avg_loss | -98.2395 |
| avg_hold_time_bars | 4.4434 |
| exposure | 0.0428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

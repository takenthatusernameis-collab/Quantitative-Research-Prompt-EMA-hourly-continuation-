# EMA Hourly Continuation — RUNE/USDT P20_144

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.9379 |
| net_win_rate | 0.5363 |
| gross_profit_factor | 1.1489 |
| gross_win_rate | 0.5363 |
| sharpe_ratio | -0.2921 |
| sortino_ratio | -0.0718 |
| max_drawdown | 0.1651 |
| cagr | -0.0365 |
| net_avg_win | 86.7658 |
| net_avg_loss | -107.0134 |
| avg_hold_time_bars | 48.9654 |
| exposure | 0.6432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

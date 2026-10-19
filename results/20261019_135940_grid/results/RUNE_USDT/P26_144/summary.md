# EMA Hourly Continuation — RUNE/USDT P26_144

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7096 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0134 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -2.0739 |
| sortino_ratio | -0.5975 |
| max_drawdown | 0.5418 |
| cagr | -0.2468 |
| net_avg_win | 58.9659 |
| net_avg_loss | -85.9488 |
| avg_hold_time_bars | 29.1663 |
| exposure | 0.5502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

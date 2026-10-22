# EMA Hourly Continuation — RUNE/USDT P20_26

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1194 |
| net_profit_factor | 0.2339 |
| net_win_rate | 0.3635 |
| gross_profit_factor | 0.6919 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -14.2357 |
| sortino_ratio | -7.1525 |
| max_drawdown | 0.9999 |
| cagr | -0.9780 |
| net_avg_win | 7.0341 |
| net_avg_loss | -17.1738 |
| avg_hold_time_bars | 1.8199 |
| exposure | 0.0988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

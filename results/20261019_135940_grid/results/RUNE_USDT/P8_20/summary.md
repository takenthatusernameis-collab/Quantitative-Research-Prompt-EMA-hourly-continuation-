# EMA Hourly Continuation — RUNE/USDT P8_20

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1657 |
| net_profit_factor | 0.3613 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.8250 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -13.7898 |
| sortino_ratio | -7.9518 |
| max_drawdown | 1.0000 |
| cagr | -0.9840 |
| net_avg_win | 8.4293 |
| net_avg_loss | -15.8780 |
| avg_hold_time_bars | 2.6506 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

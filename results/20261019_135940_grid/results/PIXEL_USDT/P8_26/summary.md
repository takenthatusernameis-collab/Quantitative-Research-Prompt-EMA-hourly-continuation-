# EMA Hourly Continuation — PIXEL/USDT P8_26

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1496 |
| net_profit_factor | 0.5993 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -8.0626 |
| sortino_ratio | -4.3972 |
| max_drawdown | 0.9951 |
| cagr | -0.8780 |
| net_avg_win | 21.9141 |
| net_avg_loss | -30.3918 |
| avg_hold_time_bars | 4.3021 |
| exposure | 0.2912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

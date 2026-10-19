# EMA Hourly Continuation — PENDLE/USDT P8_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6887 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9485 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -3.0296 |
| sortino_ratio | -1.0978 |
| max_drawdown | 0.7341 |
| cagr | -0.4061 |
| net_avg_win | 50.3051 |
| net_avg_loss | -68.3546 |
| avg_hold_time_bars | 21.4398 |
| exposure | 0.6471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

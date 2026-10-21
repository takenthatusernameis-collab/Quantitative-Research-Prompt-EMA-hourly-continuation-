# EMA Hourly Continuation — PENDLE/USDT P26_55

**Symbol:** PENDLE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8648 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.1100 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -0.9695 |
| sortino_ratio | -0.3004 |
| max_drawdown | 0.3850 |
| cagr | -0.1313 |
| net_avg_win | 78.3755 |
| net_avg_loss | -101.0196 |
| avg_hold_time_bars | 7.3341 |
| exposure | 0.1537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

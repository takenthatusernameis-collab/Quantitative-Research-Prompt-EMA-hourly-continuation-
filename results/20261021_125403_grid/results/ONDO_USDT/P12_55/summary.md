# EMA Hourly Continuation — ONDO/USDT P12_55

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.8178 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 1.0051 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.6809 |
| sortino_ratio | -0.5801 |
| max_drawdown | 0.5657 |
| cagr | -0.2353 |
| net_avg_win | 76.1551 |
| net_avg_loss | -92.1615 |
| avg_hold_time_bars | 11.8434 |
| exposure | 0.3128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

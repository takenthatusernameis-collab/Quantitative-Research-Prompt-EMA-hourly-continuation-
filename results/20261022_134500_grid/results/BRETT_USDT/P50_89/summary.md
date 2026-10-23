# EMA Hourly Continuation — BRETT/USDT P50_89

**Symbol:** BRETT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.5975 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -4.5371 |
| sortino_ratio | -1.6376 |
| max_drawdown | 0.8475 |
| cagr | -0.5405 |
| net_avg_win | 44.0076 |
| net_avg_loss | -63.0059 |
| avg_hold_time_bars | 4.9481 |
| exposure | 0.1467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

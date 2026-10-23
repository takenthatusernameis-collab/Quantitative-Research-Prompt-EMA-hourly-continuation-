# EMA Hourly Continuation — PUNDIX/USDT P12_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.6030 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9258 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -4.3294 |
| sortino_ratio | -1.5788 |
| max_drawdown | 0.8544 |
| cagr | -0.5278 |
| net_avg_win | 41.4160 |
| net_avg_loss | -59.8361 |
| avg_hold_time_bars | 19.1467 |
| exposure | 0.5814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

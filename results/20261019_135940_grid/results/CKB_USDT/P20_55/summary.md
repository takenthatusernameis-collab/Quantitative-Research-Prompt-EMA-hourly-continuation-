# EMA Hourly Continuation — CKB/USDT P20_55

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 966 |
| net_profit_factor | 0.5620 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -6.9611 |
| sortino_ratio | -3.0551 |
| max_drawdown | 0.9762 |
| cagr | -0.7717 |
| net_avg_win | 29.0405 |
| net_avg_loss | -41.6292 |
| avg_hold_time_bars | 5.4617 |
| exposure | 0.2398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

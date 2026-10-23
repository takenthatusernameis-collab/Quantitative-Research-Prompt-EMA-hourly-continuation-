# EMA Hourly Continuation — ETN/USDT P55_100

**Symbol:** ETN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.3295 |
| net_win_rate | 0.3462 |
| gross_profit_factor | 0.5228 |
| gross_win_rate | 0.3617 |
| sharpe_ratio | -9.7547 |
| sortino_ratio | -3.8404 |
| max_drawdown | 0.9833 |
| cagr | -0.8549 |
| net_avg_win | 21.5608 |
| net_avg_loss | -34.6489 |
| avg_hold_time_bars | 4.4482 |
| exposure | 0.1563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

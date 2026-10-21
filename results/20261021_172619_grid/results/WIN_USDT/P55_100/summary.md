# EMA Hourly Continuation — WIN/USDT P55_100

**Symbol:** WIN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.5984 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.8762 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -2.6573 |
| sortino_ratio | -0.6374 |
| max_drawdown | 0.5579 |
| cagr | -0.2552 |
| net_avg_win | 59.4661 |
| net_avg_loss | -87.3709 |
| avg_hold_time_bars | 10.3929 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

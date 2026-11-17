# EMA Hourly Continuation — NUM/USDT P50_100

**Symbol:** NUM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4539 |
| net_win_rate | 0.3863 |
| gross_profit_factor | 0.7269 |
| gross_win_rate | 0.3910 |
| sharpe_ratio | -6.8270 |
| sortino_ratio | -2.4381 |
| max_drawdown | 0.9488 |
| cagr | -0.6905 |
| net_avg_win | 31.7464 |
| net_avg_loss | -44.0282 |
| avg_hold_time_bars | 7.7087 |
| exposure | 0.2250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

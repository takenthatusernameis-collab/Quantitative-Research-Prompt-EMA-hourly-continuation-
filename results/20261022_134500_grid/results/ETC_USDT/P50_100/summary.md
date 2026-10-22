# EMA Hourly Continuation — ETC/USDT P50_100

**Symbol:** ETC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.4358 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -5.7885 |
| sortino_ratio | -2.0094 |
| max_drawdown | 0.9247 |
| cagr | -0.6395 |
| net_avg_win | 23.7659 |
| net_avg_loss | -51.7675 |
| avg_hold_time_bars | 6.1364 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

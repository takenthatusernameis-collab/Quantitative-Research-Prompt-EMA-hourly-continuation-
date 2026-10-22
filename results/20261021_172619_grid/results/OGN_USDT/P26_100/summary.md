# EMA Hourly Continuation — OGN/USDT P26_100

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6473 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8568 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -3.5114 |
| sortino_ratio | -1.1173 |
| max_drawdown | 0.7313 |
| cagr | -0.4018 |
| net_avg_win | 58.7430 |
| net_avg_loss | -74.0968 |
| avg_hold_time_bars | 14.9584 |
| exposure | 0.3418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

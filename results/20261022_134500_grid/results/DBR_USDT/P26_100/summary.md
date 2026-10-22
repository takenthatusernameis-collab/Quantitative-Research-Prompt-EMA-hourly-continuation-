# EMA Hourly Continuation — DBR/USDT P26_100

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.4592 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.7726 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -5.9951 |
| sortino_ratio | -2.0585 |
| max_drawdown | 0.8724 |
| cagr | -0.6372 |
| net_avg_win | 36.3617 |
| net_avg_loss | -58.2419 |
| avg_hold_time_bars | 12.5783 |
| exposure | 0.3426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

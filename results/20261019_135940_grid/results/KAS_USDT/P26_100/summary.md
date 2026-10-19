# EMA Hourly Continuation — KAS/USDT P26_100

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5620 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9383 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -4.4724 |
| sortino_ratio | -1.6631 |
| max_drawdown | 0.8671 |
| cagr | -0.5492 |
| net_avg_win | 33.5187 |
| net_avg_loss | -54.3869 |
| avg_hold_time_bars | 9.7752 |
| exposure | 0.3084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

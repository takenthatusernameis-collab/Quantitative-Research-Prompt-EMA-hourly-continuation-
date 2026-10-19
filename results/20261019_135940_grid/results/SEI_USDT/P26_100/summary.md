# EMA Hourly Continuation — SEI/USDT P26_100

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6653 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.3320 |
| sortino_ratio | -1.1490 |
| max_drawdown | 0.7579 |
| cagr | -0.4244 |
| net_avg_win | 51.2419 |
| net_avg_loss | -72.0705 |
| avg_hold_time_bars | 13.3638 |
| exposure | 0.3657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

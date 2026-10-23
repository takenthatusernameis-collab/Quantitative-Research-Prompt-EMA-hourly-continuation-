# EMA Hourly Continuation — ONT/USDT P26_100

**Symbol:** ONT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8594 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -4.2504 |
| sortino_ratio | -1.4834 |
| max_drawdown | 0.8387 |
| cagr | -0.5020 |
| net_avg_win | 41.0434 |
| net_avg_loss | -58.9450 |
| avg_hold_time_bars | 13.3922 |
| exposure | 0.3709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

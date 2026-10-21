# EMA Hourly Continuation — ETN/USDT P34_89

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.5454 |
| net_win_rate | 0.4176 |
| gross_profit_factor | 0.6920 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -3.6312 |
| sortino_ratio | -1.0348 |
| max_drawdown | 0.6381 |
| cagr | -0.3809 |
| net_avg_win | 53.6480 |
| net_avg_loss | -70.5423 |
| avg_hold_time_bars | 10.3412 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

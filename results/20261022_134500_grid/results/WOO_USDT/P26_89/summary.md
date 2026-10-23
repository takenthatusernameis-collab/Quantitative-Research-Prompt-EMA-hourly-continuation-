# EMA Hourly Continuation — WOO/USDT P26_89

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.7004 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 1.0356 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -3.5528 |
| sortino_ratio | -1.3250 |
| max_drawdown | 0.8072 |
| cagr | -0.4602 |
| net_avg_win | 55.4511 |
| net_avg_loss | -74.0400 |
| avg_hold_time_bars | 10.3202 |
| exposure | 0.3223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

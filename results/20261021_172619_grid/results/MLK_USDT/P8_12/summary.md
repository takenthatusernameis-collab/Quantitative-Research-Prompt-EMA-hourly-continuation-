# EMA Hourly Continuation — MLK/USDT P8_12

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.3209 |
| net_win_rate | 0.3081 |
| gross_profit_factor | 0.5308 |
| gross_win_rate | 0.3169 |
| sharpe_ratio | -6.6670 |
| sortino_ratio | -1.7669 |
| max_drawdown | 0.8783 |
| cagr | -0.5661 |
| net_avg_win | 39.1587 |
| net_avg_loss | -54.3432 |
| avg_hold_time_bars | 5.5407 |
| exposure | 0.0863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

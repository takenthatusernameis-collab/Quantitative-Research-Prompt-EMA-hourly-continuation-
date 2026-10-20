# EMA Hourly Continuation — GMX/USDT P20_100

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.6101 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -4.7548 |
| sortino_ratio | -1.7734 |
| max_drawdown | 0.8858 |
| cagr | -0.5720 |
| net_avg_win | 42.6900 |
| net_avg_loss | -59.3219 |
| avg_hold_time_bars | 12.8210 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

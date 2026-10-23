# EMA Hourly Continuation — QI/USDT P55_100

**Symbol:** QI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.4462 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.8472 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -5.3488 |
| sortino_ratio | -1.7995 |
| max_drawdown | 0.8925 |
| cagr | -0.5835 |
| net_avg_win | 27.7984 |
| net_avg_loss | -51.0308 |
| avg_hold_time_bars | 6.2583 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

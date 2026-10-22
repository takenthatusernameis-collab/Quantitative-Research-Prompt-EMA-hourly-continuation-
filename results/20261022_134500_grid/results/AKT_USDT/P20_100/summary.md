# EMA Hourly Continuation — AKT/USDT P20_100

**Symbol:** AKT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6386 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -3.6418 |
| sortino_ratio | -1.3145 |
| max_drawdown | 0.7961 |
| cagr | -0.4653 |
| net_avg_win | 45.1707 |
| net_avg_loss | -62.6492 |
| avg_hold_time_bars | 13.6303 |
| exposure | 0.4089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

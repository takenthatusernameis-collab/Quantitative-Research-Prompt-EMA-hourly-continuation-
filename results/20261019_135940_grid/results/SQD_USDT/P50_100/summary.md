# EMA Hourly Continuation — SQD/USDT P50_100

**Symbol:** SQD/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9899 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -4.0234 |
| sortino_ratio | -1.4064 |
| max_drawdown | 0.8137 |
| cagr | -0.4937 |
| net_avg_win | 51.2809 |
| net_avg_loss | -72.8510 |
| avg_hold_time_bars | 5.6533 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

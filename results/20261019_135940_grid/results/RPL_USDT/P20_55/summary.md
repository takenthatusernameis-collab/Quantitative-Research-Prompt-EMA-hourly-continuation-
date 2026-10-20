# EMA Hourly Continuation — RPL/USDT P20_55

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.5605 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.9533 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -6.0726 |
| sortino_ratio | -2.5525 |
| max_drawdown | 0.9573 |
| cagr | -0.7101 |
| net_avg_win | 29.9592 |
| net_avg_loss | -44.0347 |
| avg_hold_time_bars | 6.7847 |
| exposure | 0.2766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

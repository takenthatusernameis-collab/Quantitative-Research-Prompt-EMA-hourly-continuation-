# EMA Hourly Continuation — BAT/USDT P20_55

**Symbol:** BAT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.5007 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9150 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -6.2421 |
| sortino_ratio | -2.6658 |
| max_drawdown | 0.9592 |
| cagr | -0.7204 |
| net_avg_win | 22.8464 |
| net_avg_loss | -39.4471 |
| avg_hold_time_bars | 6.6465 |
| exposure | 0.2743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

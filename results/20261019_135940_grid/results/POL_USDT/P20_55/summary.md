# EMA Hourly Continuation — POL/USDT P20_55

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.4123 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.7874 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -7.9697 |
| sortino_ratio | -3.5252 |
| max_drawdown | 0.9879 |
| cagr | -0.8276 |
| net_avg_win | 15.7490 |
| net_avg_loss | -30.6725 |
| avg_hold_time_bars | 6.0526 |
| exposure | 0.2718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

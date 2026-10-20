# EMA Hourly Continuation — XYO/USDT P34_100

**Symbol:** XYO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.4157 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7812 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -7.8189 |
| sortino_ratio | -2.9619 |
| max_drawdown | 0.9752 |
| cagr | -0.7677 |
| net_avg_win | 24.2499 |
| net_avg_loss | -38.8903 |
| avg_hold_time_bars | 8.9692 |
| exposure | 0.2902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

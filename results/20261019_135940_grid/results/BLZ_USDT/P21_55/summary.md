# EMA Hourly Continuation — BLZ/USDT P21_55

**Symbol:** BLZ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.4678 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7989 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -8.5110 |
| sortino_ratio | -3.8220 |
| max_drawdown | 0.9908 |
| cagr | -0.8444 |
| net_avg_win | 20.9845 |
| net_avg_loss | -30.9766 |
| avg_hold_time_bars | 5.6526 |
| exposure | 0.2599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

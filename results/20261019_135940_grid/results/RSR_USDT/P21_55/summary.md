# EMA Hourly Continuation — RSR/USDT P21_55

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.5555 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8867 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -5.8610 |
| sortino_ratio | -2.4679 |
| max_drawdown | 0.9523 |
| cagr | -0.6993 |
| net_avg_win | 28.5715 |
| net_avg_loss | -44.2991 |
| avg_hold_time_bars | 5.8231 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

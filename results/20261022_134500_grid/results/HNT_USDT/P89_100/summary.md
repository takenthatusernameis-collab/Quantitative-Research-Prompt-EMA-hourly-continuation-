# EMA Hourly Continuation — HNT/USDT P89_100

**Symbol:** HNT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.2754 |
| net_win_rate | 0.3627 |
| gross_profit_factor | 0.6556 |
| gross_win_rate | 0.3935 |
| sharpe_ratio | -9.9463 |
| sortino_ratio | -3.7351 |
| max_drawdown | 0.9925 |
| cagr | -0.8564 |
| net_avg_win | 15.2726 |
| net_avg_loss | -31.5574 |
| avg_hold_time_bars | 2.9178 |
| exposure | 0.0903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

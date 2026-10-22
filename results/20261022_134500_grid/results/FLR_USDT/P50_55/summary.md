# EMA Hourly Continuation — FLR/USDT P50_55

**Symbol:** FLR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.1467 |
| net_win_rate | 0.2842 |
| gross_profit_factor | 0.5477 |
| gross_win_rate | 0.3440 |
| sharpe_ratio | -15.9037 |
| sortino_ratio | -7.4067 |
| max_drawdown | 1.0000 |
| cagr | -0.9831 |
| net_avg_win | 6.4627 |
| net_avg_loss | -17.4906 |
| avg_hold_time_bars | 1.9092 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — JST/USDT P21_50

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5096 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 1.0590 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -4.6035 |
| sortino_ratio | -1.5114 |
| max_drawdown | 0.8371 |
| cagr | -0.5068 |
| net_avg_win | 33.6323 |
| net_avg_loss | -63.2912 |
| avg_hold_time_bars | 7.2914 |
| exposure | 0.1732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

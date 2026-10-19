# EMA Hourly Continuation — ZRO/USDT P21_50

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9977 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -5.0649 |
| sortino_ratio | -2.2830 |
| max_drawdown | 0.9244 |
| cagr | -0.6654 |
| net_avg_win | 32.6048 |
| net_avg_loss | -49.7961 |
| avg_hold_time_bars | 4.4533 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

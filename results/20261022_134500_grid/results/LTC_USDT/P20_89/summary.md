# EMA Hourly Continuation — LTC/USDT P20_89

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.4048 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.7935 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -7.3874 |
| sortino_ratio | -2.8295 |
| max_drawdown | 0.9722 |
| cagr | -0.7554 |
| net_avg_win | 20.9648 |
| net_avg_loss | -38.1139 |
| avg_hold_time_bars | 11.0013 |
| exposure | 0.3715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

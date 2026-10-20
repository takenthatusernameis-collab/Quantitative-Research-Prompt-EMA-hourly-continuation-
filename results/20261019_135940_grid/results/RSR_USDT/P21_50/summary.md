# EMA Hourly Continuation — RSR/USDT P21_50

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.5503 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9020 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -6.0972 |
| sortino_ratio | -2.6368 |
| max_drawdown | 0.9609 |
| cagr | -0.7217 |
| net_avg_win | 26.9353 |
| net_avg_loss | -42.0932 |
| avg_hold_time_bars | 4.8908 |
| exposure | 0.2096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

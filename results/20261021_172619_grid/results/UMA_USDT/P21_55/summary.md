# EMA Hourly Continuation — UMA/USDT P21_55

**Symbol:** UMA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.6603 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9147 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -3.2548 |
| sortino_ratio | -1.1240 |
| max_drawdown | 0.7347 |
| cagr | -0.4035 |
| net_avg_win | 50.4510 |
| net_avg_loss | -70.3745 |
| avg_hold_time_bars | 8.8493 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LPT/USDT P89_100

**Symbol:** LPT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.3075 |
| net_win_rate | 0.3907 |
| gross_profit_factor | 0.7448 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -9.1691 |
| sortino_ratio | -3.3478 |
| max_drawdown | 0.9874 |
| cagr | -0.8239 |
| net_avg_win | 17.3925 |
| net_avg_loss | -36.2731 |
| avg_hold_time_bars | 2.2558 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

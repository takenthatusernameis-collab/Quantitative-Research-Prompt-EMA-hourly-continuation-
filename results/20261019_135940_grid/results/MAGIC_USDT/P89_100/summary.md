# EMA Hourly Continuation — MAGIC/USDT P89_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.3042 |
| net_win_rate | 0.4007 |
| gross_profit_factor | 0.8378 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -8.2652 |
| sortino_ratio | -2.8411 |
| max_drawdown | 0.9736 |
| cagr | -0.7648 |
| net_avg_win | 18.6683 |
| net_avg_loss | -41.0332 |
| avg_hold_time_bars | 2.6784 |
| exposure | 0.0693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

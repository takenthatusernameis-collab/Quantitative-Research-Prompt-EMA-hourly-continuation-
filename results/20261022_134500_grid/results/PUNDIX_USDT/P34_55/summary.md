# EMA Hourly Continuation — PUNDIX/USDT P34_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.4056 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -8.2784 |
| sortino_ratio | -3.4728 |
| max_drawdown | 0.9874 |
| cagr | -0.8230 |
| net_avg_win | 17.5833 |
| net_avg_loss | -33.7502 |
| avg_hold_time_bars | 4.2823 |
| exposure | 0.1703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

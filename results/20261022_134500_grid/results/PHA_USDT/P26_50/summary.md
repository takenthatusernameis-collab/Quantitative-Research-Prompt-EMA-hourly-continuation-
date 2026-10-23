# EMA Hourly Continuation — PHA/USDT P26_50

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.4125 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.7572 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -7.6038 |
| sortino_ratio | -3.3155 |
| max_drawdown | 0.9841 |
| cagr | -0.8057 |
| net_avg_win | 16.4474 |
| net_avg_loss | -31.0659 |
| avg_hold_time_bars | 3.6090 |
| exposure | 0.1573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LQTY/USDT P20_21

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.6352 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9778 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.2165 |
| sortino_ratio | -0.4842 |
| max_drawdown | 0.4569 |
| cagr | -0.1981 |
| net_avg_win | 65.7981 |
| net_avg_loss | -98.3700 |
| avg_hold_time_bars | 4.3190 |
| exposure | 0.0453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

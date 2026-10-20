# EMA Hourly Continuation — PHA/USDT P26_100

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.5201 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.7878 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -4.6347 |
| sortino_ratio | -1.7057 |
| max_drawdown | 0.8771 |
| cagr | -0.5596 |
| net_avg_win | 30.5959 |
| net_avg_loss | -47.8387 |
| avg_hold_time_bars | 10.4369 |
| exposure | 0.3269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

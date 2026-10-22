# EMA Hourly Continuation — CPOOL/USDT P20_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8292 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.2702 |
| sortino_ratio | -0.3999 |
| max_drawdown | 0.4171 |
| cagr | -0.1710 |
| net_avg_win | 75.9944 |
| net_avg_loss | -89.4114 |
| avg_hold_time_bars | 16.2099 |
| exposure | 0.3581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

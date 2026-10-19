# EMA Hourly Continuation — AAVE/USDT P8_26

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1554 |
| net_profit_factor | 0.4054 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7978 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -11.1430 |
| sortino_ratio | -6.1582 |
| max_drawdown | 0.9996 |
| cagr | -0.9565 |
| net_avg_win | 10.2951 |
| net_avg_loss | -18.8471 |
| avg_hold_time_bars | 3.9575 |
| exposure | 0.2795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

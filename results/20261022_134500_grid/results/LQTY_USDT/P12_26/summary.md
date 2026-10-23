# EMA Hourly Continuation — LQTY/USDT P12_26

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1387 |
| net_profit_factor | 0.4322 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8909 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -9.6625 |
| sortino_ratio | -5.0471 |
| max_drawdown | 0.9983 |
| cagr | -0.9194 |
| net_avg_win | 12.1768 |
| net_avg_loss | -23.0418 |
| avg_hold_time_bars | 3.4153 |
| exposure | 0.2144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

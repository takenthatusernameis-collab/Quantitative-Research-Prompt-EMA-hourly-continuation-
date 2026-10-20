# EMA Hourly Continuation — POLYX/USDT P20_26

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.2729 |
| net_win_rate | 0.3900 |
| gross_profit_factor | 0.7272 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -12.2361 |
| sortino_ratio | -5.8506 |
| max_drawdown | 0.9995 |
| cagr | -0.9522 |
| net_avg_win | 8.7458 |
| net_avg_loss | -20.4875 |
| avg_hold_time_bars | 2.6018 |
| exposure | 0.1301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

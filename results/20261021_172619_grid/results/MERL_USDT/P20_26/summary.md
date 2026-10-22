# EMA Hourly Continuation — MERL/USDT P20_26

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.5280 |
| sortino_ratio | -0.3474 |
| max_drawdown | 0.3399 |
| cagr | -0.1471 |
| net_avg_win | 76.4868 |
| net_avg_loss | -100.5598 |
| avg_hold_time_bars | 4.6653 |
| exposure | 0.0534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

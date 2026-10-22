# EMA Hourly Continuation — SSV/USDT P20_100

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7220 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8833 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -2.5973 |
| sortino_ratio | -0.8383 |
| max_drawdown | 0.6553 |
| cagr | -0.3200 |
| net_avg_win | 67.5792 |
| net_avg_loss | -79.8975 |
| avg_hold_time_bars | 17.5222 |
| exposure | 0.4115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

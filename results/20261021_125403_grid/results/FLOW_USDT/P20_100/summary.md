# EMA Hourly Continuation — FLOW/USDT P20_100

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7880 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -1.5635 |
| sortino_ratio | -0.4667 |
| max_drawdown | 0.4469 |
| cagr | -0.1944 |
| net_avg_win | 71.7799 |
| net_avg_loss | -90.2560 |
| avg_hold_time_bars | 22.4885 |
| exposure | 0.4457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

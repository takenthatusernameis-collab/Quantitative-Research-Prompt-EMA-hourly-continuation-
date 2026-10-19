# EMA Hourly Continuation — DCR/USDT P100_200

**Symbol:** DCR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -4.7811 |
| sortino_ratio | -1.3789 |
| max_drawdown | 0.8109 |
| cagr | -0.4833 |
| net_avg_win | 42.9316 |
| net_avg_loss | -63.2472 |
| avg_hold_time_bars | 8.3626 |
| exposure | 0.1597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

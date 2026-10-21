# EMA Hourly Continuation — GRAM/USDT P34_100

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6221 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8572 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -3.0512 |
| sortino_ratio | -0.9000 |
| max_drawdown | 0.6627 |
| cagr | -0.3376 |
| net_avg_win | 53.8601 |
| net_avg_loss | -73.8327 |
| avg_hold_time_bars | 12.9579 |
| exposure | 0.2521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

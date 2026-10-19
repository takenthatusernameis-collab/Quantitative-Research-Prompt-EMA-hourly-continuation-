# EMA Hourly Continuation — ZBCN/USDT P50_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.5152 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8161 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -5.6549 |
| sortino_ratio | -2.1731 |
| max_drawdown | 0.9300 |
| cagr | -0.6508 |
| net_avg_win | 30.2600 |
| net_avg_loss | -46.4442 |
| avg_hold_time_bars | 4.3560 |
| exposure | 0.1483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ROSE/USDT P12_21

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7461 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0295 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.8059 |
| sortino_ratio | -0.4822 |
| max_drawdown | 0.4484 |
| cagr | -0.1982 |
| net_avg_win | 71.9126 |
| net_avg_loss | -98.0710 |
| avg_hold_time_bars | 4.9217 |
| exposure | 0.0772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

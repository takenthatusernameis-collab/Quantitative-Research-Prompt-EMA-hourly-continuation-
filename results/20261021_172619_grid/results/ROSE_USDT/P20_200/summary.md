# EMA Hourly Continuation — ROSE/USDT P20_200

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8587 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0036 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -0.7610 |
| sortino_ratio | -0.1844 |
| max_drawdown | 0.2434 |
| cagr | -0.0835 |
| net_avg_win | 82.4426 |
| net_avg_loss | -98.0319 |
| avg_hold_time_bars | 52.6202 |
| exposure | 0.6865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

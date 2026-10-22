# EMA Hourly Continuation — CARV/USDT P20_100

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7395 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.0967 |
| sortino_ratio | -0.6391 |
| max_drawdown | 0.4759 |
| cagr | -0.2552 |
| net_avg_win | 72.5634 |
| net_avg_loss | -89.0210 |
| avg_hold_time_bars | 20.1081 |
| exposure | 0.4187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

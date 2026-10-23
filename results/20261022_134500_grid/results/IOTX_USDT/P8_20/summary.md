# EMA Hourly Continuation — IOTX/USDT P8_20

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1629 |
| net_profit_factor | 0.4741 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -11.1022 |
| sortino_ratio | -6.3408 |
| max_drawdown | 0.9996 |
| cagr | -0.9569 |
| net_avg_win | 12.4641 |
| net_avg_loss | -20.9800 |
| avg_hold_time_bars | 2.9705 |
| exposure | 0.2200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

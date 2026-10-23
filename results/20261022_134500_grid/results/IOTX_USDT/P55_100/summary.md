# EMA Hourly Continuation — IOTX/USDT P55_100

**Symbol:** IOTX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4672 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -6.0405 |
| sortino_ratio | -2.2002 |
| max_drawdown | 0.9369 |
| cagr | -0.6627 |
| net_avg_win | 27.3184 |
| net_avg_loss | -47.4132 |
| avg_hold_time_bars | 5.0985 |
| exposure | 0.1553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

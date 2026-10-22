# EMA Hourly Continuation — AEVO/USDT P8_89

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7926 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.7491 |
| sortino_ratio | -0.5532 |
| max_drawdown | 0.5024 |
| cagr | -0.2266 |
| net_avg_win | 75.6398 |
| net_avg_loss | -90.5483 |
| avg_hold_time_bars | 30.6667 |
| exposure | 0.6869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

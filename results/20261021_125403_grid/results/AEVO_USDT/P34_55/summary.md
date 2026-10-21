# EMA Hourly Continuation — AEVO/USDT P34_55

**Symbol:** AEVO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9283 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -2.4388 |
| sortino_ratio | -0.7033 |
| max_drawdown | 0.5562 |
| cagr | -0.2754 |
| net_avg_win | 57.4343 |
| net_avg_loss | -81.0262 |
| avg_hold_time_bars | 5.4644 |
| exposure | 0.1006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

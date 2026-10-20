# EMA Hourly Continuation — AEVO/USDT P8_144

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7533 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0166 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.9451 |
| sortino_ratio | -0.5434 |
| max_drawdown | 0.5401 |
| cagr | -0.2313 |
| net_avg_win | 74.0734 |
| net_avg_loss | -97.8377 |
| avg_hold_time_bars | 43.7506 |
| exposure | 0.7939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

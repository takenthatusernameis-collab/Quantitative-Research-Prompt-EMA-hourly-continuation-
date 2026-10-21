# EMA Hourly Continuation — RENDER/USDT P8_12

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.8478 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.1663 |
| gross_win_rate | 0.5373 |
| sharpe_ratio | -0.8048 |
| sortino_ratio | -0.1780 |
| max_drawdown | 0.2310 |
| cagr | -0.0789 |
| net_avg_win | 83.9887 |
| net_avg_loss | -115.0426 |
| avg_hold_time_bars | 4.4428 |
| exposure | 0.0471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

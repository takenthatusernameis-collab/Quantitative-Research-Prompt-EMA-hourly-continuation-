# EMA Hourly Continuation — ENA/USDT P8_21

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.9739 |
| net_win_rate | 0.5542 |
| gross_profit_factor | 1.2292 |
| gross_win_rate | 0.5542 |
| sharpe_ratio | -0.1145 |
| sortino_ratio | -0.0368 |
| max_drawdown | 0.2236 |
| cagr | -0.0254 |
| net_avg_win | 86.0429 |
| net_avg_loss | -109.8270 |
| avg_hold_time_bars | 5.8405 |
| exposure | 0.1298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

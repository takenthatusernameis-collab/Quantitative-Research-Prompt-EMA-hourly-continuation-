# EMA Hourly Continuation — RENDER/USDT P8_100

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6966 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -2.8142 |
| sortino_ratio | -1.0168 |
| max_drawdown | 0.6615 |
| cagr | -0.3834 |
| net_avg_win | 53.7551 |
| net_avg_loss | -74.2235 |
| avg_hold_time_bars | 22.9097 |
| exposure | 0.6832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

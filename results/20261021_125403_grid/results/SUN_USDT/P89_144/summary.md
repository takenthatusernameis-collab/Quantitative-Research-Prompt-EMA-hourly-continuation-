# EMA Hourly Continuation — SUN/USDT P89_144

**Symbol:** SUN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.4096 |
| net_win_rate | 0.4098 |
| gross_profit_factor | 0.8209 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -5.2374 |
| sortino_ratio | -1.3240 |
| max_drawdown | 0.7958 |
| cagr | -0.4672 |
| net_avg_win | 44.1727 |
| net_avg_loss | -74.8834 |
| avg_hold_time_bars | 10.0918 |
| exposure | 0.1393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

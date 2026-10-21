# EMA Hourly Continuation — TURBO/USDT P34_55

**Symbol:** TURBO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.5554 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.9654 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -6.8284 |
| sortino_ratio | -2.9117 |
| max_drawdown | 0.9528 |
| cagr | -0.7609 |
| net_avg_win | 33.6087 |
| net_avg_loss | -52.4885 |
| avg_hold_time_bars | 2.9421 |
| exposure | 0.1220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

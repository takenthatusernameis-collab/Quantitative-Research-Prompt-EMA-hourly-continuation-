# EMA Hourly Continuation — LQTY/USDT P8_100

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7364 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0065 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -2.0694 |
| sortino_ratio | -0.6496 |
| max_drawdown | 0.5636 |
| cagr | -0.2662 |
| net_avg_win | 60.8124 |
| net_avg_loss | -82.9087 |
| avg_hold_time_bars | 33.3038 |
| exposure | 0.7490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

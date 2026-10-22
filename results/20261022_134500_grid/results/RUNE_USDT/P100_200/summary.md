# EMA Hourly Continuation — RUNE/USDT P100_200

**Symbol:** RUNE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5967 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -2.8349 |
| sortino_ratio | -0.7413 |
| max_drawdown | 0.5955 |
| cagr | -0.2974 |
| net_avg_win | 52.0849 |
| net_avg_loss | -81.8954 |
| avg_hold_time_bars | 10.1014 |
| exposure | 0.1584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

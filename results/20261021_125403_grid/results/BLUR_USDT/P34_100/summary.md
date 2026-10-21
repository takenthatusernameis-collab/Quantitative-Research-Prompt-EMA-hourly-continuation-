# EMA Hourly Continuation — BLUR/USDT P34_100

**Symbol:** BLUR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.9097 |
| net_win_rate | 0.5374 |
| gross_profit_factor | 1.1594 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -0.6395 |
| sortino_ratio | -0.1965 |
| max_drawdown | 0.3441 |
| cagr | -0.0905 |
| net_avg_win | 87.8085 |
| net_avg_loss | -112.1556 |
| avg_hold_time_bars | 13.5308 |
| exposure | 0.2780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

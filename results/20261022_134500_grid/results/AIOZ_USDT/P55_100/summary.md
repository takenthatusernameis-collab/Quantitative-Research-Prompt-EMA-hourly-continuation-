# EMA Hourly Continuation — AIOZ/USDT P55_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6124 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9999 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -5.2072 |
| sortino_ratio | -1.9661 |
| max_drawdown | 0.9180 |
| cagr | -0.6166 |
| net_avg_win | 42.6632 |
| net_avg_loss | -61.4584 |
| avg_hold_time_bars | 5.1377 |
| exposure | 0.1679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

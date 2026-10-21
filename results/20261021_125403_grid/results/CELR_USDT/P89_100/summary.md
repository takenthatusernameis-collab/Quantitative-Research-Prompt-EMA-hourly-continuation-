# EMA Hourly Continuation — CELR/USDT P89_100

**Symbol:** CELR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9080 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -1.9637 |
| sortino_ratio | -0.3738 |
| max_drawdown | 0.3600 |
| cagr | -0.1573 |
| net_avg_win | 69.5328 |
| net_avg_loss | -100.5015 |
| avg_hold_time_bars | 5.3107 |
| exposure | 0.0425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

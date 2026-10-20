# EMA Hourly Continuation — ARKM/USDT P21_100

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.6322 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -3.9717 |
| sortino_ratio | -1.5198 |
| max_drawdown | 0.8355 |
| cagr | -0.5085 |
| net_avg_win | 41.9354 |
| net_avg_loss | -58.2998 |
| avg_hold_time_bars | 11.6516 |
| exposure | 0.3861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

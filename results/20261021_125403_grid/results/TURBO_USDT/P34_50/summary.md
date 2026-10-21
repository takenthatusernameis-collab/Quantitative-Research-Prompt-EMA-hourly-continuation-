# EMA Hourly Continuation — TURBO/USDT P34_50

**Symbol:** TURBO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.7962 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -2.5329 |
| sortino_ratio | -0.5625 |
| max_drawdown | 0.4608 |
| cagr | -0.2272 |
| net_avg_win | 68.2739 |
| net_avg_loss | -91.2723 |
| avg_hold_time_bars | 4.7882 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ARKM/USDT P8_50

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.8509 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0323 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.3270 |
| sortino_ratio | -0.4948 |
| max_drawdown | 0.4985 |
| cagr | -0.2070 |
| net_avg_win | 73.2362 |
| net_avg_loss | -89.4495 |
| avg_hold_time_bars | 15.0400 |
| exposure | 0.4615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

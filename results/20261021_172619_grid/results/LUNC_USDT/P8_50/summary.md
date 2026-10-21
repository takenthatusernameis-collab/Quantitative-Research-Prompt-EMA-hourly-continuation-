# EMA Hourly Continuation — LUNC/USDT P8_50

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.6289 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8179 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -4.1456 |
| sortino_ratio | -1.5599 |
| max_drawdown | 0.8368 |
| cagr | -0.5125 |
| net_avg_win | 45.5316 |
| net_avg_loss | -57.5815 |
| avg_hold_time_bars | 12.5741 |
| exposure | 0.4012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

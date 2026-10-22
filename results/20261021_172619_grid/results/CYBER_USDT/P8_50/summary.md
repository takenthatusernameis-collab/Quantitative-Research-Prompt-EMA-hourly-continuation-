# EMA Hourly Continuation — CYBER/USDT P8_50

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.7564 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9653 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -2.6000 |
| sortino_ratio | -1.0349 |
| max_drawdown | 0.7016 |
| cagr | -0.3784 |
| net_avg_win | 56.7991 |
| net_avg_loss | -72.6161 |
| avg_hold_time_bars | 12.3884 |
| exposure | 0.4364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

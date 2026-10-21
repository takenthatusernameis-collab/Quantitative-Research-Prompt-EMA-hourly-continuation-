# EMA Hourly Continuation — FLOW/USDT P20_50

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6995 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9702 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.5937 |
| sortino_ratio | -0.8504 |
| max_drawdown | 0.6403 |
| cagr | -0.3227 |
| net_avg_win | 56.5316 |
| net_avg_loss | -77.7918 |
| avg_hold_time_bars | 7.5916 |
| exposure | 0.1808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

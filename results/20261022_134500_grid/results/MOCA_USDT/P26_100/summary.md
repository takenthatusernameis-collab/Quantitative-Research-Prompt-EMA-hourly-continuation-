# EMA Hourly Continuation — MOCA/USDT P26_100

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.6089 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -4.5987 |
| sortino_ratio | -1.6479 |
| max_drawdown | 0.8570 |
| cagr | -0.5552 |
| net_avg_win | 47.3112 |
| net_avg_loss | -67.2639 |
| avg_hold_time_bars | 11.2111 |
| exposure | 0.3355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MERL/USDT P8_50

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.6609 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8967 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -4.2250 |
| sortino_ratio | -1.9714 |
| max_drawdown | 0.9116 |
| cagr | -0.6031 |
| net_avg_win | 34.0342 |
| net_avg_loss | -46.9494 |
| avg_hold_time_bars | 9.6645 |
| exposure | 0.4766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

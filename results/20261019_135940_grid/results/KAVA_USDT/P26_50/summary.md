# EMA Hourly Continuation — KAVA/USDT P26_50

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.4503 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -10.3807 |
| sortino_ratio | -4.7518 |
| max_drawdown | 0.9978 |
| cagr | -0.9118 |
| net_avg_win | 19.2789 |
| net_avg_loss | -29.7571 |
| avg_hold_time_bars | 3.9381 |
| exposure | 0.1851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

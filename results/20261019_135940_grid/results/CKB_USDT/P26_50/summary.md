# EMA Hourly Continuation — CKB/USDT P26_50

**Symbol:** CKB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.4521 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.8023 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -8.7599 |
| sortino_ratio | -3.8432 |
| max_drawdown | 0.9918 |
| cagr | -0.8497 |
| net_avg_win | 20.2475 |
| net_avg_loss | -32.4853 |
| avg_hold_time_bars | 3.7409 |
| exposure | 0.1634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

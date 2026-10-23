# EMA Hourly Continuation — MOCA/USDT P20_55

**Symbol:** MOCA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.5325 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8876 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -6.6297 |
| sortino_ratio | -2.8060 |
| max_drawdown | 0.9598 |
| cagr | -0.7516 |
| net_avg_win | 29.1036 |
| net_avg_loss | -44.7479 |
| avg_hold_time_bars | 5.5090 |
| exposure | 0.2300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

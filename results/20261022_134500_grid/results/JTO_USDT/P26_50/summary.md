# EMA Hourly Continuation — JTO/USDT P26_50

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.5426 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.9238 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -6.2275 |
| sortino_ratio | -2.6671 |
| max_drawdown | 0.9610 |
| cagr | -0.7237 |
| net_avg_win | 26.8769 |
| net_avg_loss | -42.0850 |
| avg_hold_time_bars | 4.1463 |
| exposure | 0.1740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

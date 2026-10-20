# EMA Hourly Continuation — WEMIX/USDT P26_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.2968 |
| net_win_rate | 0.3065 |
| gross_profit_factor | 0.4937 |
| gross_win_rate | 0.3198 |
| sharpe_ratio | -12.6418 |
| sortino_ratio | -5.6796 |
| max_drawdown | 0.9993 |
| cagr | -0.9426 |
| net_avg_win | 14.0106 |
| net_avg_loss | -20.8657 |
| avg_hold_time_bars | 9.6996 |
| exposure | 0.4330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

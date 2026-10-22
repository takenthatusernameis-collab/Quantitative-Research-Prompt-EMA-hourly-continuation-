# EMA Hourly Continuation — MOCA/USDT P8_26

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6674 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9022 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -3.1586 |
| sortino_ratio | -1.2111 |
| max_drawdown | 0.7363 |
| cagr | -0.4246 |
| net_avg_win | 45.4580 |
| net_avg_loss | -64.2516 |
| avg_hold_time_bars | 6.4639 |
| exposure | 0.2109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

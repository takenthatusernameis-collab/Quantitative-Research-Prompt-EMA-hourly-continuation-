# EMA Hourly Continuation — ONE/USDT P20_50

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.5418 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.9011 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -7.1362 |
| sortino_ratio | -3.1674 |
| max_drawdown | 0.9810 |
| cagr | -0.7890 |
| net_avg_win | 25.8080 |
| net_avg_loss | -39.1702 |
| avg_hold_time_bars | 5.3970 |
| exposure | 0.2441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

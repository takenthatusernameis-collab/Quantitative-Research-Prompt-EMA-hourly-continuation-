# EMA Hourly Continuation — SUI/USDT P26_50

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.5443 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -8.3052 |
| sortino_ratio | -3.6856 |
| max_drawdown | 0.9916 |
| cagr | -0.8460 |
| net_avg_win | 26.7739 |
| net_avg_loss | -38.6199 |
| avg_hold_time_bars | 3.2697 |
| exposure | 0.1494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

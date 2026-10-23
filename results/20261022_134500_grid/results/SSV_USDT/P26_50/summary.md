# EMA Hourly Continuation — SSV/USDT P26_50

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.5032 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -7.7676 |
| sortino_ratio | -3.5275 |
| max_drawdown | 0.9874 |
| cagr | -0.8228 |
| net_avg_win | 21.7868 |
| net_avg_loss | -34.2638 |
| avg_hold_time_bars | 3.9143 |
| exposure | 0.1840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

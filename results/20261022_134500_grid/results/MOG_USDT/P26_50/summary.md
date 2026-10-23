# EMA Hourly Continuation — MOG/USDT P26_50

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 883 |
| net_profit_factor | 0.5855 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -6.3007 |
| sortino_ratio | -2.7517 |
| max_drawdown | 0.9545 |
| cagr | -0.7385 |
| net_avg_win | 33.5166 |
| net_avg_loss | -47.8466 |
| avg_hold_time_bars | 3.6976 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

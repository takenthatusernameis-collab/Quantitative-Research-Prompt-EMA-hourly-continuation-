# EMA Hourly Continuation — SYN/USDT P20_50

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6967 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.4811 |
| sortino_ratio | -0.8417 |
| max_drawdown | 0.6381 |
| cagr | -0.3214 |
| net_avg_win | 52.7642 |
| net_avg_loss | -69.8056 |
| avg_hold_time_bars | 7.7982 |
| exposure | 0.2003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

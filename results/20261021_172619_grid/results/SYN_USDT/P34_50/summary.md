# EMA Hourly Continuation — SYN/USDT P34_50

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.6907 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -2.0767 |
| sortino_ratio | -0.5560 |
| max_drawdown | 0.5098 |
| cagr | -0.2248 |
| net_avg_win | 61.6785 |
| net_avg_loss | -85.7923 |
| avg_hold_time_bars | 5.7077 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — T/USDT P20_26

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 937 |
| net_profit_factor | 0.3556 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -10.7053 |
| sortino_ratio | -4.6813 |
| max_drawdown | 0.9980 |
| cagr | -0.9145 |
| net_avg_win | 14.2274 |
| net_avg_loss | -28.1560 |
| avg_hold_time_bars | 3.5464 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

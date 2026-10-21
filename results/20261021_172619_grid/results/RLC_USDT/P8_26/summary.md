# EMA Hourly Continuation — RLC/USDT P8_26

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 816 |
| net_profit_factor | 0.7098 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9830 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -3.2868 |
| sortino_ratio | -1.3456 |
| max_drawdown | 0.8086 |
| cagr | -0.4599 |
| net_avg_win | 47.7788 |
| net_avg_loss | -65.6798 |
| avg_hold_time_bars | 6.7022 |
| exposure | 0.2486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

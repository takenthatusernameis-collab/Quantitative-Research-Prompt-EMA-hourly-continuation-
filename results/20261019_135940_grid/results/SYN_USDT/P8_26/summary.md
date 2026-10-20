# EMA Hourly Continuation — SYN/USDT P8_26

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1450 |
| net_profit_factor | 0.5360 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -8.1836 |
| sortino_ratio | -4.3780 |
| max_drawdown | 0.9953 |
| cagr | -0.8818 |
| net_avg_win | 17.7437 |
| net_avg_loss | -26.7469 |
| avg_hold_time_bars | 4.4910 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

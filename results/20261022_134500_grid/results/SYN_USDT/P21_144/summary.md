# EMA Hourly Continuation — SYN/USDT P21_144

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7490 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9945 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -1.9141 |
| sortino_ratio | -0.5644 |
| max_drawdown | 0.5115 |
| cagr | -0.2333 |
| net_avg_win | 68.2114 |
| net_avg_loss | -88.9814 |
| avg_hold_time_bars | 29.9559 |
| exposure | 0.5869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

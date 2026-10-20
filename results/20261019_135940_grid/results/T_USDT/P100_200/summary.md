# EMA Hourly Continuation — T/USDT P100_200

**Symbol:** T/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.5756 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -3.2468 |
| sortino_ratio | -0.9056 |
| max_drawdown | 0.6669 |
| cagr | -0.3489 |
| net_avg_win | 48.2223 |
| net_avg_loss | -76.7564 |
| avg_hold_time_bars | 11.1157 |
| exposure | 0.1957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

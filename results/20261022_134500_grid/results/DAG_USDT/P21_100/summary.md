# EMA Hourly Continuation — DAG/USDT P21_100

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.4976 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7557 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -5.9532 |
| sortino_ratio | -2.2678 |
| max_drawdown | 0.9443 |
| cagr | -0.6803 |
| net_avg_win | 28.8250 |
| net_avg_loss | -43.4461 |
| avg_hold_time_bars | 10.4960 |
| exposure | 0.3607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ZK/USDT P100_200

**Symbol:** ZK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6578 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -2.6160 |
| sortino_ratio | -0.7440 |
| max_drawdown | 0.5745 |
| cagr | -0.2998 |
| net_avg_win | 58.4906 |
| net_avg_loss | -84.8135 |
| avg_hold_time_bars | 10.0052 |
| exposure | 0.1859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

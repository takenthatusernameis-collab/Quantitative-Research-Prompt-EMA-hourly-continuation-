# EMA Hourly Continuation — ZBCN/USDT P26_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.6500 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9472 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -4.1889 |
| sortino_ratio | -1.7015 |
| max_drawdown | 0.8793 |
| cagr | -0.5600 |
| net_avg_win | 41.0200 |
| net_avg_loss | -57.5444 |
| avg_hold_time_bars | 7.5995 |
| exposure | 0.2897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

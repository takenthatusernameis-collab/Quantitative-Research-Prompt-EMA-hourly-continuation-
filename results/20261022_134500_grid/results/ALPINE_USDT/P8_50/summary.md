# EMA Hourly Continuation — ALPINE/USDT P8_50

**Symbol:** ALPINE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 996 |
| net_profit_factor | 0.4641 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -7.3888 |
| sortino_ratio | -3.2768 |
| max_drawdown | 0.9826 |
| cagr | -0.7973 |
| net_avg_win | 20.0512 |
| net_avg_loss | -32.0280 |
| avg_hold_time_bars | 9.9548 |
| exposure | 0.4507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

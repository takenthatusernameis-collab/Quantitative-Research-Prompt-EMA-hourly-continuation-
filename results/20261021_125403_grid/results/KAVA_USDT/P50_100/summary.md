# EMA Hourly Continuation — KAVA/USDT P50_100

**Symbol:** KAVA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8458 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -4.0743 |
| sortino_ratio | -1.1955 |
| max_drawdown | 0.7691 |
| cagr | -0.4296 |
| net_avg_win | 51.0582 |
| net_avg_loss | -74.2919 |
| avg_hold_time_bars | 9.2524 |
| exposure | 0.1783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CATI/USDT P89_100

**Symbol:** CATI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.3182 |
| net_win_rate | 0.3722 |
| gross_profit_factor | 0.7823 |
| gross_win_rate | 0.4185 |
| sharpe_ratio | -9.7974 |
| sortino_ratio | -3.6238 |
| max_drawdown | 0.9809 |
| cagr | -0.8490 |
| net_avg_win | 22.7616 |
| net_avg_loss | -42.4188 |
| avg_hold_time_bars | 3.2056 |
| exposure | 0.0949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

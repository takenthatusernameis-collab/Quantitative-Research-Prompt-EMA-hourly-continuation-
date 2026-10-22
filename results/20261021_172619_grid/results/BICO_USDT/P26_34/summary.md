# EMA Hourly Continuation — BICO/USDT P26_34

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.4929 |
| net_win_rate | 0.4366 |
| gross_profit_factor | 0.7206 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -3.7012 |
| sortino_ratio | -0.9946 |
| max_drawdown | 0.6844 |
| cagr | -0.3663 |
| net_avg_win | 42.7590 |
| net_avg_loss | -67.2368 |
| avg_hold_time_bars | 4.9803 |
| exposure | 0.0804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

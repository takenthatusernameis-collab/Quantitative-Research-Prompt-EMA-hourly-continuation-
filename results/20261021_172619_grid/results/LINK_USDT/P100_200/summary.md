# EMA Hourly Continuation — LINK/USDT P100_200

**Symbol:** LINK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7922 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0575 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -0.9855 |
| sortino_ratio | -0.2141 |
| max_drawdown | 0.2788 |
| cagr | -0.0936 |
| net_avg_win | 70.0573 |
| net_avg_loss | -96.5452 |
| avg_hold_time_bars | 13.2018 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

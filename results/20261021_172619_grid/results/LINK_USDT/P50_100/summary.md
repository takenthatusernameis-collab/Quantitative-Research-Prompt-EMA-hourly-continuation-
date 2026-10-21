# EMA Hourly Continuation — LINK/USDT P50_100

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9832 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.8845 |
| sortino_ratio | -0.4784 |
| max_drawdown | 0.4314 |
| cagr | -0.1971 |
| net_avg_win | 72.7004 |
| net_avg_loss | -96.4658 |
| avg_hold_time_bars | 9.5223 |
| exposure | 0.1359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

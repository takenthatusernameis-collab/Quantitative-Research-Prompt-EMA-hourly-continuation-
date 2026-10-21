# EMA Hourly Continuation — BLUR/USDT P144_200

**Symbol:** BLUR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.6371 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.8937 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -1.9544 |
| sortino_ratio | -0.4275 |
| max_drawdown | 0.3976 |
| cagr | -0.1777 |
| net_avg_win | 60.5250 |
| net_avg_loss | -88.7214 |
| avg_hold_time_bars | 6.0855 |
| exposure | 0.0644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

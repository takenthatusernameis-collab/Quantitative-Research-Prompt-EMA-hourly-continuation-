# EMA Hourly Continuation — SAND/USDT P26_200

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7151 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -1.7702 |
| sortino_ratio | -0.4201 |
| max_drawdown | 0.3973 |
| cagr | -0.1764 |
| net_avg_win | 74.4509 |
| net_avg_loss | -90.8423 |
| avg_hold_time_bars | 46.0932 |
| exposure | 0.5845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

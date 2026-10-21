# EMA Hourly Continuation — LINK/USDT P26_34

**Symbol:** LINK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.6266 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9043 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -1.9687 |
| sortino_ratio | -0.3656 |
| max_drawdown | 0.3603 |
| cagr | -0.1537 |
| net_avg_win | 72.7351 |
| net_avg_loss | -103.0350 |
| avg_hold_time_bars | 5.2024 |
| exposure | 0.0397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

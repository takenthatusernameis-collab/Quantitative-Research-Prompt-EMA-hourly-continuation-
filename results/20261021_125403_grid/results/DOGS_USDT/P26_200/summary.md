# EMA Hourly Continuation — DOGS/USDT P26_200

**Symbol:** DOGS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.8107 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9551 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -1.1369 |
| sortino_ratio | -0.2814 |
| max_drawdown | 0.3080 |
| cagr | -0.1229 |
| net_avg_win | 83.5401 |
| net_avg_loss | -98.3612 |
| avg_hold_time_bars | 40.8682 |
| exposure | 0.5594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

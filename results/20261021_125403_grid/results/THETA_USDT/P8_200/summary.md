# EMA Hourly Continuation — THETA/USDT P8_200

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.9911 |
| net_win_rate | 0.5442 |
| gross_profit_factor | 1.1724 |
| gross_win_rate | 0.5442 |
| sharpe_ratio | 0.0023 |
| sortino_ratio | 0.0006 |
| max_drawdown | 0.2263 |
| cagr | -0.0054 |
| net_avg_win | 96.9970 |
| net_avg_loss | -116.8350 |
| avg_hold_time_bars | 62.8410 |
| exposure | 0.8084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TAIKO/USDT P21_34

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6425 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -2.4897 |
| sortino_ratio | -0.6485 |
| max_drawdown | 0.5458 |
| cagr | -0.2549 |
| net_avg_win | 59.0840 |
| net_avg_loss | -89.0548 |
| avg_hold_time_bars | 6.4084 |
| exposure | 0.0957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ALGO/USDT P8_89

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8499 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -1.0079 |
| sortino_ratio | -0.3159 |
| max_drawdown | 0.3374 |
| cagr | -0.1382 |
| net_avg_win | 72.0292 |
| net_avg_loss | -89.5018 |
| avg_hold_time_bars | 29.4906 |
| exposure | 0.6394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

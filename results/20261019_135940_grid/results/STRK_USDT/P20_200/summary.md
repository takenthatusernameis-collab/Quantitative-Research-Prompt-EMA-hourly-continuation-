# EMA Hourly Continuation — STRK/USDT P20_200

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7116 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9478 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.1960 |
| sortino_ratio | -0.6067 |
| max_drawdown | 0.5563 |
| cagr | -0.2503 |
| net_avg_win | 68.3086 |
| net_avg_loss | -89.7226 |
| avg_hold_time_bars | 36.4026 |
| exposure | 0.6370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

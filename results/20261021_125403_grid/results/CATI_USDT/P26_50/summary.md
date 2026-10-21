# EMA Hourly Continuation — CATI/USDT P26_50

**Symbol:** CATI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.6139 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.8083 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -2.9708 |
| sortino_ratio | -0.7923 |
| max_drawdown | 0.5573 |
| cagr | -0.3067 |
| net_avg_win | 65.2612 |
| net_avg_loss | -84.7879 |
| avg_hold_time_bars | 8.5495 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

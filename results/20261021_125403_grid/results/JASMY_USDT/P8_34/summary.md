# EMA Hourly Continuation — JASMY/USDT P8_34

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.7765 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.2275 |
| sortino_ratio | -0.8344 |
| max_drawdown | 0.6384 |
| cagr | -0.3186 |
| net_avg_win | 63.5735 |
| net_avg_loss | -79.7453 |
| avg_hold_time_bars | 8.3460 |
| exposure | 0.2599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

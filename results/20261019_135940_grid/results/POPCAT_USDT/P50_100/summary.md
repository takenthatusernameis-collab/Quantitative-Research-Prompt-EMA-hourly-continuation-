# EMA Hourly Continuation — POPCAT/USDT P50_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8147 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -4.8051 |
| sortino_ratio | -1.7724 |
| max_drawdown | 0.8404 |
| cagr | -0.5711 |
| net_avg_win | 43.7730 |
| net_avg_loss | -60.3740 |
| avg_hold_time_bars | 6.2403 |
| exposure | 0.1948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

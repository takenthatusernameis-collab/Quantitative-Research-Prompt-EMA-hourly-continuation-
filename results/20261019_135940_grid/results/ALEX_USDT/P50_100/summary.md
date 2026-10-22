# EMA Hourly Continuation — ALEX/USDT P50_100

**Symbol:** ALEX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.4727 |
| net_win_rate | 0.3727 |
| gross_profit_factor | 0.7634 |
| gross_win_rate | 0.3828 |
| sharpe_ratio | -6.2894 |
| sortino_ratio | -1.9800 |
| max_drawdown | 0.9116 |
| cagr | -0.6137 |
| net_avg_win | 43.7710 |
| net_avg_loss | -55.0289 |
| avg_hold_time_bars | 11.0601 |
| exposure | 0.2509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

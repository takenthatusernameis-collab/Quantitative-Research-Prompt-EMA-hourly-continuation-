# EMA Hourly Continuation — GMEE/USDT P26_89

**Symbol:** GMEE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.5925 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8405 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -4.5211 |
| sortino_ratio | -1.7127 |
| max_drawdown | 0.8743 |
| cagr | -0.5555 |
| net_avg_win | 38.4297 |
| net_avg_loss | -54.5741 |
| avg_hold_time_bars | 9.7639 |
| exposure | 0.3195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

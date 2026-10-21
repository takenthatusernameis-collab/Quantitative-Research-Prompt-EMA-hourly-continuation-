# EMA Hourly Continuation — CELR/USDT P12_100

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8678 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.7271 |
| sortino_ratio | -0.8605 |
| max_drawdown | 0.6664 |
| cagr | -0.3273 |
| net_avg_win | 67.2568 |
| net_avg_loss | -79.9610 |
| avg_hold_time_bars | 26.0282 |
| exposure | 0.5854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

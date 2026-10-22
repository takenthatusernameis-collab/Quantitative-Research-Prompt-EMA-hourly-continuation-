# EMA Hourly Continuation — SHIB/USDT P8_50

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.4850 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -8.4065 |
| sortino_ratio | -3.9862 |
| max_drawdown | 0.9935 |
| cagr | -0.8655 |
| net_avg_win | 18.5250 |
| net_avg_loss | -29.9539 |
| avg_hold_time_bars | 8.5561 |
| exposure | 0.4469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

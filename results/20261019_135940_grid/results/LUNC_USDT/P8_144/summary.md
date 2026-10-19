# EMA Hourly Continuation — LUNC/USDT P8_144

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.5396 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8302 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -4.7114 |
| sortino_ratio | -1.5968 |
| max_drawdown | 0.8613 |
| cagr | -0.5387 |
| net_avg_win | 38.1730 |
| net_avg_loss | -57.4290 |
| avg_hold_time_bars | 27.2896 |
| exposure | 0.7281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

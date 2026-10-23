# EMA Hourly Continuation — PUNDIX/USDT P8_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.5396 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.9464 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -6.5978 |
| sortino_ratio | -3.0294 |
| max_drawdown | 0.9766 |
| cagr | -0.7703 |
| net_avg_win | 23.5200 |
| net_avg_loss | -36.3953 |
| avg_hold_time_bars | 9.8521 |
| exposure | 0.4783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

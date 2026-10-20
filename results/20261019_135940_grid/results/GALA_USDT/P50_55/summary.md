# EMA Hourly Continuation — GALA/USDT P50_55

**Symbol:** GALA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 840 |
| net_profit_factor | 0.1942 |
| net_win_rate | 0.3226 |
| gross_profit_factor | 0.5471 |
| gross_win_rate | 0.3738 |
| sharpe_ratio | -13.0197 |
| sortino_ratio | -5.5290 |
| max_drawdown | 0.9995 |
| cagr | -0.9495 |
| net_avg_win | 8.8881 |
| net_avg_loss | -21.7981 |
| avg_hold_time_bars | 1.9250 |
| exposure | 0.0735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

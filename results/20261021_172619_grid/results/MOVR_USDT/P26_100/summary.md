# EMA Hourly Continuation — MOVR/USDT P26_100

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6889 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -2.7889 |
| sortino_ratio | -0.8754 |
| max_drawdown | 0.6697 |
| cagr | -0.3319 |
| net_avg_win | 63.5249 |
| net_avg_loss | -76.6692 |
| avg_hold_time_bars | 14.1656 |
| exposure | 0.3149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

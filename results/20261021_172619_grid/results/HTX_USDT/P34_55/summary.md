# EMA Hourly Continuation — HTX/USDT P34_55

**Symbol:** HTX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.2468 |
| net_win_rate | 0.3034 |
| gross_profit_factor | 0.4706 |
| gross_win_rate | 0.3061 |
| sharpe_ratio | -8.2672 |
| sortino_ratio | -2.3749 |
| max_drawdown | 0.9425 |
| cagr | -0.6777 |
| net_avg_win | 26.8564 |
| net_avg_loss | -47.3995 |
| avg_hold_time_bars | 6.9235 |
| exposure | 0.1187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

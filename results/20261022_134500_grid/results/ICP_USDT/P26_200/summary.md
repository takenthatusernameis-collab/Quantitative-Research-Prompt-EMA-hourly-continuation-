# EMA Hourly Continuation — ICP/USDT P26_200

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.5847 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8740 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -3.3763 |
| sortino_ratio | -0.9689 |
| max_drawdown | 0.7070 |
| cagr | -0.3773 |
| net_avg_win | 49.9668 |
| net_avg_loss | -74.1131 |
| avg_hold_time_bars | 29.4005 |
| exposure | 0.5640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

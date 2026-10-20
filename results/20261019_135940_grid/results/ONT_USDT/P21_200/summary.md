# EMA Hourly Continuation — ONT/USDT P21_200

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.5751 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8000 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -3.6100 |
| sortino_ratio | -1.0522 |
| max_drawdown | 0.7294 |
| cagr | -0.3941 |
| net_avg_win | 51.1115 |
| net_avg_loss | -69.7736 |
| avg_hold_time_bars | 29.9792 |
| exposure | 0.5860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

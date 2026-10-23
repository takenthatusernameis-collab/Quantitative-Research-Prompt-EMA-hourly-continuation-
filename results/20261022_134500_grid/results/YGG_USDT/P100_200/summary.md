# EMA Hourly Continuation — YGG/USDT P100_200

**Symbol:** YGG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.5845 |
| sortino_ratio | -0.7055 |
| max_drawdown | 0.5947 |
| cagr | -0.2895 |
| net_avg_win | 53.3549 |
| net_avg_loss | -83.0442 |
| avg_hold_time_bars | 9.4605 |
| exposure | 0.1627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

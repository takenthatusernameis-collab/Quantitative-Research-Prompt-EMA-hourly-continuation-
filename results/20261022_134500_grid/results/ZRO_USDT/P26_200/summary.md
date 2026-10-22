# EMA Hourly Continuation — ZRO/USDT P26_200

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7359 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -2.0387 |
| sortino_ratio | -0.5954 |
| max_drawdown | 0.4847 |
| cagr | -0.2445 |
| net_avg_win | 69.6724 |
| net_avg_loss | -89.5432 |
| avg_hold_time_bars | 28.6329 |
| exposure | 0.5536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

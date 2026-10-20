# EMA Hourly Continuation — XAI/USDT P50_200

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6373 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.8503 |
| sortino_ratio | -0.7837 |
| max_drawdown | 0.6335 |
| cagr | -0.3107 |
| net_avg_win | 60.6059 |
| net_avg_loss | -81.6511 |
| avg_hold_time_bars | 26.5984 |
| exposure | 0.4606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

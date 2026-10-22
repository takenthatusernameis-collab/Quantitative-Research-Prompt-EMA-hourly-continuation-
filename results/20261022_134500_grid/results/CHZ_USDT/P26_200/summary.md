# EMA Hourly Continuation — CHZ/USDT P26_200

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8269 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1599 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | -1.0421 |
| sortino_ratio | -0.2737 |
| max_drawdown | 0.3646 |
| cagr | -0.1241 |
| net_avg_win | 72.7352 |
| net_avg_loss | -102.8932 |
| avg_hold_time_bars | 38.9594 |
| exposure | 0.6110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

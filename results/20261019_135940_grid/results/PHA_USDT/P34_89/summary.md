# EMA Hourly Continuation — PHA/USDT P34_89

**Symbol:** PHA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5109 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.7957 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -5.2327 |
| sortino_ratio | -1.9725 |
| max_drawdown | 0.9087 |
| cagr | -0.6117 |
| net_avg_win | 29.8876 |
| net_avg_loss | -46.2465 |
| avg_hold_time_bars | 6.7423 |
| exposure | 0.2200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

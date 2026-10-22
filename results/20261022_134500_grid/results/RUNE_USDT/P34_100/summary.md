# EMA Hourly Continuation — RUNE/USDT P34_100

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.6176 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -3.5390 |
| sortino_ratio | -1.2264 |
| max_drawdown | 0.7907 |
| cagr | -0.4408 |
| net_avg_win | 41.8881 |
| net_avg_loss | -66.2552 |
| avg_hold_time_bars | 10.7696 |
| exposure | 0.2932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

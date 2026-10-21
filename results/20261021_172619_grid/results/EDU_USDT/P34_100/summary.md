# EMA Hourly Continuation — EDU/USDT P34_100

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7192 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.1638 |
| sortino_ratio | -0.6812 |
| max_drawdown | 0.5617 |
| cagr | -0.2689 |
| net_avg_win | 59.2913 |
| net_avg_loss | -76.8981 |
| avg_hold_time_bars | 11.7751 |
| exposure | 0.2606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

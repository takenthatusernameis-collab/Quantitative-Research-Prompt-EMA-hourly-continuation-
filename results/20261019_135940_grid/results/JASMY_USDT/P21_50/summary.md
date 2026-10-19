# EMA Hourly Continuation — JASMY/USDT P21_50

**Symbol:** JASMY/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.5098 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8856 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -6.8714 |
| sortino_ratio | -3.0811 |
| max_drawdown | 0.9768 |
| cagr | -0.7745 |
| net_avg_win | 21.9765 |
| net_avg_loss | -36.6770 |
| avg_hold_time_bars | 3.8448 |
| exposure | 0.1756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

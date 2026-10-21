# EMA Hourly Continuation — CTC/USDT P20_50

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 0.9906 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.6358 |
| sortino_ratio | -0.8938 |
| max_drawdown | 0.6528 |
| cagr | -0.3366 |
| net_avg_win | 52.4439 |
| net_avg_loss | -75.2263 |
| avg_hold_time_bars | 8.3918 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

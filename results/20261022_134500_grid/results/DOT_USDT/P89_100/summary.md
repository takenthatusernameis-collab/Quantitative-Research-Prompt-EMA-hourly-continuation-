# EMA Hourly Continuation — DOT/USDT P89_100

**Symbol:** DOT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.2034 |
| net_win_rate | 0.3738 |
| gross_profit_factor | 0.7359 |
| gross_win_rate | 0.4125 |
| sharpe_ratio | -9.7398 |
| sortino_ratio | -3.3408 |
| max_drawdown | 0.9885 |
| cagr | -0.8303 |
| net_avg_win | 12.4340 |
| net_avg_loss | -36.4934 |
| avg_hold_time_bars | 1.8619 |
| exposure | 0.0460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

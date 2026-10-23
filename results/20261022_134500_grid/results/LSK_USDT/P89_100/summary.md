# EMA Hourly Continuation — LSK/USDT P89_100

**Symbol:** LSK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.2938 |
| net_win_rate | 0.4023 |
| gross_profit_factor | 0.8273 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -7.8066 |
| sortino_ratio | -2.5703 |
| max_drawdown | 0.9648 |
| cagr | -0.7350 |
| net_avg_win | 18.7523 |
| net_avg_loss | -42.9465 |
| avg_hold_time_bars | 3.6034 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

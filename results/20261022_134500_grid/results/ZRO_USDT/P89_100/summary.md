# EMA Hourly Continuation — ZRO/USDT P89_100

**Symbol:** ZRO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.2636 |
| net_win_rate | 0.3806 |
| gross_profit_factor | 0.5481 |
| gross_win_rate | 0.3903 |
| sharpe_ratio | -8.3539 |
| sortino_ratio | -2.8258 |
| max_drawdown | 0.9656 |
| cagr | -0.7632 |
| net_avg_win | 17.6270 |
| net_avg_loss | -41.0895 |
| avg_hold_time_bars | 1.9146 |
| exposure | 0.0483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

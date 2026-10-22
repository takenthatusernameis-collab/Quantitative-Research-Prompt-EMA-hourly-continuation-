# EMA Hourly Continuation — HTX/USDT P26_100

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.3267 |
| net_win_rate | 0.3254 |
| gross_profit_factor | 0.8438 |
| gross_win_rate | 0.3913 |
| sharpe_ratio | -11.4313 |
| sortino_ratio | -4.4441 |
| max_drawdown | 0.9977 |
| cagr | -0.9098 |
| net_avg_win | 20.8695 |
| net_avg_loss | -30.8079 |
| avg_hold_time_bars | 12.2286 |
| exposure | 0.3946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

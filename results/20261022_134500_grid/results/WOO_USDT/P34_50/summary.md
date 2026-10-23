# EMA Hourly Continuation — WOO/USDT P34_50

**Symbol:** WOO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.4612 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -7.2365 |
| sortino_ratio | -3.0215 |
| max_drawdown | 0.9749 |
| cagr | -0.7672 |
| net_avg_win | 21.4927 |
| net_avg_loss | -38.3907 |
| avg_hold_time_bars | 3.2934 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

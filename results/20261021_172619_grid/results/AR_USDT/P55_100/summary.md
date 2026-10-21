# EMA Hourly Continuation — AR/USDT P55_100

**Symbol:** AR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7319 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9441 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.7256 |
| sortino_ratio | -0.4706 |
| max_drawdown | 0.4474 |
| cagr | -0.1949 |
| net_avg_win | 64.0394 |
| net_avg_loss | -85.1180 |
| avg_hold_time_bars | 7.2617 |
| exposure | 0.1198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

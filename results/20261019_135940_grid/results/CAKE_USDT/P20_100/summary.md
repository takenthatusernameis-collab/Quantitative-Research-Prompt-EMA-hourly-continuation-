# EMA Hourly Continuation — CAKE/USDT P20_100

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 1.0362 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -3.7305 |
| sortino_ratio | -1.2989 |
| max_drawdown | 0.8178 |
| cagr | -0.4704 |
| net_avg_win | 45.8251 |
| net_avg_loss | -69.8273 |
| avg_hold_time_bars | 14.8728 |
| exposure | 0.4198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

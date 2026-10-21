# EMA Hourly Continuation — CAKE/USDT P21_100

**Symbol:** CAKE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.8206 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0840 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -1.3901 |
| sortino_ratio | -0.4317 |
| max_drawdown | 0.4423 |
| cagr | -0.1810 |
| net_avg_win | 74.5408 |
| net_avg_loss | -97.7008 |
| avg_hold_time_bars | 19.1092 |
| exposure | 0.4056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

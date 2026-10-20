# EMA Hourly Continuation — DYDX/USDT P26_100

**Symbol:** DYDX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6921 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 1.0232 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.2746 |
| sortino_ratio | -1.1920 |
| max_drawdown | 0.7675 |
| cagr | -0.4301 |
| net_avg_win | 52.0006 |
| net_avg_loss | -73.3362 |
| avg_hold_time_bars | 11.6888 |
| exposure | 0.3517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

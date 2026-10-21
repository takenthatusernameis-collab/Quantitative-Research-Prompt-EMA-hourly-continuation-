# EMA Hourly Continuation — CAKE/USDT P50_100

**Symbol:** CAKE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.6575 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9449 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.3495 |
| sortino_ratio | -0.6200 |
| max_drawdown | 0.5347 |
| cagr | -0.2468 |
| net_avg_win | 58.8969 |
| net_avg_loss | -85.9491 |
| avg_hold_time_bars | 10.2271 |
| exposure | 0.1576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

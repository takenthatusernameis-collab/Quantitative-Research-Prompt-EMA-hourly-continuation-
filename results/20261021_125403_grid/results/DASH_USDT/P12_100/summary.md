# EMA Hourly Continuation — DASH/USDT P12_100

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7504 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9464 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -1.8882 |
| sortino_ratio | -0.5651 |
| max_drawdown | 0.5304 |
| cagr | -0.2294 |
| net_avg_win | 67.7705 |
| net_avg_loss | -84.7465 |
| avg_hold_time_bars | 28.7477 |
| exposure | 0.5750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CAKE/USDT P12_100

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.8260 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0619 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -1.3347 |
| sortino_ratio | -0.4138 |
| max_drawdown | 0.4446 |
| cagr | -0.1748 |
| net_avg_win | 75.6912 |
| net_avg_loss | -96.8873 |
| avg_hold_time_bars | 26.4475 |
| exposure | 0.5614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — BAT/USDT P26_200

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.8054 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9995 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.1369 |
| sortino_ratio | -0.2871 |
| max_drawdown | 0.3594 |
| cagr | -0.1247 |
| net_avg_win | 74.9560 |
| net_avg_loss | -94.2639 |
| avg_hold_time_bars | 40.5897 |
| exposure | 0.5756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

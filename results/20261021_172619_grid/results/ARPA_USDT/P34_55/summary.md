# EMA Hourly Continuation — ARPA/USDT P34_55

**Symbol:** ARPA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.5453 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.8151 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -4.3130 |
| sortino_ratio | -1.2900 |
| max_drawdown | 0.7861 |
| cagr | -0.4492 |
| net_avg_win | 48.5847 |
| net_avg_loss | -69.2566 |
| avg_hold_time_bars | 6.3986 |
| exposure | 0.1271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

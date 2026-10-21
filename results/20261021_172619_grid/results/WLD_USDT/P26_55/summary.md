# EMA Hourly Continuation — WLD/USDT P26_55

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.7449 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9357 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -1.8053 |
| sortino_ratio | -0.5107 |
| max_drawdown | 0.4633 |
| cagr | -0.2092 |
| net_avg_win | 68.4579 |
| net_avg_loss | -86.4395 |
| avg_hold_time_bars | 8.2934 |
| exposure | 0.1478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

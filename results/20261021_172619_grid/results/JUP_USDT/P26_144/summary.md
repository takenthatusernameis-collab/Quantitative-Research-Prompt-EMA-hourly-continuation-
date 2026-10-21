# EMA Hourly Continuation — JUP/USDT P26_144

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8453 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 0.9971 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.0087 |
| sortino_ratio | -0.2856 |
| max_drawdown | 0.3396 |
| cagr | -0.1252 |
| net_avg_win | 79.1764 |
| net_avg_loss | -94.6232 |
| avg_hold_time_bars | 23.0689 |
| exposure | 0.4110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

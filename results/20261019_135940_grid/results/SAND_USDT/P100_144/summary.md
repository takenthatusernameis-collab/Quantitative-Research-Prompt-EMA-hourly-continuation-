# EMA Hourly Continuation — SAND/USDT P100_144

**Symbol:** SAND/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.4559 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.9215 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -5.4574 |
| sortino_ratio | -1.6965 |
| max_drawdown | 0.8765 |
| cagr | -0.5652 |
| net_avg_win | 33.5307 |
| net_avg_loss | -61.2491 |
| avg_hold_time_bars | 3.4979 |
| exposure | 0.0766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

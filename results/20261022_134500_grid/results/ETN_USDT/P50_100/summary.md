# EMA Hourly Continuation — ETN/USDT P50_100

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.3369 |
| net_win_rate | 0.3506 |
| gross_profit_factor | 0.5331 |
| gross_win_rate | 0.3643 |
| sharpe_ratio | -9.5659 |
| sortino_ratio | -3.7843 |
| max_drawdown | 0.9824 |
| cagr | -0.8509 |
| net_avg_win | 21.6854 |
| net_avg_loss | -34.7522 |
| avg_hold_time_bars | 4.9070 |
| exposure | 0.1749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

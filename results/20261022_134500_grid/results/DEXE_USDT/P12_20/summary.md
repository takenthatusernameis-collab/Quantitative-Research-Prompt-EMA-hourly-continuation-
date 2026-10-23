# EMA Hourly Continuation — DEXE/USDT P12_20

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1490 |
| net_profit_factor | 0.1641 |
| net_win_rate | 0.3591 |
| gross_profit_factor | 0.4687 |
| gross_win_rate | 0.3960 |
| sharpe_ratio | -15.3746 |
| sortino_ratio | -8.5345 |
| max_drawdown | 1.0000 |
| cagr | -0.9886 |
| net_avg_win | 3.6682 |
| net_avg_loss | -12.5261 |
| avg_hold_time_bars | 3.7040 |
| exposure | 0.2509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — THETA/USDT P12_100

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7807 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -1.6576 |
| sortino_ratio | -0.4788 |
| max_drawdown | 0.4690 |
| cagr | -0.1986 |
| net_avg_win | 77.0623 |
| net_avg_loss | -90.8677 |
| avg_hold_time_bars | 32.1703 |
| exposure | 0.6010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

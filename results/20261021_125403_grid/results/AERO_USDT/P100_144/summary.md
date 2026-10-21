# EMA Hourly Continuation — AERO/USDT P100_144

**Symbol:** AERO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8695 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -1.6834 |
| sortino_ratio | -0.3317 |
| max_drawdown | 0.3165 |
| cagr | -0.1406 |
| net_avg_win | 73.5914 |
| net_avg_loss | -95.2406 |
| avg_hold_time_bars | 6.3508 |
| exposure | 0.0551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — G/USDT P12_100

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5602 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -3.8446 |
| sortino_ratio | -1.2842 |
| max_drawdown | 0.7695 |
| cagr | -0.4602 |
| net_avg_win | 41.7708 |
| net_avg_loss | -63.0674 |
| avg_hold_time_bars | 24.1976 |
| exposure | 0.6247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

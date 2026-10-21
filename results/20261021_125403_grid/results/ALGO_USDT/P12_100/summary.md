# EMA Hourly Continuation — ALGO/USDT P12_100

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8564 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0390 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -1.0051 |
| sortino_ratio | -0.3063 |
| max_drawdown | 0.3666 |
| cagr | -0.1339 |
| net_avg_win | 78.2458 |
| net_avg_loss | -95.9328 |
| avg_hold_time_bars | 28.0732 |
| exposure | 0.5755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — PENDLE/USDT P100_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6465 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8400 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -1.9754 |
| sortino_ratio | -0.4317 |
| max_drawdown | 0.4030 |
| cagr | -0.1800 |
| net_avg_win | 65.8430 |
| net_avg_loss | -88.1084 |
| avg_hold_time_bars | 5.9702 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

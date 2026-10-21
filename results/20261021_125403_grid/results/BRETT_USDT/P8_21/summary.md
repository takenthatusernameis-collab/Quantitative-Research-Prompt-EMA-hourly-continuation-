# EMA Hourly Continuation — BRETT/USDT P8_21

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8186 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0205 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -1.3811 |
| sortino_ratio | -0.4595 |
| max_drawdown | 0.4595 |
| cagr | -0.1918 |
| net_avg_win | 69.3656 |
| net_avg_loss | -87.7976 |
| avg_hold_time_bars | 6.2801 |
| exposure | 0.1532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

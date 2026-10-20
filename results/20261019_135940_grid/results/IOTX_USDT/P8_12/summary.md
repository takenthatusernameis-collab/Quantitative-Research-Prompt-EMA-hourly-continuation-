# EMA Hourly Continuation — IOTX/USDT P8_12

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1748 |
| net_profit_factor | 0.2691 |
| net_win_rate | 0.3804 |
| gross_profit_factor | 0.7987 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -16.8034 |
| sortino_ratio | -10.1800 |
| max_drawdown | 1.0000 |
| cagr | -0.9953 |
| net_avg_win | 5.5368 |
| net_avg_loss | -12.6334 |
| avg_hold_time_bars | 2.0011 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

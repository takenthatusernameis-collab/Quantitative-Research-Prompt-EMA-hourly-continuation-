# EMA Hourly Continuation — AXL/USDT P20_26

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.4554 |
| net_win_rate | 0.3767 |
| gross_profit_factor | 0.6332 |
| gross_win_rate | 0.3767 |
| sharpe_ratio | -4.4618 |
| sortino_ratio | -1.0812 |
| max_drawdown | 0.7357 |
| cagr | -0.3967 |
| net_avg_win | 54.7829 |
| net_avg_loss | -72.7003 |
| avg_hold_time_bars | 5.2123 |
| exposure | 0.0689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

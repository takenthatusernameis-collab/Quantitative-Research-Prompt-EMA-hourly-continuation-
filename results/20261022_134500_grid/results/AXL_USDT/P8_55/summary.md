# EMA Hourly Continuation — AXL/USDT P8_55

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.5966 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -6.6631 |
| sortino_ratio | -3.1084 |
| max_drawdown | 0.9778 |
| cagr | -0.7765 |
| net_avg_win | 29.7381 |
| net_avg_loss | -38.8836 |
| avg_hold_time_bars | 10.2831 |
| exposure | 0.5160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

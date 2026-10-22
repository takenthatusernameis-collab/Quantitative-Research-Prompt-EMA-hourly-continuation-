# EMA Hourly Continuation — SYN/USDT P8_55

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.8082 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.7507 |
| sortino_ratio | -0.6504 |
| max_drawdown | 0.5429 |
| cagr | -0.2611 |
| net_avg_win | 66.9557 |
| net_avg_loss | -81.6286 |
| avg_hold_time_bars | 15.2978 |
| exposure | 0.4694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CFX/USDT P21_26

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1256 |
| net_profit_factor | 0.1937 |
| net_win_rate | 0.3304 |
| gross_profit_factor | 0.6447 |
| gross_win_rate | 0.3766 |
| sharpe_ratio | -16.2123 |
| sortino_ratio | -8.4701 |
| max_drawdown | 1.0000 |
| cagr | -0.9897 |
| net_avg_win | 5.7897 |
| net_avg_loss | -14.7475 |
| avg_hold_time_bars | 1.8073 |
| exposure | 0.1032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — HNT/USDT P8_12

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.5387 |
| net_win_rate | 0.4078 |
| gross_profit_factor | 0.7259 |
| gross_win_rate | 0.4078 |
| sharpe_ratio | -3.3408 |
| sortino_ratio | -0.7569 |
| max_drawdown | 0.5917 |
| cagr | -0.2953 |
| net_avg_win | 65.6708 |
| net_avg_loss | -83.9593 |
| avg_hold_time_bars | 5.8157 |
| exposure | 0.0674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

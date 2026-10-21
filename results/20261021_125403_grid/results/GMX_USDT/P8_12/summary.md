# EMA Hourly Continuation — GMX/USDT P8_12

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7086 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.1055 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -2.7725 |
| sortino_ratio | -0.8568 |
| max_drawdown | 0.6647 |
| cagr | -0.3263 |
| net_avg_win | 64.8220 |
| net_avg_loss | -94.2755 |
| avg_hold_time_bars | 4.7355 |
| exposure | 0.1001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

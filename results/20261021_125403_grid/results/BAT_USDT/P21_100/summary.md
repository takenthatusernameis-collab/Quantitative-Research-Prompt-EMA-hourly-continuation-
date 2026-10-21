# EMA Hourly Continuation — BAT/USDT P21_100

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0764 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.5576 |
| sortino_ratio | -0.5171 |
| max_drawdown | 0.5339 |
| cagr | -0.2119 |
| net_avg_win | 71.8962 |
| net_avg_loss | -94.0811 |
| avg_hold_time_bars | 16.4184 |
| exposure | 0.3978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

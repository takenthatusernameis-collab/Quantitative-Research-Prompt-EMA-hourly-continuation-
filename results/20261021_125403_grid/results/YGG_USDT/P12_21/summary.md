# EMA Hourly Continuation — YGG/USDT P12_21

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7461 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0485 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -2.1393 |
| sortino_ratio | -0.6425 |
| max_drawdown | 0.5782 |
| cagr | -0.2546 |
| net_avg_win | 69.2777 |
| net_avg_loss | -95.4359 |
| avg_hold_time_bars | 4.4726 |
| exposure | 0.0886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

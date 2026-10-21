# EMA Hourly Continuation — CFG/USDT P8_21

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.6282 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8370 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -3.4383 |
| sortino_ratio | -1.1582 |
| max_drawdown | 0.7438 |
| cagr | -0.4119 |
| net_avg_win | 48.9765 |
| net_avg_loss | -64.5068 |
| avg_hold_time_bars | 5.2870 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LTC/USDT P12_21

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1451 |
| net_profit_factor | 0.1756 |
| net_win_rate | 0.3563 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -16.6488 |
| sortino_ratio | -9.2624 |
| max_drawdown | 1.0000 |
| cagr | -0.9935 |
| net_avg_win | 4.1214 |
| net_avg_loss | -12.9879 |
| avg_hold_time_bars | 2.0669 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

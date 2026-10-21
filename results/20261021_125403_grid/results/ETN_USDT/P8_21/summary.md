# EMA Hourly Continuation — ETN/USDT P8_21

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4359 |
| net_win_rate | 0.3861 |
| gross_profit_factor | 0.5699 |
| gross_win_rate | 0.3861 |
| sharpe_ratio | -5.1409 |
| sortino_ratio | -1.6197 |
| max_drawdown | 0.7984 |
| cagr | -0.5296 |
| net_avg_win | 38.1553 |
| net_avg_loss | -55.0517 |
| avg_hold_time_bars | 6.3837 |
| exposure | 0.1446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

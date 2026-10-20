# EMA Hourly Continuation — HNT/USDT P8_21

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1658 |
| net_profit_factor | 0.3337 |
| net_win_rate | 0.3914 |
| gross_profit_factor | 0.6610 |
| gross_win_rate | 0.4071 |
| sharpe_ratio | -12.8600 |
| sortino_ratio | -7.4181 |
| max_drawdown | 0.9999 |
| cagr | -0.9750 |
| net_avg_win | 7.7164 |
| net_avg_loss | -14.8732 |
| avg_hold_time_bars | 3.3359 |
| exposure | 0.2514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

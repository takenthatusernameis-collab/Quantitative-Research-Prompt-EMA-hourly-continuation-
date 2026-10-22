# EMA Hourly Continuation — PUFFER/USDT P8_21

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7012 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9175 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.9596 |
| sortino_ratio | -1.0290 |
| max_drawdown | 0.6624 |
| cagr | -0.3779 |
| net_avg_win | 63.9714 |
| net_avg_loss | -81.8209 |
| avg_hold_time_bars | 6.9812 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

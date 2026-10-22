# EMA Hourly Continuation — MOVR/USDT P8_55

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.7598 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -2.1729 |
| sortino_ratio | -0.8382 |
| max_drawdown | 0.6364 |
| cagr | -0.3207 |
| net_avg_win | 54.8815 |
| net_avg_loss | -69.8926 |
| avg_hold_time_bars | 14.2514 |
| exposure | 0.4716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

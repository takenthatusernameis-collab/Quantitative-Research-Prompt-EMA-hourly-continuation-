# EMA Hourly Continuation — MASK/USDT P8_50

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.6067 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8482 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -4.3138 |
| sortino_ratio | -1.7139 |
| max_drawdown | 0.8625 |
| cagr | -0.5462 |
| net_avg_win | 36.9516 |
| net_avg_loss | -52.2078 |
| avg_hold_time_bars | 12.6154 |
| exposure | 0.4473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

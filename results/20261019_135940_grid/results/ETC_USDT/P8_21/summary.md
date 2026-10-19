# EMA Hourly Continuation — ETC/USDT P8_21

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1663 |
| net_profit_factor | 0.2468 |
| net_win_rate | 0.4011 |
| gross_profit_factor | 0.7602 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -14.8164 |
| sortino_ratio | -8.6243 |
| max_drawdown | 1.0000 |
| cagr | -0.9890 |
| net_avg_win | 4.9126 |
| net_avg_loss | -13.3299 |
| avg_hold_time_bars | 2.9886 |
| exposure | 0.2259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RUNE/USDT P8_50

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.7902 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -2.1765 |
| sortino_ratio | -0.7974 |
| max_drawdown | 0.6399 |
| cagr | -0.3070 |
| net_avg_win | 69.5221 |
| net_avg_loss | -87.1822 |
| avg_hold_time_bars | 14.5832 |
| exposure | 0.4342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

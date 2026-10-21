# EMA Hourly Continuation — MOODENG/USDT P89_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.8431 |
| net_win_rate | 0.5370 |
| gross_profit_factor | 1.1581 |
| gross_win_rate | 0.5370 |
| sharpe_ratio | -0.6086 |
| sortino_ratio | -0.1007 |
| max_drawdown | 0.1568 |
| cagr | -0.0459 |
| net_avg_win | 85.6967 |
| net_avg_loss | -117.9041 |
| avg_hold_time_bars | 4.3611 |
| exposure | 0.0261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
